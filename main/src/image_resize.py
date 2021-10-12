import os
from glob2 import glob
from docs import config
import cv2


def main():
    image_files = glob(os.path.join(config.ASSETS_ALIGNMENT_CT_DIR, "*.jpg"), recursive=True)
    image_files = sorted(image_files)

    for image_file in image_files:
        image = cv2.imread(image_file)
        image = cv2.resize(image, (1000, 570), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(config.ASSETS_ALIGNMENT_CT_RESIZE_DIR, os.path.basename(image_file)), image)


if __name__ == '__main__':
    main()
