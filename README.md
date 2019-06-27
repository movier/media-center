# Todo
1. test adding video with check parameter
2. static file path should also be dynamic
3. refactor codes related to dynamic database and file path
4. is a way better than referrer to check, such as base prefix of api request

# Run the backend
```
docker-compose up
```
## Access backend container
```
docker exec -it my-running-flask-app bash
```
## Access frontend container
```
docker exec -it my-running-react-app bash
```
# Others
```
server {
    listen 80;
    server_name localhost;

    location / {
        root /mnt/sda4/jffs/my-video-app/frontend/build;
    }
    location = /api { rewrite ^ /api/ last; }
    location /api { try_files $uri @my-video-app-api; }
    location @my-video-app-api{
        include fastcgi_params;
        fastcgi_split_path_info ^(/api)(.*)$;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param SCRIPT_NAME $fastcgi_script_name;
        fastcgi_pass unix:/tmp/my-video-app-api-fcgi.sock;
    }
}
```