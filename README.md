Two types of videos for this project, therefore:
* there are two static paths for each of them
* there are two frontend ports for each of them (the ports are used to distinguish database and static file path)
* take these two types into account when designing or developing new features

# Run the project 
```
docker-compose up
```
open http://localhost:9000 and http://localhost:9001 to visit these two websites

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