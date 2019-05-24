# Build
`docker build -t my-flask-app .`

# Run
`docker run -it --rm --name my-running-flask-app -p 8003:5000 -v $(pwd):/usr/src/app my-flask-app`

http://localhost:8003/

# Get into command line of the running container
`docker exec -it my-running-flask-app bash`

# Server Configuration

1. Install dependencies
```
pip3 install --no-cache-dir -r requirements.txt
```

Check the path of python3

2. Add executable permission to the file below
```
chmod +x /mnt/sda4/jffs/my-video-app/flask/my-video-app-api.fcgi
```

3. Configure Nginx
```
 location = /api { rewrite ^ /api/ last; }
    location /api { try_files $uri @my-video-app-api; }
    location @my-video-app-api{
        include fastcgi_params;
        fastcgi_split_path_info ^(/api)(.*)$;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param SCRIPT_NAME $fastcgi_script_name;
        fastcgi_pass unix:/tmp/my-video-app-api-fcgi.sock;
    }
```

4. Running FastCGI Process
```
/mnt/sda4/jffs/my-video-app/flask/my-video-app-api.fcgi &
```

# Troubleshooting
1. If you got a 404 and find permission denied in error log, please make sure that the user of nginx and that of the fcgi file should be the same.