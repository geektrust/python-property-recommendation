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
