"""Shared data structures passed between pipeline modules."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import numpy as np


@dataclass
class Frame:
    """A single decoded video frame."""
    image: np.ndarray            # BGR image, shape (H, W, 3), dtype uint8
    timestamp: datetime          # capture time
    camera_id: str               # source camera identifier
    frame_id: int                # monotonically increasing counter


@dataclass
class PreprocessedFrame:
    """Model-ready tensor plus the metadata needed to map results back."""
    tensor: np.ndarray           # float32, shape (1, 3, H_in, W_in), values in [0, 1]
    original_shape: Tuple[int, int]   # (H, W) of the source frame
    scale: float                 # resize ratio used (letterbox)
    pad: Tuple[int, int]         # (pad_x, pad_y) added by letterbox
    source: Frame


@dataclass
class Detection:
    """One detected object in original-frame pixel coordinates."""
    bbox: Tuple[float, float, float, float]   # (x1, y1, x2, y2)
    confidence: float
    class_id: int
    class_name: str
    identity: Optional[str] = None            # recognised person ID, if any


@dataclass
class Alert:
    """An event that must be pushed to operators."""
    alert_type: str              # e.g. "UNKNOWN_FACE", "RESTRICTED_ZONE"
    severity: str                # "INFO" | "WARNING" | "CRITICAL"
    message: str
    camera_id: str
    timestamp: datetime
    detections: List[Detection] = field(default_factory=list)
    metadata: Dict[str, str] = field(default_factory=dict)
