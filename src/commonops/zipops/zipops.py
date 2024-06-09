import shutil
import zipfile

def zip_folder(source_folder, output_filename):
    """
    Zip target folder and its contents.

    # Example:
        >>> source_folder = '/content/patches64/train'
        >>> output_filename = '/content/patches64/train' # '/train' here will be 'train.zip'
        >>> zip_folder(source_folder, output_filename)  
    """
    shutil.make_archive(output_filename, 'zip', source_folder)


def unzip_folder(zip_filename, extract_folder):
    """
    Unzip target folder to target output folder.

    # Example:
        >>> zip_filename = '/content/metadata.zip'
        >>> extract_folder = '/content/metadata'
        >>> unzip_folder(zip_filename, extract_folder)
    """
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)