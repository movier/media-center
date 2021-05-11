from manage import db, AndroidRelease

new_android_release = AndroidRelease(version_name='sddads', version_code=6)
db.session.add(new_android_release)
db.session.commit()
