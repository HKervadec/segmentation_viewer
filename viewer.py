#!/usr/bin/env python3.6

import re
import argparse
from math import ceil
from pathlib import Path
from pprint import pprint
from functools import partial
from typing import Callable, List, Tuple

import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from skimage.transform import resize


def extract(pattern: str, string: str) -> str:
    try:
        return re.match(pattern, string).group(1)
    except AttributeError:  # id not found
        return None


def display_item(axe, img: np.ndarray, mask: np.ndarray, title=""):
    m = resize(mask, img.shape, mode='constant', preserve_range=True)
    try:
        assert(img.shape == m.shape)
    except AssertionError:
        # print(title)
        # print(img.shape, m.shape)
        # raise

        # Some grayscale mask are sometimes loaded with 3 channel
        m = m[:, :, 0]

    axe.imshow(img, cmap="gray")
    axe.set_title(title)
    axe.contour(m, cmap='rainbow')
    axe.axis('off')


def display(background_names: List[str], segmentation_names: List[List[str]],
            indexes: List[int], titles: List[List[str]], crop: int) -> None:
    rn: int = int(ceil(len(indexes) ** .5))

    fig, axes = plt.subplots(nrows=rn, ncols=rn * len(segmentation_names))

    for i, idx in enumerate(indexes):
        img: np.ndarray = imread(background_names[idx])
        if crop > 0:
            img = img[crop:-crop, crop:-crop]

        for l, names in enumerate(segmentation_names):
            axe_id = len(segmentation_names) * i + l
            axe = axes.flatten()[axe_id]

            seg: np.ndarray = imread(names[idx])
            if crop > 0:
                seg = seg[crop:-crop, crop:-crop]

            title: str = titles[l][idx]
            display_item(axe, img, seg, title)

    plt.show()


def get_image_lists(img_source: str, folders: List[str], id_regex: str) -> Tuple[List[str], List[List[str]]]:
    path_source: Path = Path(img_source)
    background_names: List[str] = sorted(map(str, path_source.glob("*")))
    segmentation_names: List[List[str]] = [sorted(map(str, Path(folder).glob("*"))) for folder in folders]

    extracter: Callable[[str], str] = partial(extract, id_regex)
    background_names = [bg for bg in background_names if extracter(bg) is not None]
    segmentation_names = [[sn for sn in sl if extracter(sn) is not None] for sl in segmentation_names]

    ids: List[str] = list(map(extracter, background_names))

    for names, folder in zip(segmentation_names, folders):
        try:
            assert(len(background_names) == len(names))
            assert(ids == list(map(extracter, names)))
        except AssertionError:
            print(f"Error verifying content for folder {folder}")
            print(f"Background folder '{img_source}': {len(background_names)} imgs")
            pprint(background_names[:10])
            print(f"Folder '{folder}': {len(names)} imgs")
            pprint(names[:10])

    return background_names, segmentation_names


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
    parser.add_argument("--display_names", type=str, nargs='*',
                        help="The display name for the folders in the viewer")
    parser.add_argument("--crop", type=int, default=0,
                        help="The number of pixels to remove from each border")
    args = parser.parse_args()

    return args


def main() -> None:
    args: argparse.Namespace = get_args()
    np.random.seed(args.seed)

    background_names: List[str]
    segmentation_names: List[List[str]]
    background_names, segmentation_names = get_image_lists(args.img_source, args.folders, args.id_regex)

    if args.display_names is None:
        display_names = [""] * len(args.folders)
    else:
        assert(len(args.display_names) == len(args.folders))
        display_names = args.display_names

    # fn_title: Callable[[str, int], str] = lambda s, _: "/".join(map(str, Path(s).parts[-2:]))
    fn_title: Callable[[str, int], str] = lambda s, i: display_names[i] + " " + re.match(args.id_regex, s).group(1)

    titles = [[fn_title(path, i) for path in l] for i, l in enumerate(segmentation_names)]

    order: List[int] = list(range(len(background_names)))
    order = np.random.permutation(order)
    for a in range(0, len(background_names), args.n):
        idx: List[int] = order[a:a+args.n]
        assert(len(idx == args.n))
        display(background_names, segmentation_names, idx, titles, args.crop)


if __name__ == "__main__":
    main()
