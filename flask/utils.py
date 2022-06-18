# 0 for unknown, 1 for photo, 2 for video
def get_media_type(filename):
  if filename.lower().endswith(('.jpg', '.jpeg', 'png')):
    return 1
  if filename.lower().endswith(('.mp4', '.mov')):
    return 2
  return 0
