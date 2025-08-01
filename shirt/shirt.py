# Week 6 File I/O Problem Set 6 P-Shirt shirt.py with muppets.zip and shirt.png imported to shirt CS50 folder

# In a file called shirt.py, implement a program that expects exactly two command-line arguments:

# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the
# input after resizing and cropping the input to be the same size, saving the result as its output.

# Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
# resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
# using default values for method, bleed, and centering, overlay the shirt with Image.paste,
# per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
# and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

# The program should instead exit via sys.exit:

# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.

# Hints
# Note that you can determine a file’s extension with os.path.splitext, per docs.python.org/3/library/os.path.html#os.path.splitext.
# Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
# Note that the Pillow package comes with quite a few classes and methods, per pypi.org/project/Pillow.
# You might find its handbook and reference helpful to skim. You can install the package with:
# pip install Pillow
# You can open an image (e.g., shirt.png) with code like:
# shirt = Image.open("shirt.png")
# You can get the width and height, respectively, of that image as a tuple with code like:
# size = shirt.size
# And you can overlay that image on top of another (e.g., photo) with code like
# photo.paste(shirt, shirt)
# wherein the first shirt represents the image to overlay and the second shirt represents a “mask” indicating which pixels in photo to update.
# Note that you can open an image (e.g., shirt.png) in VS Code by running
# code shirt.png
# or by double-clicking its icon in VS Code’s file explorer.

# How to Test
# Here’s how to test your code manually:
# Run your program with python shirt.py. Your program should exit using sys.exit and provide an error message:
# Too few command-line arguments
# Be sure to download muppets.zip and extract a collection of muppet photos using unzip muppets.zip.
# Run your program with python shirt.py before1.jpg before2.jpg before3.jpg. Your program should output:
# Too many command-line arguments
# Run your program with python shirt.py before1.jpg invalid_format.bmp.
# Your program should exit using sys.exit and provide an error message:
# Invalid output
# Run your program with python shirt.py before1.jpg after1.png.
# Your program should exit using sys.exit and provide an error message:
# Input and output have different extensions
# Run your program with python shirt.py non_existent_image.jpg after1.jpg.
# Your program should exit using sys.exit and provide an error message:
# Input does not exist
# Run your program with python shirt.py before1.jpg after1.jpg.

import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    # Check command line arguments
    check_command_line_arg()
    # Open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open shirt
    shirtfile = Image.open("shirt.png")
    # Get the size of the shirt
    size = shirtfile.size
    # Resize muppet image to fit the shirt
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt in muppet image
    muppet.paste(shirtfile, shirtfile)
    # Create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    # Check how many elements are in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    # Check if it is an Image file
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    # Check if extension of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False



if __name__ == "__main__":
    main()
