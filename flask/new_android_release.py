from manage import db, AndroidRelease

name='test'
code=7
url='ssdd'
new_android_release = AndroidRelease(version_name=name, version_code=code, download_url=url)
db.session.add(new_android_release)
db.session.commit()
