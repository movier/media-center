import subprocess
from os.path import isfile
from PIL import Image
from PIL.ExifTags import TAGS

# 0 for unknown, 1 for photo, 2 for video
def get_media_type(filename):
  if filename.lower().endswith(('.jpg', '.jpeg', 'png')):
    return 1
  if filename.lower().endswith(('.mp4', '.mov')):
    return 2
  return 0

def generate_poster_for_video(video):
  if not isfile(video.uri) or isfile(video.poster_uri):
    return
  subprocess.run(
    ["ffmpeg", "-i", video.uri, "-ss", "00:00:01.000", "-vframes", "1", video.poster_uri],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
  )

def get_image_metadata(uri):
  image = Image.open(uri)
  
  # extract other basic metadata
  info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
  }
  
  # for label,value in info_dict.items():
  #   print(f"{label:25}: {value}")

  # extract EXIF data
  exifdata = image.getexif()

  # iterating over all EXIF data fields
  for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    info_dict[tag] = data
  
  return info_dict
