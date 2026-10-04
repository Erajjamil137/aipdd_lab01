"""Pipeline: wires the four modules together (orchestration layer)."""
from __future__ import annotations

from alert_logger import AlertLogger
from data_ingestion import DataIngestion
from image_preprocessor import ImagePreprocessor
from model_inference_engine import ModelInferenceEngine


class Pipeline:
    """Ingest -> Preprocess -> Infer -> Log/Alert loop."""

    def __init__(self, ingestion: DataIngestion, preprocessor: ImagePreprocessor,
                 engine: ModelInferenceEngine, logger: AlertLogger) -> None:
        self.ingestion = ingestion
        self.preprocessor = preprocessor
        self.engine = engine
        self.logger = logger

    def run(self) -> None:
        """Main loop: for each frame, detect objects, log them and raise alerts."""
        raise NotImplementedError

    def stop(self) -> None:
        """Graceful shutdown of all modules."""
        raise NotImplementedError
