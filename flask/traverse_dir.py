from os import listdir
from os.path import isfile, join, splitext, getmtime
from datetime import datetime

mypath = "/mnt/sda4/data/kids" # dynamic

def traverse_dir(base_path):
    for f in listdir(base_path):
        path = join(base_path, f)
        if isfile(path):
            title, ext = splitext(f)
            if ext == ".mp4" and not f.startswith("._"):
                title = "".join(title)
                uri = path[len(mypath):]
                root, ext1 = splitext(uri)
                poster_uri = "".join(root) + ".jpg"
                mtimestamp = getmtime(path)
                mdatetime = datetime.fromtimestamp(mtimestamp).isoformat()
                print(dict(title=title, uri=uri, poster_uri=poster_uri, mtime=mdatetime))
        else:
            traverse_dir(path)


traverse_dir(mypath)
