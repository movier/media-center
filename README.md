# Build
`docker build -t my-video-app .`

# Run
`docker run -it --rm --name my-running-app -p 8002:8000 -v $(pwd):/usr/src/app my-video-app`

http://localhost:8002/

# Get into command line of the running container
`docker exec -it my-running-app bash`
