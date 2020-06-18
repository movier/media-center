import os
from datetime import datetime

def runBash(command):
	os.system(command)

def crop(start, end, input, output):
	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
	duration = str(tdelta)
	str1 = "ffmpeg -ss " + start + " -i " + input + " -t " + duration + " -vcodec copy -acodec copy " + output
	print(str1)
	runBash(str1)

crop("00:00:02","00:00:06","/mnt/sda4/data/AI/sample.mp4","/mnt/sda4/data/AI/output.mp4")
