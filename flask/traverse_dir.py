import subprocess
from os import listdir
from os.path import isfile, join, splitext, getmtime, getsize
from datetime import datetime
from update_duration_and_datetime import get_datetime, get_duration
from manage import db, Media
from utils import get_media_type, get_image_metadata, get_media_dimensions

def fini(aa, db, bb = None):
  list = []
  def traverse_dir(base_path, db, _check_exist_function = None):
    for f in listdir(base_path):
      if _check_exist_function:
        query_existing_video = db.query(Media).filter(Media.filename == f).count()
        if query_existing_video > 0:
          continue
      path = join(base_path, f)
      if isfile(path):
        title, ext = splitext(f)
        if f.lower().endswith(('.mkv', '.mp4', '.jpg', '.jpeg')) and not f.startswith("._"):
          title = "".join(title)
          # uri = path[len(mypath):]
          root, ext1 = splitext(path)
          poster_uri = "".join(root) + ".jpg"
                
          # An image could be a poster of a video
          if f.lower().endswith(('.jpg', '.jpeg')) and (isfile("".join(root) + ".mp4") or isfile("".join(root) + ".mkv")):
            continue

          # Generate thumbnail if necessary
          if not isfile(poster_uri):
            if ext == ".mp4" or ext == ".mkv":
              subprocess.run(
                ["ffmpeg", "-i", path, "-ss", "00:00:01.000", "-vframes", "1", poster_uri],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
              )
                
          mtimestamp = getmtime(path)
          mdatetime = datetime.fromtimestamp(mtimestamp)
          file_size = getsize(path)

          media_type = get_media_type(f)

          creation_datetime = None
          if media_type == 1:
            meta_data = get_image_metadata(path)
            creation_datetime = meta_data.get('datetime')
          elif media_type == 2:
            creation_datetime = get_datetime(path)
          
          # print('creation datetime', creation_datetime) 
          media_datetime = None
          if creation_datetime:
            if media_type == 1:
              media_datetime = datetime.strptime(creation_datetime, '%Y:%m:%d %H:%M:%S')
            elif media_type == 2:
              media_datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
          else:
            media_datetime = mdatetime

          duration = get_duration(path)

          media_dimensions = get_media_dimensions(path, media_type)
          width = media_dimensions.get('width')
          height = media_dimensions.get('height')
          
          list.append(dict(
            title=title,
            uri=path,
            poster_uri=poster_uri,
            created_at=mdatetime.isoformat(),
            media_type=media_type,
            size=file_size,
            datetime=media_datetime,
            duration=duration,
            filename=f,
            width=width,
            height=height,
          ))

          if _check_exist_function:
            v = Media(
              title=title,
              uri=path,
              poster_uri=poster_uri,
              created_at=mdatetime,
              media_type=media_type,
              size=file_size,
              datetime=media_datetime,
              duration=duration,
              filename=f,
              width=width,
              height=height,
            )
            db.add(v)
      else:
        traverse_dir(path, db, _check_exist_function)

  traverse_dir(aa, db, bb)

  if bb:
    db.commit()
  
  return list
