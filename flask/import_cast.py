from manage import db, Video, Cast

video = Video.query.get(2)
cast = Cast(name='Test2')
video.cast.append(cast)
db.session.add(video)
db.session.commit()

