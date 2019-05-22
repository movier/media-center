# Build
`docker build -t my-flask-app .`

# Run
`docker run -it --rm --name my-running-flask-app -p 8003:5000 -v $(pwd):/usr/src/app my-flask-app`

http://localhost:8003/

# Get into command line of the running container
`docker exec -it my-running-flask-app bash`
