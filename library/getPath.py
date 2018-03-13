import os


def root_path():
    root_paths = os.path.dirname(os.path.abspath(__file__))
    while root_paths:
        if os.path.exists(os.path.join(root_paths, 'README.MD')):
            break
        root_paths = root_paths[0:root_paths.rfind(os.path.sep)]
    return root_paths


def data_path(filename):
    root_paths = root_path()
    data_paths = os.path.join(root_paths, 'data', filename)
    return data_paths







