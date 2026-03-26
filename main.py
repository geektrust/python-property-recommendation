from typing import List, Dict, Any


class Main:
    #
    # ---------------------------------------------------------------------------
    # Implement your solution here
    #
    # ---------------------------------------------------------------------------
    def recommend_properties(
        self,
        properties: List[Dict[str, Any]],
        events: List[Dict[str, Any]],
        top_n: int,
    ) -> List[Dict[str, Any]]:
        """
        Build a content-based recommendation engine that scores every unseen
        property for each user based on their demonstrated preferences.

        Args:
            properties: List of property dictionaries with keys:
                        property_id, suburb, property_type, bedrooms,
                        price, has_parking
            events:     List of interaction event dictionaries with keys:
                        user_id, property_id, event_type, event_time
                        event_type is one of: 'view' (weight 1.0),
                                              'save' (weight 2.0),
                                              'enquiry' (weight 3.0)
            top_n:      Number of recommendations to return per user

        Returns:
            List of per-user recommendation dictionaries sorted by user_id
            ascending. Each entry has the shape:
            {
                "user_id": str,
                "recommendations": [
                    {"property_id": str, "score": float},
                    ...   # up to top_n items, sorted by score desc,
                          # then property_id asc as tiebreaker
                ]
            }

        Scoring logic (all five sub-scores averaged):
            suburb_score  : weighted_suburb_count / total_weighted_interactions
                            (0 if suburb not seen)
            type_score    : weighted_type_count / total_weighted_interactions
                            (0 if type not seen)
            bedroom_score : 1.0 - |property_bedrooms - user_weighted_avg_bedrooms|
                                  / max_bedrooms_in_dataset   (clamped >= 0)
            price_score   : 1.0 - |property_price - user_weighted_avg_price|
                                  / max_price_in_dataset      (clamped >= 0)
            parking_score : 1.0 if has_parking matches user's weighted majority
                            preference, else 0.0
            final_score   : round((suburb_score + type_score + bedroom_score
                                   + price_score + parking_score) / 5.0, 6)
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Implement recommend_properties")
