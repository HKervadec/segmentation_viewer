#!/usr/bin/env python3.6

import re
import random
import argparse
from math import ceil
from pathlib import Path
from functools import partial
from typing import List, Callable

import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.transform import resize


def extract(pattern: str, string: str) -> str:
    return re.match(pattern, string).group(1)


def display_item(axe, img: np.ndarray, mask: np.ndarray, title=""):
    m = resize(mask, img.shape, mode='constant', preserve_range=True)
    try:
        assert(img.shape == m.shape)
    except AssertionError:
        print(title)
        print(img.shape, m.shape)
        raise

    axe.imshow(img, cmap="gray")
    axe.set_title(title)
    axe.contour(m, cmap='rainbow')


def display(background_names: List[str], segmentation_names: List[List[str]], indexes: List[int]) -> None:
    rn: int = int(ceil(len(indexes) ** .5))

    fig, axes = plt.subplots(nrows=rn, ncols=rn * len(segmentation_names))

    for i, idx in enumerate(indexes):
        img: np.ndarray = imread(background_names[idx])

        for l, names in enumerate(segmentation_names):
            axe_id = len(segmentation_names) * i + l
            axe = axes.flatten()[axe_id]
            seg: np.ndarray = imread(names[idx])
            title: str = "/".join(map(str, Path(names[idx]).parts[-2:]))
            display_item(axe, img, seg, title)

    plt.show()


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Display the requested data.")
    parser.add_argument("-n", type=int, default=9,
                        help="The number of images to sample per window.")
    parser.add_argument("--img_source", type=str, required=True,
                        help="The folder containing the images (background).")
    parser.add_argument("--seed", type=int, default=0,
                        help="The seed for the number generator. Used to sample the images. \
                             Useful to reproduce the same outputs between runs.")
    parser.add_argument("--id_regex", type=str, default=".*/(.*).png",
                        help="The regex to extract the image id from the images names \
                             Required to match the images between them.")
    parser.add_argument("folders", type=str, nargs='*',
                        help="The folder containing the source segmentations.")
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args: argparse.Namespace = get_args()
    random.seed(args.seed)

    img_source: Path = Path(args.img_source)
    background_names: List[str] = sorted(map(str, img_source.glob("*.png")))
    segmentation_names: List[List[str]] = [sorted(map(str, Path(folder).glob("*.png"))) for folder in args.folders]

    extracter: Callable[[str], str] = partial(extract, args.id_regex)
    ids: List[str] = list(map(extracter, background_names))
    for names in segmentation_names:
        assert(ids == list(map(extracter, names)))
        assert(len(background_names) == len(names))
    del ids

    order: List[int] = list(range(len(background_names)))
    while True:
        display(background_names, segmentation_names, random.sample(order, args.n))
