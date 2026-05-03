from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
IMAGE_DIR = DATA_DIR / "images"
VIDEO_DIR = DATA_DIR / "videos"
OUTPUT_DIR = ROOT_DIR / "outputs"


def ensure_project_dirs() -> None:
    """Create local-only folders used by the project."""
    for path in (DATA_DIR, IMAGE_DIR, VIDEO_DIR, OUTPUT_DIR):
        path.mkdir(parents=True, exist_ok=True)
