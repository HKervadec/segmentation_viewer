# Segmentation viewer
A really simple tool to visualize different segmentations on a dataset.
The idea is to sample images and the associated results (for instance: ground truth, alg, alg2).

```
usage: viewer [-h] [-n N] --img_source IMG_SOURCE [--seed SEED]
              [--id_regex ID_REGEX]
              [folders [folders ...]]
```
You can specify the regex in patient_id to regroup the images by id. By default, it will regroup images per name.

It handles of the shelf both multi-class and continuous (probabilities map) as segmentation inputs.

![example](example.png)

Many things to add:
* Better use of the space with matplotlib
* Use the button to go to the next batch of images