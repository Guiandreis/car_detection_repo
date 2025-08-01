from pathlib import Path
import yaml
from pydantic import BaseModel, Field


class DetectionThresholds(BaseModel):
    """Confidence and IoU thresholds used during inference."""

    conf: float = Field(0.25, ge=0.0, le=1.0, description="Confidence threshold in the range [0, 1]")
    iou: float = Field(0.45, ge=0.0, le=1.0, description="IoU threshold in the range [0, 1]")


class Settings(BaseModel):
    """Application-wide runtime settings loaded from YAML files."""

    thresholds: DetectionThresholds = DetectionThresholds()  # default if missing in YAML

    @classmethod
    def from_yaml(cls, path: str | Path):
        """Load configuration from a YAML file and validate it using pydantic.

        Args:
            path (str | Path): Path to the YAML file.

        Returns:
            Settings: Settings object.
        """
        path = Path(path)
        with path.expanduser().resolve().open("r", encoding="utf-8") as stream:
            raw = yaml.safe_load(stream) or {}
        return cls.model_validate(raw) 