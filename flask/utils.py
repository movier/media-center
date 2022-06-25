import subprocess
from os.path import isfile
# from PIL import Image
# from PIL.ExifTags import TAGS
from exif import Image
import ffmpeg
import sys

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

def generate_thumbnail_for_video(video_uri, screenshot_time, poster_uri):
  if not isfile(video_uri) or isfile(poster_uri):
    return
  subprocess.run(
    ["ffmpeg", "-i", video_uri, "-ss", screenshot_time, "-vframes", "1", poster_uri],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
  )
# generate_thumbnail_for_video('/mnt/sda4/data/AI/IMG_2825.mp4', "5.287213", '/mnt/sda4/data/AI/IMG_2825_7.jpg')

def generate_thumbnail(in_filename, out_filename, time):
  try:
    (
      ffmpeg
      .input(in_filename, ss=time)
      .output(out_filename, vframes=1)
      .overwrite_output()
      .run(capture_stdout=True, capture_stderr=True)
    )
  except ffmpeg.Error as e:
    print(e.stderr.decode(), file=sys.stderr)
    sys.exit(1)
# generate_thumbnail('/mnt/sda4/data/AI/IMG_2825.mp4', '/mnt/sda4/data/AI/IMG_2825_27.jpg', "4.387213")

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

# print(get_image_metadata('/mnt/sda4/data/AI/MIAA-658.jpg'))

def get_image_dimensions(uri):
  metadata = get_image_metadata(uri)
  # print('metadata', metadata)
  image_width = metadata.get('pixel_x_dimension')
  image_height = metadata.get('pixel_y_dimension')
  return { 'width': image_width, 'height': image_height }

# print(get_image_dimensions('/mnt/sda4/data/AI/MIAA-658.jpg'))

def get_video_metadata(uri):
  metadata = {}
  try:
    all_metadata = ffmpeg.probe(uri)["streams"]
    for item in all_metadata:
      for label in item:
        metadata[label] = item.get(label)
  except Exception as inst:
    print(inst)
  return metadata

# print(get_video_metadata('/mnt/sda4/data/AI/IMG_2825.mp4'))

def get_video_dimensions(uri):
  metadata = get_video_metadata(uri)
  video_width = metadata.get('width')
  video_height = metadata.get('height')
  return { 'width': video_width, 'height': video_height }

# print(get_video_dimensions('/mnt/sda4/data/AI/sample4.mp4'))

def get_media_dimensions(uri, media_type):
  if media_type == 1:
    return get_image_dimensions(uri)
  if media_type == 2:
    return get_video_dimensions(uri)
  return None

# print(get_media_dimensions('/mnt/sda4/data/AI/IMG_2826.mp4', 2))
