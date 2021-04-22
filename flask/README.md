After installing new dependency through `pip3 install`, run `pip3 freeze > requirements.txt` to export dependencies

# Get into command line of the running container
```
docker exec -it my-running-flask-app bash
```

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

# Backend update in production environment
1. if use `screen`
```
screen -list
screen -r [session]
ctrl + c
/mnt/sda4/jffs/my-video-app/flask/my-video-app-api.fcgi
ctrl a + d
```

2. else 
```
ps | grep python
kill pid
screen
/mnt/sda4/jffs/my-video-app/flask/my-video-app-api.fcgi
ctrl a + d
```

# Data Migration
0.(Important) Back up db. Nothing is more important

1.Update `manage.py` and related files

2.Generate a migration script
```
python manage.py db migrate
```

3.Update the script if necessary, make sure both the upgrade method and downgrade method work well. Then do the upgrade migration twice connecting to different db.
```
python manage.py db upgrade
python manage.py db downgrade
```

4.(Optional) Sometimes we also need to manipulate data. Usually I will write a Python script to do so. This also needs to be done twice by changing the db and base path.

# Troubleshooting
1. If you got a 404 and find permission denied in error log, please make sure that the user of nginx and that of the fcgi file should be the same.