import os, errno

CWD = os.path.normpath(os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir) + os.sep + os.pardir)
os.chdir(CWD)


def create_dir_if_not(path: str):
    """
    Creates a directory recursively if not exist already
    :param path: Full path with multiple sub-folders output/initial-data/collection/
    :return: None
    """
    try:
        os.makedirs(path)
        # print('Directory Created')
    except OSError as e:
        if e.errno != errno.EEXIST:
            print(e)

# create_dir_if_not('output\scrapped-data')
