# Segmentation viewer
A really simple tool to visualize different segmentations on a dataset.
The idea is to sample images and the associated results (for instance: ground truth, alg, alg2).
By clicking inside the window (left click), it will go to the next batch of images. Right click to go to the previous one.

```
usage: viewer.py [-h] --img_source IMG_SOURCE [-n N] [--seed SEED] [--crop CROP] [-C C] [--alpha ALPHA] [--id_regex ID_REGEX] [--display_names [DISPLAY_NAMES [DISPLAY_NAMES ...]]] [--remap REMAP] [--no_contour] [--legend]
                 [--cmap {Blues,BrBG,BuGn,BuPu,CMRmap,GnBu,Greens,Greys,OrRd,Oranges,PRGn,PiYG,PuBu,PuBuGn,PuOr,PuRd,Purples,RdBu,RdGy,RdPu,RdYlBu,RdYlGn,Reds,Spectral,Wistia,YlGn,YlGnBu,YlOrBr,YlOrRd,afmhot,autumn,binary,bone,brg,bwr,cool,coolwarm,copper,cubehelix,flag,gist_earth,gist_gray,gist_heat,gist_ncar,gist_rainbow,gist_stern,gist_yarg,gnuplot,gnuplot2,gray,hot,hsv,jet,nipy_spectral,ocean,pink,prism,rainbow,seismic,spring,summer,terrain,winter,Accent,Dark2,Paired,Pastel1,Pastel2,Set1,Set2,Set3,tab10,tab20,tab20b,tab20c,Blues_r,BrBG_r,BuGn_r,BuPu_r,CMRmap_r,GnBu_r,Greens_r,Greys_r,OrRd_r,Oranges_r,PRGn_r,PiYG_r,PuBu_r,PuBuGn_r,PuOr_r,PuRd_r,Purples_r,RdBu_r,RdGy_r,RdPu_r,RdYlBu_r,RdYlGn_r,Reds_r,Spectral_r,Wistia_r,YlGn_r,YlGnBu_r,YlOrBr_r,YlOrRd_r,afmhot_r,autumn_r,binary_r,bone_r,brg_r,bwr_r,cool_r,coolwarm_r,copper_r,cubehelix_r,flag_r,gist_earth_r,gist_gray_r,gist_heat_r,gist_ncar_r,gist_rainbow_r,gist_stern_r,gist_yarg_r,gnuplot_r,gnuplot2_r,gray_r,hot_r,hsv_r,jet_r,nipy_spectral_r,ocean_r,pink_r,prism_r,rainbow_r,seismic_r,spring_r,summer_r,terrain_r,winter_r,Accent_r,Dark2_r,Paired_r,Pastel1_r,Pastel2_r,Set1_r,Set2_r,Set3_r,tab10_r,tab20_r,tab20b_r,tab20c_r,cityscape}]
                 [folders [folders ...]]

Display the requested data.

positional arguments:
  folders               The folder containing the source segmentations.

optional arguments:
  -h, --help            show this help message and exit
  --img_source IMG_SOURCE
                        The folder containing the images (background).
  -n N                  The number of images to sample per window.
  --seed SEED           The seed for the number generator. Used to sample the images. Useful to reproduce the same outputs between runs.
  --crop CROP           The number of pixels to remove from each border
  -C C                  Number of classes. Useful when not all of them appear on each images.
  --alpha ALPHA
  --id_regex ID_REGEX   The regex to extract the image id from the images names Required to match the images between them.
  --display_names [DISPLAY_NAMES [DISPLAY_NAMES ...]]
                        The display name for the folders in the viewer
  --remap REMAP         Remap some mask values if needed. Useful to suppress some classes.
  --no_contour          Do not draw a contour but a transparent overlap instead.
  --legend              When set, display the legend of the colors at the bottom
  --cmap {Blues,BrBG,BuGn,BuPu,CMRmap,GnBu,Greens,Greys,OrRd,Oranges,PRGn,PiYG,PuBu,PuBuGn,PuOr,PuRd,Purples,RdBu,RdGy,RdPu,RdYlBu,RdYlGn,Reds,Spectral,Wistia,YlGn,YlGnBu,YlOrBr,YlOrRd,afmhot,autumn,binary,bone,brg,bwr,cool,coolwarm,copper,cubehelix,flag,gist_earth,gist_gray,gist_heat,gist_ncar,gist_rainbow,gist_stern,gist_yarg,gnuplot,gnuplot2,gray,hot,hsv,jet,nipy_spectral,ocean,pink,prism,rainbow,seismic,spring,summer,terrain,winter,Accent,Dark2,Paired,Pastel1,Pastel2,Set1,Set2,Set3,tab10,tab20,tab20b,tab20c,Blues_r,BrBG_r,BuGn_r,BuPu_r,CMRmap_r,GnBu_r,Greens_r,Greys_r,OrRd_r,Oranges_r,PRGn_r,PiYG_r,PuBu_r,PuBuGn_r,PuOr_r,PuRd_r,Purples_r,RdBu_r,RdGy_r,RdPu_r,RdYlBu_r,RdYlGn_r,Reds_r,Spectral_r,Wistia_r,YlGn_r,YlGnBu_r,YlOrBr_r,YlOrRd_r,afmhot_r,autumn_r,binary_r,bone_r,brg_r,bwr_r,cool_r,coolwarm_r,copper_r,cubehelix_r,flag_r,gist_earth_r,gist_gray_r,gist_heat_r,gist_ncar_r,gist_rainbow_r,gist_stern_r,gist_yarg_r,gnuplot_r,gnuplot2_r,gray_r,hot_r,hsv_r,jet_r,nipy_spectral_r,ocean_r,pink_r,prism_r,rainbow_r,seismic_r,spring_r,summer_r,terrain_r,winter_r,Accent_r,Dark2_r,Paired_r,Pastel1_r,Pastel2_r,Set1_r,Set2_r,Set3_r,tab10_r,tab20_r,tab20b_r,tab20c_r,cityscape}
```
You can specify the regex in patient_id to regroup the images by id. By default, it will regroup images per name.

By default, it will draw contours of the segmentation, but it can be disabled and draw a transparent mask overlay instead.

The display names are useful to have better columns names, instead of the complete folder name.

It handles of the shelf both multi-class and continuous (probabilities map) as segmentation inputs, but can easily be tweaked for each application.

![example](example.png)

It nows support the colormap argument, including the cityscape colors. For instance:
```shell
python3.8 viewer.py  -n 1 -C 34 --img_source data/gsv_images results/cityscapes/fcn8s_fine/gsv_pred/iter000 results/cityscapes/residualunet/gsv_pred/iter000 results/cityscapes/fcn8s_fine/gsv_pred_crf/iter000 results/cityscapes/residualunet/gsv_pred_crf/iter000 \
	--display_names fcn8s_fine residualunet  fcn8s_fine_crf residualunet_crf --no_contour --cmap cityscape \
	--legend
```
![cityscape](example_cityscape.jpg)

I also added the `--legend` option, to display the discretized colors legend at the bottom of the plot ; this is most useful for results with many different classes, such as Cityscape.

Adding the colormap for PascalVOC for instance would be quite easy.

Things to add:
* Remove all the wasted space around the plots