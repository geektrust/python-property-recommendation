from datetime import datetime, timezone, timedelta
from typing import Iterable, List, Dict, Any
from collections import defaultdict

class Main:
    #
    # ---------------------------------------------------------------------------
    # Implement your solution here
    #
    # ---------------------------------------------------------------------------
    def aggregate_events_by_window(self, 
        events: Iterable[Dict[str, Any]],
        window_minutes: int,
    ) -> List[Dict[str, Any]]:
        """
        Group events into tumbling time windows and compute per-tenant
        aggregates.
        
        Args:
            events: Iterable of event dictionaries with keys:
                    tenant_id, user_id, event_time, amount
            window_minutes: Size of tumbling window in minutes
        
        Returns:
            List of aggregate dictionaries sorted by (tenant_id, window_start)
        """
        # TODO: Implement your solution here
        raise NotImplementedError("Implement aggregate_events_by_window")


    # #
    # # ---------------------------------------------------------------------------
    # # Test harness (do not modify)
    # #
    # # ---------------------------------------------------------------------------
    # def _normalize(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    #     """Normalize records for comparison: sort and round floats."""

    #     normalized = []
    #     for r in records:
    #         norm_record = {}
    #         for k, v in r.items():
    #             if isinstance(v, float):
    #                 norm_record[k] = round(v, 6)
    #             else:
    #                 norm_record[k] = v
    #                 normalized.append(norm_record)
    #     return sorted(normalized, key=lambda x: (x["tenant_id"],
    #                                             x["window_start"]))


    # def _print_diff(expected, actual):
    #     print(" Expected:")
    #     for row in expected:
    #         print(" ", row)
    #         print(" Actual:")
    #     for row in actual:
    #         print(" ", row)


    # def run_tests():

    #     tests = []
    # # ------------------------------------------------------------------
    # # Test 0: Example from problem statement
    # # ------------------------------------------------------------------
    #     events_example = [
    #         {"tenant_id": "bank_a", "user_id": "u1", "event_time":
    #         "2025-01-01T10:01:00Z", "amount": 10.0}, {"tenant_id": "bank_a", "user_id": "u1", "event_time":
    #                                                 "2025-01-01T10:05:00Z", "amount": 20.0},
    #         {"tenant_id": "bank_a", "user_id": "u2", "event_time":
    #         "2025-01-01T10:10:00Z", "amount": 5.0},
    #         {"tenant_id": "bank_b", "user_id": "u9", "event_time":
    #         "2025-01-01T10:14:59Z", "amount": 7.5},
    #         {"tenant_id": "bank_a", "user_id": "u1", "event_time":
    #         "2025-01-01T10:16:00Z", "amount": 3.0},
    #     ]
    #     expected_example = [
    #         {
    #             "tenant_id": "bank_a",
    #             "window_start": "2025-01-01T10:00:00Z",
    #             "window_end": "2025-01-01T10:15:00Z",
    #             "event_count": 3,
    #             "unique_users": 2,
    #             "total_amount": 35.0,
    #             "avg_amount_per_event": 11.666667,
    #         },
    #         {
    #             "tenant_id": "bank_a",
    #             "window_start": "2025-01-01T10:15:00Z",
    #             "window_end": "2025-01-01T10:30:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 3.0,
    #             "avg_amount_per_event": 3.0,
    #         },
    #         {
    #             "tenant_id": "bank_b",
    #             "window_start": "2025-01-01T10:00:00Z",
    #             "window_end": "2025-01-01T10:15:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 7.5,
    #             "avg_amount_per_event": 7.5,
    #         },
    #     ]
    #     tests.append(("example", events_example, 15, expected_example))

    #     # ------------------------------------------------------------------
    #     # Test 1: Empty input
    #     # ------------------------------------------------------------------

    #     tests.append(("empty", [], 10, []))

    #     # ------------------------------------------------------------------
    #     # Test 2: Single event
    #     # ------------------------------------------------------------------
    #     events_single = [
    #         {"tenant_id": "t1", "user_id": "u1", "event_time":
    #         "2025-05-10T12:34:56Z", "amount": 100.0}
    #     ]
    #     expected_single = [
    #         {
    #             "tenant_id": "t1",
    #             "window_start": "2025-05-10T12:30:00Z",
    #             "window_end": "2025-05-10T12:45:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 100.0,
    #             "avg_amount_per_event": 100.0,
    #         }
    #     ]
    #     tests.append(("single", events_single, 15, expected_single))

    #     # ------------------------------------------------------------------
    #     # Test 3: Out-of-order events
    #     # ------------------------------------------------------------------
    #     events_out_of_order = [
    #         {"tenant_id": "t1", "user_id": "u2", "event_time":
    #         "2025-01-01T00:29:00Z", "amount": 10.0},
    #         {"tenant_id": "t1", "user_id": "u1", "event_time":
    #         "2025-01-01T00:02:00Z", "amount": 5.0},
    #         {"tenant_id": "t1", "user_id": "u1", "event_time":
    #         "2025-01-01T00:10:00Z", "amount": 5.0},
    #     ]
    #     expected_out_of_order = [
    #         {
    #             "tenant_id": "t1",
    #             "window_start": "2025-01-01T00:00:00Z",
    #             "window_end": "2025-01-01T00:15:00Z",
    #             "event_count": 2,
    #             "unique_users": 1,
    #             "total_amount": 10.0,
    #             "avg_amount_per_event": 5.0,
    #         }, {
    #             "tenant_id": "t1",
    #             "window_start": "2025-01-01T00:15:00Z",
    #             "window_end": "2025-01-01T00:30:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 10.0,
    #             "avg_amount_per_event": 10.0,
    #         },
    #     ]
    #     tests.append(("out_of_order", events_out_of_order, 15,
    #                 expected_out_of_order))

    #     # ------------------------------------------------------------------
    #     # Test 4: Multiple tenants, multiple windows
    #     # ------------------------------------------------------------------
    #     events_multi_tenant = [
    #         {"tenant_id": "A", "user_id": "u1", "event_time":
    #         "2025-01-01T09:00:00Z", "amount": 10.0},
    #         {"tenant_id": "A", "user_id": "u2", "event_time":
    #         "2025-01-01T09:14:59Z", "amount": 20.0},
    #         {"tenant_id": "A", "user_id": "u1", "event_time":
    #         "2025-01-01T09:15:00Z", "amount": 30.0},
    #         {"tenant_id": "B", "user_id": "u3", "event_time":
    #         "2025-01-01T09:07:00Z", "amount": 5.0},
    #         {"tenant_id": "B", "user_id": "u3", "event_time":
    #         "2025-01-01T09:16:00Z", "amount": 15.0},
    #     ]
    #     expected_multi_tenant = [
    #         {
    #             "tenant_id": "A",
    #             "window_start": "2025-01-01T09:00:00Z",
    #             "window_end": "2025-01-01T09:15:00Z",
    #             "event_count": 2,
    #             "unique_users": 2,
    #             "total_amount": 30.0,
    #             "avg_amount_per_event": 15.0,
    #         },
    #         {
    #             "tenant_id": "A",
    #             "window_start": "2025-01-01T09:15:00Z",
    #             "window_end": "2025-01-01T09:30:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 30.0,
    #             "avg_amount_per_event": 30.0,
    #         },
    #         {
    #             "tenant_id": "B",
    #             "window_start": "2025-01-01T09:00:00Z",
    #             "window_end": "2025-01-01T09:15:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 5.0,
    #             "avg_amount_per_event": 5.0,
    #         },
    #         {
    #             "tenant_id": "B",
    #             "window_start": "2025-01-01T09:15:00Z",
    #             "window_end": "2025-01-01T09:30:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 15.0,
    #             "avg_amount_per_event": 15.0,
    #         },
    #     ]
    #     tests.append(("multi_tenant_multi_window", events_multi_tenant, 15,
    #                 expected_multi_tenant))

    #     # ------------------------------------------------------------------
    #     # Test 5: Boundary edges (exactly on window boundaries)
    #     # ------------------------------------------------------------------
    #     events_boundary = [
    #         {"tenant_id": "T", "user_id": "u1", "event_time":
    #         "2025-01-01T00:00:00Z", "amount": 1.0},
    #         {"tenant_id": "T", "user_id": "u2", "event_time":
    #         "2025-01-01T00:15:00Z", "amount": 2.0},
    #         {"tenant_id": "T", "user_id": "u3", "event_time":
    #         "2025-01-01T00:29:59Z", "amount": 3.0},
    #     ]
    #     expected_boundary = [
    #         {
    #             "tenant_id": "T",
    #             "window_start": "2025-01-01T00:00:00Z",
    #             "window_end": "2025-01-01T00:15:00Z",
    #             "event_count": 1,
    #             "unique_users": 1,
    #             "total_amount": 1.0,
    #             "avg_amount_per_event": 1.0,
    #         },
    #         {
    #             "tenant_id": "T",
    #             "window_start": "2025-01-01T00:15:00Z",
    #             "window_end": "2025-01-01T00:30:00Z",
    #             "event_count": 2,
    #             "unique_users": 2,
    #             "total_amount": 5.0,
    #             "avg_amount_per_event": 2.5,
    #         },
    #     ]
    #     tests.append(("boundary_edges", events_boundary, 15,
    #                 expected_boundary))


    #     # ------------------------------------------------------------------
    #     # Execute tests
    #     # ------------------------------------------------------------------
    #     all_passed = True
    #     for name, events, window_minutes, expected in tests:
    #         try:
    #             actual = aggregate_events_by_window(events, window_minutes)
    #         except NotImplementedError as e:
    #             print(f" SKIP: {e}")
    #             all_passed = False
    #             continue
    #         except Exception as e:
    #             print(f" ERROR: {repr(e)}")
    #             all_passed = False
    #             continue
    #         norm_expected = _normalize(expected)
    #         norm_actual = _normalize(actual)
    #         if norm_expected == norm_actual:
    #             print("PASS")
    #         else:
    #             all_passed = False
    #             print("FAIL")
    #             # _print_diff(norm_expected, norm_actual)

    #     # print()
    #     # if all_passed:
    #     #     print("All tests passed ✅ ")
    #     # else:
    #     #     print("Some tests failed ❌ ")


    # if __name__ == "__main__":
    #     run_tests()

    