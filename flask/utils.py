import subprocess
from os.path import isfile
# from PIL import Image
# from PIL.ExifTags import TAGS
from exif import Image

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

# def get_image_metadata(uri):
#   image = Image.open(uri)
  
#   # extract other basic metadata
#   info_dict = {
#     "Filename": image.filename,
#     "Image Size": image.size,
#     "Image Height": image.height,
#     "Image Width": image.width,
#     "Image Format": image.format,
#     "Image Mode": image.mode,
#     "Image is Animated": getattr(image, "is_animated", False),
#     "Frames in Image": getattr(image, "n_frames", 1)
#   }
  
#   # for label,value in info_dict.items():
#   #   print(f"{label:25}: {value}")

#   # extract EXIF data
#   exifdata = image.getexif()

#   # iterating over all EXIF data fields
#   for tag_id in exifdata:
#     # get the tag name, instead of human unreadable tag id
#     tag = TAGS.get(tag_id, tag_id)
#     data = exifdata.get(tag_id)
#     # decode bytes 
#     if isinstance(data, bytes):
#         data = data.decode()
#     info_dict[tag] = data
  
#   return info_dict

def get_image_metadata(uri):
  with open(uri, 'rb') as img_file:
    img = Image(img_file)
    
  # print(img.has_exif)
  
  # List all EXIF tags contained in the image
  # sorted(img.list_all())

  # print(img.list_all())

  info_dict = {}

  for item in img.list_all():
    try:
      data = img.get(item)
      info_dict[item] = data
      # print(f'{item}: {data}')
    except Exception as inst:
      print(inst)

  # print(info_dict)
  # # Make of device which captured image
  # print(f'Make: {img.get("make")}')

  # # Model of device which captured image
  # print(f'Model: {img.get("model")}')

  # # Software involved in uploading and digitizing image
  # print(f'Software: {img.get("software")}')

  # # Name of photographer who took the image
  # print(f'Artist: {img.get("artist")}')

  # # Original datetime that image was taken (photographed)
  # print(f'DateTime (Original): {img.get("datetime_original")}')

  # # Details of flash function
  # print(f'Flash Details: {img.get("flash")}')
  return info_dict

# get_image_metadata('/mnt/sda4/data/AI/20140904_212615.jpg')