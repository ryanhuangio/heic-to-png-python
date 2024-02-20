# HEIC to PNG Conversion Tool

This tool allows you to convert HEIC images to PNG format using Python on macOS. Below are the instructions to set up your environment and run the conversion script.

## Prerequisites

Before running the script, ensure you have Homebrew and Python installed on your macOS. This guide will cover the installation of all necessary dependencies.

### Install Homebrew

Homebrew is a package manager for macOS that simplifies the installation of software. To install Homebrew, open the Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions to complete the installation.

### Install Python

macOS comes with Python 2.7 pre-installed, but we need Python 3. Install the latest version of Python using Homebrew by running:

```bash
brew install python
```

This command installs Python 3 and `pip3`, the package installer for Python.

### Install libheif

`libheif` is a dependency for handling HEIC files. Install it using Homebrew:

```bash
brew install libheif
```

### Install Pillow

Pillow is the Python Imaging Library (Fork), which supports opening, manipulating, and saving many different image file formats. Install it using `pip3`:

```bash
pip3 install Pillow
```

### Handling pyheif Installation (Optional)

If you need `pyheif` for direct HEIC file manipulation and encounter issues installing it, ensure you have the latest `libheif` installed as described above. Installing `pyheif` can be attempted with:

```bash
pip3 install pyheif
```

However, due to potential compatibility issues, an alternative approach using command-line tools and subprocess in Python is recommended for converting HEIC files.

## Running the Conversion Script

With all dependencies installed, you're now ready to run the conversion script. Place your HEIC images in a directory and run the Python script as follows:

```bash
python3 convert.py
```

## Troubleshooting

- If you encounter issues with `pyheif` installation or runtime errors, check that `libheif` is up to date and consider using command-line tools like `heif-convert` for conversion tasks.
- Ensure you have read/write permissions for the directory containing the HEIC images and the script.

## Upgrading pip

To avoid warnings about pip being out of date, upgrade pip to the latest version by running:

```bash
pip3 install --upgrade pip
```
