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

### Deploy FE
After getting into FE container, run `yarn build` to generate new static files and then in production environment, run `git pull` to get the latest code.

# Below is part of the nginx configurations for production mode
```
server {
    listen 9000;

    location / {
        root /mnt/sda4/jffs/my-video-app/react/build;
        try_files $uri $uri/ /index.html;
    }

    location ~ \.(mp4|jpg)$ {
        root /mnt/sda4/data/AI;
    }

    location = /api { rewrite ^ /api/ last; }
    location /api { try_files $uri @my-video-app-api; }
    location @my-video-app-api{
        include fastcgi_params;
        fastcgi_read_timeout 1h;
        fastcgi_split_path_info ^(/api)(.*)$;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param SCRIPT_NAME $fastcgi_script_name;
        fastcgi_pass unix:/tmp/my-video-app-api-fcgi.sock;
    }
}
```
