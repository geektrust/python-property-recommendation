This is the starter kit for the problem statement property recommendation

## Problem Statement

### Property Recommendation Scoring

You are building a content-based recommendation engine for a real estate platform.
The platform records user interaction events (views, saves, enquiries) on property listings.
Your engine must infer each user's preferences from their interaction history and score
every unseen property to surface the most relevant recommendations.

Each property has the following fields:
```
{
    "property_id": str,
    "suburb": str,
    "property_type": str,   # one of: "house", "apartment", "townhouse"
    "bedrooms": int,
    "price": float,
    "has_parking": bool,
}
```

Each interaction event has the following fields:
```
{
    "user_id": str,
    "property_id": str,
    "event_type": str,      # one of: "view", "save", "enquiry"
    "event_time": str,      # ISO-8601 UTC, e.g. "2025-06-01T09:00:00Z"
}
```

#### Requirements

1. **Interaction weights** — each event type carries a different signal strength:
   - `view` = 1.0
   - `save` = 2.0
   - `enquiry` = 3.0

2. **Build a per-user preference profile** by aggregating the features of every
   property the user has interacted with, weighted by event type:
   - Weighted suburb counts
   - Weighted property type counts
   - Weighted average number of bedrooms
   - Weighted average price
   - Weighted parking preference (sum of weights for `has_parking=True` vs `False`)

3. **Exclude seen properties** — never recommend a property the user has already
   interacted with (any event type).

4. **Score each unseen property** using five sub-scores, then average them:

   - `suburb_score`: `weighted_suburb_count / total_weighted_interactions` (0 if suburb not in history)
   - `type_score`: `weighted_type_count / total_weighted_interactions` (0 if type not in history)
   - `bedroom_score`: `max(0.0, 1.0 - |property_bedrooms - user_weighted_avg_bedrooms| / max_bedrooms_in_dataset)`
   - `price_score`: `max(0.0, 1.0 - |property_price - user_weighted_avg_price| / max_price_in_dataset)`
   - `parking_score`: `1.0` if `has_parking` matches the user's weighted majority preference, else `0.0`

   ```
   final_score = round((suburb_score + type_score + bedroom_score + price_score + parking_score) / 5.0, 6)
   ```

5. **Return top-N recommendations per user**, sorted by `score` descending,
   then `property_id` ascending as a tiebreaker.

6. Return a list of dictionaries with exactly these keys:
   ```
   {
       "user_id": str,
       "recommendations": [
           {
               "property_id": str,
               "score": float,   # rounded to 6 decimal places
           },
           ...
       ]
   }
   ```

7. Sort output by `user_id` ascending.

8. Users with no interaction history must be excluded from the output.

9. If fewer than `top_n` unseen properties exist for a user, return only what is available.

#### How to execute
```
./run.sh "{\"properties\": [{\"property_id\": \"p1\", \"suburb\": \"Richmond\", \"property_type\": \"apartment\", \"bedrooms\": 2, \"price\": 650000, \"has_parking\": true}], \"events\": [{\"user_id\": \"u1\", \"property_id\": \"p1\", \"event_type\": \"view\", \"event_time\": \"2025-06-01T09:00:00Z\"}], \"top_n\": 2}"
```
