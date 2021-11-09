from os import listdir
from os.path import isfile, join, splitext, getmtime, getsize
from datetime import datetime
from update_duration_and_datetime import get_datetime, get_duration

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
                file_size = getsize(path)

                creation_datetime = get_datetime(path)
                media_datetime = None
                if creation_datetime:
                    media_datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')

                duration = get_duration(path)

                print(dict(
                    title=title,
                    uri=uri,
                    poster_uri=poster_uri,
                    created_at=mdatetime,
                    media_type=1,
                    size=file_size,
                    datetime=creation_datetime,
                    duration=duration,
                    filename=f,
                ))
        else:
            traverse_dir(path)


traverse_dir(mypath)
