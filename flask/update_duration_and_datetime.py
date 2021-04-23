import os, sys, subprocess
from manage import db, Media
from datetime import datetime

base_path = "/mnt/sda4/data/kids"
# base_path = "/mnt/sda4/data/AI"

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
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
  )
  return result.stdout.decode("utf-8").rstrip()

for media in db.session.query(Media).all():
  if os.path.isfile(media.uri):
    duration = get_duration(media.uri)
    media.duration = duration

    creation_datetime = get_datetime(media.uri)
    if creation_datetime:
      media.datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')

    db.session.add(media)

db.session.commit()
