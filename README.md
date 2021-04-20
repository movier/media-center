# Background, Updated on 2021-04-19
我想基于目前的 my-video-app 结合和我之前想要开发的 Moment，打造一个家庭多媒体中心。

The router will work as the server. All the images and videos will be stored on it.

当家里的终端设备链接到家庭 Wi-Fi 后，自动上传手机相册到路由器上，这样一方面把手机相册都备份了，另一方面也方便我统一管理。

Two types of videos for this project, therefore:
* there are two static paths for each of them
* there are two frontend ports for each of them (the ports are used to distinguish database and static file path)
* take these two types into account when designing or developing new features
* Data migration needs to be done twice

# 生产环境的 Nginx 配置
为了腾出路由器的空间，一些文件被移动到了移动硬盘里，只需要修改 Nginx 的配置：
```
location ~ ^/newdata/.+\.(mp4|jpg)$ {        # 当请求的是以 /newdata/ 开头的 mp4 或者 jpg 文件时
    root /mnt/TOSHIBA;                       # 到移动硬盘里去寻找相关文件
}
```
Nginx 实在是太帅了

# Features
* Media List Page
* Check Updates to see if there are any untracked media
* Media Details Page
  * Add people
  * Delete media
* People List Page

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

    location ~ ^/newdata/.+\.(mp4|jpg)$ {
        root /mnt/TOSHIBA;
    }

    location ~ ^/JULIA/.+\.(mp4|jpg)$ {
        root /mnt/TOSHIBA;
    }

    location ~ ^/霧島さくら/.+\.(mp4|jpg)$ {
        root /mnt/TOSHIBA;
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
