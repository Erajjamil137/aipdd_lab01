"""DataIngestion: connects to camera sources and yields decoded frames."""
from __future__ import annotations

from typing import Iterator, Optional

from schemas import Frame


class DataIngestion:
    """Reads frames from an RTSP stream, video file or webcam.

    Responsibilities:
        * open/close the video source and auto-reconnect on stream loss
        * decode frames and attach timestamp / camera_id / frame_id
        * enforce a target FPS by dropping stale frames (never block the pipeline)
    """

    def __init__(self, source_uri: str, camera_id: str, target_fps: int = 15,
                 reconnect_attempts: int = 5) -> None:
        """
        Args:
            source_uri: RTSP URL, file path or device index (as string).
            camera_id: unique ID stored with every frame.
            target_fps: maximum frames per second delivered downstream.
            reconnect_attempts: retries before raising ConnectionError.
        """
        self.source_uri = source_uri
        self.camera_id = camera_id
        self.target_fps = target_fps
        self.reconnect_attempts = reconnect_attempts

    def open(self) -> bool:
        """Open the video source. Returns True on success."""
        raise NotImplementedError

    def read_frame(self) -> Optional[Frame]:
        """Return the next Frame, or None if the stream ended / read failed."""
        raise NotImplementedError

    def frames(self) -> Iterator[Frame]:
        """Generator that yields frames until the source is closed."""
        raise NotImplementedError

    def reconnect(self) -> bool:
        """Try to re-open a dropped stream. Returns True if recovered."""
        raise NotImplementedError

    def is_opened(self) -> bool:
        """True while the underlying capture is open."""
        raise NotImplementedError

    def release(self) -> None:
        """Release the capture handle and free resources."""
        raise NotImplementedError
