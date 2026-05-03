import argparse
from pathlib import Path

import cv2

from config import IMAGE_DIR, OUTPUT_DIR, VIDEO_DIR, ensure_project_dirs


def show_project_status() -> None:
    ensure_project_dirs()

    print("OpenCV project is ready.")
    print(f"OpenCV version: {cv2.__version__}")
    print(f"Image folder: {IMAGE_DIR}")
    print(f"Video folder: {VIDEO_DIR}")
    print(f"Output folder: {OUTPUT_DIR}")


def convert_to_gray(input_path: Path, output_path: Path) -> None:
    image = cv2.imread(str(input_path))

    if image is None:
        raise FileNotFoundError(f"Could not read image: {input_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path), gray_image)

    print(f"Saved grayscale image: {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OpenCV project starter")
    parser.add_argument(
        "--image",
        type=Path,
        help="Path to an image file to convert to grayscale.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_DIR / "gray_output.jpg",
        help="Path where the processed image will be saved.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.image:
        convert_to_gray(args.image, args.output)
    else:
        show_project_status()


if __name__ == "__main__":
    main()
