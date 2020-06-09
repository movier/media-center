import os

def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	str = "ffmpeg -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
	print(str)
	runBash(str)

crop("00:00:00","00:00:04","/mnt/sda4/data/AI/sample.mp4","/mnt/sda4/data/AI/output.mp4")