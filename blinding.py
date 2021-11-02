import csv
from os import scandir, path, makedirs, sep
from random import sample
from shutil import copyfile



def check_recursion(dir_path, image_dirs):
    """
    Check for subdirectories and prepare for processing accordingly
    """
    global total_images
    content = scandir(dir_path)
    for item in content:
        if item.is_dir():
            image_dirs.append(path.join(dir_path, item.name))
            check_recursion(path.join(dir_path, item.name), image_dirs)
        else:
            total_images += 1
    if len(image_dirs) == 0:
        return False


def prepare_names(image_dirs):
    """
    Generate new 
    Return: Dict - Pairs of original file names and new file names
    """
    # Prepare return dict
    final = {}
    
    # Get file names and generate new names
    new_names = sample(range(100,9999), total_images)

    # Pair names together
    counter = 0
    for dir in image_dirs:
        images = scandir(dir)
        for item in images:
            if item.is_file():
                extension = item.name.split('.')[-1]
                final[path.join(dir, item.name)] = path.join(dir, str(new_names[counter]) + '.' + extension)
                counter += 1

    return final


def create_files(names_dict):
    """
    Performs file copy with new name
    names_dict: Dictionary of original and new file name pairs
    Return: None
    """
    for original, new in names_dict.items():
        new = new.replace('image_input\\', 'image_output\\')
        copyfile(original, new)


def create_csv(file_name):
    """
    Generate a CSV to keep track of the original and new image file names
    names_dict: Dictionary of original and new file name pairs
    Return: File handle to new outfile
    """
    headers = ['Original', 'New']
    outfile = open(file_name + '.csv', 'w', newline='')
    writer = csv.writer(outfile)
    writer.writerow(headers)
    return outfile


def main():
    # Variable setup
    global total_images
    total_images = 0
    image_dirs = ['image_input']

    # Gather input informaiton
    check_recursion('image_input', image_dirs)

    # Create new output directories as needed
    for dir in image_dirs:
        dir = dir.replace('image_input\\', 'image_output\\')
        makedirs(dir, exist_ok=True)
    
    # Create randomized names
    names_dict = prepare_names(image_dirs)

    # Create copies of the images with randomized names
    create_files(names_dict)

    # Create CSV mappings for each directory
    for dir in image_dirs:
        file_name = '_'.join(dir.split(sep))
        outfile = create_csv(file_name)
        writer = csv.writer(outfile)
        for image in names_dict.keys():
            if path.dirname(image) == path.normpath(dir):
                writer.writerow([path.split(image)[1], path.split(names_dict[image])[1]])


if __name__ == "__main__":
    main()
