# HEIC to PNG Conversion and Compression Tool

This tool provides two main functionalities: converting HEIC images to PNG format and compressing large PNG files to smaller sizes using Python on macOS. Below are the instructions to set up your environment and run both conversion and compression scripts.

## Prerequisites

Before running the scripts, ensure you have Homebrew and Python installed on your macOS. This guide will cover the installation of all necessary dependencies with a single command where possible.

### Install Homebrew

Homebrew is a package manager for macOS that simplifies the installation of software. To install Homebrew, open the Terminal and run:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Follow the on-screen instructions to complete the installation.

### Install Python and Dependencies

macOS comes with Python 2.7 pre-installed, but we need Python 3. Additionally, `libheif` is required for handling HEIC files, and Pillow for image processing. You can install these dependencies using Homebrew and pip3 in one command:

brew install python libheif && pip3 install Pillow

This command installs Python 3, `libheif`, and Pillow. `pip3` comes with Python 3 installed via Homebrew.

## Running the Conversion Script

With all dependencies installed, you're now ready to run the conversion script. Place your HEIC images in a directory and run the Python script as follows:

python3 convert.py

## Compressing PNG Files

After converting HEIC images to PNG format, you might want to compress these PNG files to reduce their size. The `compress.py` script resizes large PNG files, ensuring they are under a specified size limit and saves them into a `/compressed` directory. To use the script, ensure it's in the same directory as your PNG files and run:

python3 compress.py

## Troubleshooting

- If you encounter issues with `pyheif` installation or runtime errors, check that `libheif` is up to date and consider using command-line tools like `heif-convert` for conversion tasks.
- Ensure you have read/write permissions for the directory containing the HEIC images, the script, and the `/compressed` directory.

## Upgrading pip

To avoid warnings about pip being out of date, upgrade pip to the latest version by running:

pip3 install --upgrade pip
