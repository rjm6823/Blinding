import csv
from os import listdir
from random import sample
from shutil import copyfile


def prepare_names():
    """
    Generate new 
    Return: Dict - Pairs of original file names and new file names
    """
    # Prepare return dict
    final = {}
    
    # Get file names and generate new names
    images = listdir('image_input')
    new_names = sample(range(100,999), len(images))

    # Pair names together
    for counter, image in enumerate(images):
        extension = image.split('.')[-1]
        final[image] = str(new_names[counter]) + '.' + extension

    return final


def create_files(names_dict):
    """
    Performs file copy with new name
    names_dict: Dictionary of original and new file name pairs
    Return: None
    """
    for original, new in names_dict.items():
        copyfile('image_input/' + original, 'image_output/' + new)


def create_csv(names_dict):
    """
    Generate a CSV to keep track of the original and new image file names
    names_dict: Dictionary of original and new file name pairs
    Return: None
    """
    headers = ['Original', 'New']
    with open('output.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for original, new in names_dict.items():
            writer.writerow([original, new])


def main():
    names_dict = prepare_names()
    create_files(names_dict)
    create_csv(names_dict)


if __name__ == "__main__":
    main()
