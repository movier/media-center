FROM python:3.8

RUN apt update
RUN apt install -y ffmpeg

WORKDIR /mnt/sda4/jffs/my-video-app/flask

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD FLASK_APP=hello.py FLASK_ENV=development flask run --host=0.0.0.0
