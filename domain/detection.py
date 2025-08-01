from pydantic import BaseModel
from typing import Tuple, Optional


class Detection(BaseModel):
    """Represents a single object detection output."""
    xyxy:  Tuple[int, int, int, int] # x1, y1, x2, y2 format
    confidence: float
    class_id: int
    class_name: Optional[str] = None 