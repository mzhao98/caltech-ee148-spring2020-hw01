import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import linalg as LA
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import json
import os


def plot_annotated_image(img, rl_locations, save_filepath):
    # im = thresh_filtered_image
    im = img
    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)

    # Create a Rectangle patch
    for entry in rl_locations:
        [tl_row, tl_col, br_row, br_col] = entry
        kernel_col_size = br_col-tl_col
        kernel_row_size = br_row - tl_row
        rect = patches.Rectangle((tl_col, tl_row),kernel_col_size,kernel_row_size,linewidth=1,edgecolor='r',facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)

    plt.savefig()



results_filepath = '../CS148/hw01_preds/'
save_filepath = '../CS148/hw01_preds_imgs/'
results_file = 'preds1.json'

with open(results_filepath + results_file) as f:
    results_dict = json.load(f)

if not os.path.exists(save_filepath):
    os.makedirs(save_filepath)

for filename_key in results_dict:
    datapath = '../CS148/RedLights2011_Medium/'
    img = np.array(Image.open(datapath+filename_key))
    rl_locations = results_dict[filename_key]

    # Create figure and axes
    fig,ax = plt.subplots(1)
    # Display the image
    ax.imshow(img)

    # Create a Rectangle patch
    for entry in rl_locations:
        [tl_row, tl_col, br_row, br_col] = entry
        kernel_col_size = br_col-tl_col
        kernel_row_size = br_row - tl_row
        rect = patches.Rectangle((tl_col, tl_row),kernel_col_size,kernel_row_size,linewidth=1,edgecolor='r',facecolor='none')
        # Add the patch to the Axes
        ax.add_patch(rect)

    

    plt.savefig(save_filepath + filename_key)
    plt.close()
    






