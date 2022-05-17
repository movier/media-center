import subprocess
from os import listdir
from os.path import isfile, join, splitext, getmtime, getsize
from datetime import datetime
from update_duration_and_datetime import get_datetime, get_duration
from manage import db, Media

mypath = "/mnt/sda4/data/kids" # dynamic

def fini(aa, bb = None):
  list = []
  def traverse_dir(base_path, _check_exist_function = None):
    for f in listdir(base_path):
      if _check_exist_function:
        query_existing_video = db.session.query(Media).filter(Media.filename == f).count()
        if query_existing_video > 0:
          continue
      path = join(base_path, f)
      if isfile(path):
        title, ext = splitext(f)
        # if ext == ".mp4" and not f.startswith("._"):
        if not f.startswith("._"):
          title = "".join(title)
          # uri = path[len(mypath):]
          root, ext1 = splitext(path)
          poster_uri = "".join(root) + ".jpg"
                
          # Generate thumbnail if necessary
          if not isfile(poster_uri):
            if ext == ".mp4":
              subprocess.run(
                ["ffmpeg", "-i", path, "-ss", "00:00:01.000", "-vframes", "1", poster_uri],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
              )
                
          mtimestamp = getmtime(path)
          mdatetime = datetime.fromtimestamp(mtimestamp)
          file_size = getsize(path)

          creation_datetime = get_datetime(path)
          
          media_datetime = None
          if creation_datetime:
            media_datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
          else:
            media_datetime = mdatetime
          print('media datetime', media_datetime)

          duration = get_duration(path)

          list.append(dict(
            title=title,
            uri=path,
            poster_uri=poster_uri,
            created_at=mdatetime.isoformat(),
            media_type=1,
            size=file_size,
            datetime=creation_datetime,
            duration=duration,
            filename=f,
          ))

          if _check_exist_function:
            v = Media(
              title=title,
              uri=path,
              poster_uri=poster_uri,
              created_at=mdatetime,
              media_type=1,
              size=file_size,
              datetime=media_datetime,
              duration=duration,
              filename=f,
            )
            db.session.add(v)
        else:
          traverse_dir(path, _check_exist_function)

  traverse_dir(aa, bb)

  if bb:
    db.session.commit()
  
  return list


print(fini(mypath))
