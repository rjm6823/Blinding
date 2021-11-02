# Blinding

Blinding is an executable used to randomize file names and create a CSV to match the original file with the new name.

Now with support for nested input directories. Each input directory will create an output directory and they will each have an output CSV.

## Setup - Windows

* Create a folder to contain everything
* Download `blinding.exe` and place it in the folder
* Create `image_input` folder
* Create `image_output` folder

## Usage - Windows

* Put images in the image_input folder
* Double-click blinding.exe to run
* Review the `image_output` folder for the new images
* Review the `output.csv` file for name pairings
* **Note:** Be sure to back up the input/output folders and CSV file elsewhere between runs, otherwise the CSV will be overwritten and the images will be jumbled together

## Setup - Mac

* Install python 3 if it's not already - <https://www.python.org/downloads/>
  * You can run `python --version` OR `python3 --version` from the terminal to check your installed version
* Create a folder to contain everything
* Download `blinding.py` and place it in the folder
* Create `image_input` folder
* Create `image_output` folder
* Make sure the script is executable using `sudo chmod +x blinding.py`

## Usage - Mac

* Put images in the image_input folder
* Use the terminal to run the script - `python blinding.py` OR `python3 blinding.py`
* Review the `image_output` folder for the new images
* Review the `output.csv` file for name pairings
* **Note:** Be sure to back up the input/output folders and CSV file elsewhere between runs, otherwise the CSV will be overwritten and the images will be jumbled together
