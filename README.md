# Build
docker build -t my-video-app .

# Run
docker run -it --rm --name my-running-app -p 8002:8000 -v $(pwd):/usr/src/app my-video-app

