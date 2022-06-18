import subprocess
from os.path import isfile

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
