import subprocess

def runBash(command):
    try:
        output = subprocess.check_output(command, shell=True,
                                     stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print('Execution of "%s" failed!\n' % command)
        sys.exit(1)

    # Process output
    for line in output.splitlines():
        print('Line', line)

def crop(start,end,input,output):
	str = "ffmpeg -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
	runBash(str)

crop("00:00:00","00:00:04","/mnt/sda4/data/AI/sample.mp4","/mnt/sda4/data/AI/output.mp4")
print('Done!')
