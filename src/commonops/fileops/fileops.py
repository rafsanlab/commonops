import os
from natsort import natsorted

def collect_same_file_from_subdir(projectdir, subsubdir=None, fname='', filter_subdir_names=[]):
    """ Collect file paths from subdir of parentdir if all files are the same name.
        Provide subsubdir if the file is in dir in the subdir.
        Returns dict containing the subdir (key) and filepath (value).
    """
    filepaths = {}
    # get all the data from subdir
    for subdir in os.listdir(projectdir):
        if os.path.isdir(os.path.join(projectdir, subdir)): # avoid files, just folders
            if subsubdir is not None: # a subdir of subdir
                filepath = os.path.join(subdir, subsubdir, fname)
            else:
                filepath = os.path.join(subdir, fname)
            filepath = os.path.join(projectdir, filepath)
            if os.path.exists(filepath): # check is exist
                filepaths[subdir] = filepath
    # filter subdir name based on filter_subdir_name list
    if filter_subdir_names is not None:
        if len(filter_subdir_names)>0 :
            filtered_filepaths = {}
            for k, v in filepaths.items():
                if all(name in k for name in filter_subdir_names):
                    filtered_filepaths[k] = v
            filepaths = filtered_filepaths
    # natural sort the keys
    filepaths = {k: filepaths[k] for k in natsorted(filepaths)}
    return filepaths