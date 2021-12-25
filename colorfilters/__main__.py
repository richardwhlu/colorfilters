from . import *
import cv2 as cv
import argparse

choices = {
    "bgr": BGRFilter,
    "hsv": HSVFilter,
    "hls": HLSFilter,
    "lab": LabFilter,
    "luv": LuvFilter,
    "ycc": YCrCbFilter,
    "xyz": XYZFilter,
    "gray": GrayscaleFilter,
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "test color thresholding of images in different colorspaces"
    )
    parser.add_argument("image", help="path to image")
    parser.add_argument(
        "colorspace", choices=list(choices.keys()), help="colorspace to filter in"
    )
    parser.add_argument(
        "resize_factor_w", help="factor to resize width"
    )
    parser.add_argument(
        "resize_factor_h", help="factor to resize height"
    )
    args = parser.parse_args()

    img = cv.imread(args.image)
    img = cv.resize(img, (int(img.shape[0] / args.resize_factor_w), int(img.shape[1] / args.resize_factor_h)))
    if img is None or img.size == 0:
        raise Exception(f"Unable to read image {args.image}. Please check the path.")
    window = choices[args.colorspace](img)

    window.show()
    cv.destroyAllWindows()
