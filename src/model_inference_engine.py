"""ModelInferenceEngine: loads the detector and runs prediction."""
from __future__ import annotations

from typing import List

import numpy as np

from schemas import Detection, PreprocessedFrame


class ModelInferenceEngine:
    """Wraps the AI model (e.g. YOLO) behind a framework-independent API."""

    def __init__(self, model_path: str, device: str = "cpu",
                 conf_threshold: float = 0.5, iou_threshold: float = 0.45,
                 class_names: List[str] | None = None) -> None:
        """
        Args:
            model_path: path to weights (.pt / .onnx).
            device: "cpu", "cuda:0", etc.
            conf_threshold: minimum confidence to keep a detection.
            iou_threshold: IoU threshold used by non-maximum suppression.
            class_names: label list indexed by class_id.
        """
        self.model_path = model_path
        self.device = device
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        self.class_names = class_names or []
        self.model = None

    def load_model(self) -> None:
        """Load weights into memory and warm up the model."""
        raise NotImplementedError

    def predict(self, item: PreprocessedFrame) -> np.ndarray:
        """Run a forward pass. Returns raw predictions, shape (N, 6):
        [x1, y1, x2, y2, confidence, class_id] in model-input coordinates."""
        raise NotImplementedError

    def postprocess(self, raw: np.ndarray, item: PreprocessedFrame) -> List[Detection]:
        """Apply confidence filter + NMS and map boxes back to original pixels."""
        raise NotImplementedError

    def detect(self, item: PreprocessedFrame) -> List[Detection]:
        """Convenience: predict() followed by postprocess()."""
        raise NotImplementedError

    def unload(self) -> None:
        """Free model memory / GPU resources."""
        raise NotImplementedError
