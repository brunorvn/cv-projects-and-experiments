import os
import argparse
from PIL import Image


def resize_images(input_folder: str, output_folder: str, size: tuple = (200, 110)) -> None:
    """
    Resize all images in the input folder and save them to the output folder.

    Parameters:
        input_folder (str): Path to the folder containing images to resize.
        output_folder (str): Path to the folder where resized images will be saved.
        size (tuple): The target size for resizing (width, height). Default is (200, 110).
    """
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as image:
                resized_image = image.resize(size, resample=Image.Resampling.LANCZOS)
                resized_image.save(output_path)


def main() -> None:
    """Parse command-line arguments and resize images based on user input."""

    parser = argparse.ArgumentParser(description="Resize all images in a folder.")
    parser.add_argument(
        "input_folder",
        type=str,
        help="Path to the input folder containing images to resize.",
    )
    parser.add_argument(
        "--size",
        type=int,
        nargs=2,
        metavar=("width", "height"),
        default=(200, 110),
        help="Target size for resizing images (default: 200x110).",
    )

    args = parser.parse_args()

    output_folder = os.path.join(
        os.path.dirname(os.path.abspath(args.input_folder)), "resized"
    )

    resize_images(args.input_folder, output_folder, size=tuple(args.size))


if __name__ == "__main__":
    main()
