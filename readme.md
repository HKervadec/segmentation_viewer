# Segmentation viewer
A really simple tool to visualize different segmentations on a dataset.
The idea is to sample images and the associated results (for instance: ground truth, alg, alg2).

```
usage: viewer [-h] [-n N] --img_source IMG_SOURCE [--seed SEED]
              [--id_regex ID_REGEX]
              [--display_names [DISPLAY_NAMES [DISPLAY_NAMES ...]]]
              [--crop CROP]
              [folders [folders ...]]
```
You can specify the regex in patient_id to regroup the images by id. By default, it will regroup images per name.

The display names are useful to have better columns names, instead of the complete folder name.

It handles of the shelf both multi-class and continuous (probabilities map) as segmentation inputs, but can easily be tweaked for each application.

![example](example.png)

Many things to add:
* Use the button to go to the next batch of images
* Remove all the wasted space around the plots