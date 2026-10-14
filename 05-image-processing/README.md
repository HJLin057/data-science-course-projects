# Image Processing: Blur, Colour Segmentation and Retinal Vessels

Two notebooks with classic image processing in scikit-image and SciPy.

## 1. Gaussian blur and colour segmentation (`1_blur_and_segmentation.ipynb`)

- **Spatial vs. frequency domain:** times a Gaussian blur for sigma 1 to 64, averaged over 10 runs. The spatial
  blur gets slower as sigma grows, from 0.009 to 0.19 seconds; the frequency-domain blur takes about 0.04 seconds
  for every sigma and is faster from sigma 16 on. Both give the same blurred image.
- **Segmentation:** separates a teddy bear, its shirt and its ribbon with three HSV colour ranges, combines them
  and cleans the mask with closing, hole filling, small-object removal and opening.
- **Measurements:** bounding box of the head, and area and centre of each eye from region properties.
  The eyes measure 577 and 632 pixels.

## 2. Retinal vessel segmentation (`2_retinal_vessels.ipynb`)

- **Segmentation:** blood vessels in a colour fundus image are found by thresholding the hue channel
  (0.022, close to Otsu's 0.0215), removing small objects and closing gaps.
  **Dice score 0.77** against a manual annotation.
- **Centreline:** on the manual annotation, vessels narrower than 8 pixels are removed with an opening and the
  rest is thinned to a 1-pixel centreline of **6,198 pixels**.
- **Orientation:** the direction of the centreline at each pixel, from Sobel gradients, shown in a rose plot.

## Files

- `1_blur_and_segmentation.ipynb`, `2_retinal_vessels.ipynb`: the notebooks with their outputs

## Run

```bash
pip install -r requirements.txt
```

The images are not included in this repository.

Some parts started from code suggested by ChatGPT and were then adjusted by hand: the starting HSV ranges for
the teddy bear, the kernel handling in the frequency-domain blur, the Dice score and the rose plot.
