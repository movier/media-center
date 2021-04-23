import os, sys, subprocess
from manage import db, Media
from datetime import datetime

base_path = "/mnt/sda4/data/kids"
# base_path = "/mnt/sda4/data/AI"

def runBash(command):
  try:
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError:
    print('Execution of "%s" failed!\n' % command)
    sys.exit(1)

  # Process output
  for line in output.splitlines():
    print('Line', line)

def get_duration(filename):
  result = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filename],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
  )
  return float(result.stdout)

def get_datetime(filename):
  result = subprocess.run(
    ["ffprobe", "-v", "quiet", "-select_streams", "v:0", "-show_entries", "stream_tags=creation_time", "-of", "default=noprint_wrappers=1:nokey=1", filename],
    # ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_entries", "stream=index,codec_type:stream_tags=creation_time:format_tags=creation_time", filename],
    # ffprobe -v quiet input.mp4 -print_format json -show_entries stream=index,codec_type:stream_tags=creation_time:format_tags=creation_time
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
  )
  return result.stdout.decode("utf-8").rstrip()

for media in db.session.query(Media).all():
  # print(media.uri)
  get_video_info = "ffprobe -v error -show_format " + media.uri
  duration = get_duration(media.uri)
  print(duration)
  media.duration = duration
  datetime1 = get_datetime(media.uri)
  print(datetime1)
  media.datetime = datetime.strptime(datetime1, '%Y-%m-%dT%H:%M:%S.%fZ')
  db.session.add(media)

db.session.commit()
