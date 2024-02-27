import nibabel as nib
from nilearn import plotting
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import argparse

def image_dimensions(input_file, plane):
    """ Takes a nifti input file and extracts the x, y and z dimensions then finds the mid-points on the axes
    ----------
    input_file : string
        Absolute or relative path to the nifti you want to analyze.
    """

    # Load the nifti image
    img = nib.load(input_file)

    # Get image data and dimensions
    data = img.get_fdata()
    dim_x, dim_y, dim_z = data.shape
    
    # Calculate mid-slice indices
    mid_x = int(dim_x / 2)
    mid_y = int(dim_y / 2)
    mid_z = int(dim_z / 2)

    # Extract middle slices
    slice_x = data[mid_x, :, :]
    slice_y = data[:, mid_y, :]
    slice_z = data[:, :, mid_z]
    
    # Return our slice x/y/z, nibabel image and input file for further use
    return slice_x, slice_y, slice_z, img, input_file
    
def midslice_saving(input_file, plane):
    """ Takes a nifti input file and extracts the x, y and z dimensions then finds the mid-points on the axes
    ----------
    plane : string
        Absolute or relative path to the nifti you want to analyze.
    """
    
    # Get our three x, y and z objects from the image_dimensions function
    slice_x, slice_y, slice_z, img, input_file = image_dimensions(input_file, plane)
    
    # Set a name for use based on the plane of interest
    if plane == "x":
        chosen_slice = slice_x
    elif plane == "y":
        chosen_slice = slice_y
    elif plane == "z":
        chosen_slice = slice_z
    
    # Save our files as nifti
    nifti_fname = "./middle_" + plane + ".nii.gz"
    nib.save(nib.Nifti1Image(chosen_slice, img.affine), nifti_fname)

    # Save our files as png images for computer vision tasks
    png_fname = "./middle_" + plane + "_image.png"
    plt.imsave(png_fname, chosen_slice, cmap='gray')
    
# Set up our argument parser 
parser = argparse.ArgumentParser()

# Get the input nifti filename and location
parser.add_argument("-input_nifti", help="Path of nifti file to chop up", required=True)

# Get the plane that we want to extract the mid-axis image from
parser.add_argument("-plane_axis", help="x/y/z plane you are interested in", required=True)

# Save our argument values to the args variable
args = parser.parse_args()

# Load in our argument values to variables that our functions use
input_file = args.input_nifti
plane = args.plane_axis

# RUN OUR SCRIPT
midslice_saving(input_file, plane)