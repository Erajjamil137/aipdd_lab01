"""ImagePreprocessor: converts raw frames into model-ready tensors."""
from __future__ import annotations

from typing import Tuple

import numpy as np

from schemas import Frame, PreprocessedFrame


class ImagePreprocessor:
    """Resize (letterbox), colour-convert and normalise frames."""

    def __init__(self, input_size: Tuple[int, int] = (640, 640),
                 mean: Tuple[float, float, float] = (0.0, 0.0, 0.0),
                 std: Tuple[float, float, float] = (1.0, 1.0, 1.0)) -> None:
        """
        Args:
            input_size: (width, height) expected by the model.
            mean / std: per-channel normalisation constants (RGB order).
        """
        self.input_size = input_size
        self.mean = mean
        self.std = std

    def resize_letterbox(self, image: np.ndarray) -> Tuple[np.ndarray, float, Tuple[int, int]]:
        """Resize keeping aspect ratio and pad to input_size.

        Returns:
            (resized_image, scale, (pad_x, pad_y))
        """
        raise NotImplementedError

    def normalize(self, image: np.ndarray) -> np.ndarray:
        """BGR->RGB, scale to [0, 1], apply mean/std. Returns float32 HWC array."""
        raise NotImplementedError

    def to_tensor(self, image: np.ndarray) -> np.ndarray:
        """HWC -> NCHW float32 tensor with batch dimension of 1."""
        raise NotImplementedError

    def process(self, frame: Frame) -> PreprocessedFrame:
        """Full pipeline: letterbox -> normalise -> tensor."""
        raise NotImplementedError
