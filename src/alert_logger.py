"""AlertLogger: persists detections and dispatches alerts."""
from __future__ import annotations

from typing import List, Optional

from schemas import Alert, Detection, Frame


class AlertLogger:
    """Writes log entries to the database and raises operator alerts."""

    def __init__(self, db_path: str = "logs/events.db",
                 notify_channels: List[str] | None = None,
                 dedup_window_s: int = 600) -> None:
        """
        Args:
            db_path: SQLite / DB connection string for the event log.
            notify_channels: e.g. ["email", "sms", "dashboard"].
            dedup_window_s: ignore identical alerts inside this window (seconds).
        """
        self.db_path = db_path
        self.notify_channels = notify_channels or ["dashboard"]
        self.dedup_window_s = dedup_window_s

    def log_detections(self, frame: Frame, detections: List[Detection]) -> int:
        """Store detections for a frame. Returns number of rows written."""
        raise NotImplementedError

    def evaluate_rules(self, frame: Frame, detections: List[Detection]) -> List[Alert]:
        """Apply alert rules (unknown face, restricted zone, ...) and return alerts."""
        raise NotImplementedError

    def send_alert(self, alert: Alert) -> bool:
        """Dispatch an alert to all channels. Returns True if delivered."""
        raise NotImplementedError

    def log_attendance(self, person_id: str, camera_id: str, timestamp) -> bool:
        """Record attendance once per dedup window. Returns True if a new row was added."""
        raise NotImplementedError

    def sync_to_server(self) -> int:
        """Push unsynced rows to the central DB. Returns rows synced."""
        raise NotImplementedError

    def get_recent(self, limit: int = 50) -> List[dict]:
        """Fetch the most recent log entries for the dashboard."""
        raise NotImplementedError
