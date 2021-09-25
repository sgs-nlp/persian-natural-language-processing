import string
import random
import os
import json
from zipfile import ZipFile


def data2zip(data, path, zip_file_name):
    jfile_name = f'{"".join(random.choice(string.ascii_lowercase) for _ in range(16))}.json'
    jfile_path = os.path.join(path, jfile_name)
    zfile_path = os.path.join(path, zip_file_name)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(jfile_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))
    with ZipFile(zfile_path, 'w') as myzip:
        myzip.write(jfile_path, jfile_name)
    os.remove(jfile_path)
    return zfile_path
