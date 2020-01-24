from manage import db, Video, Cast

listOfNonCastSubPath = ['others', 'unsolved', 'newdata', 'new']
for row in Video.query.all():
  sub_path = row.uri.split('/')
  print(sub_path)
  if len(sub_path) > 2 and sub_path[1] not in listOfNonCastSubPath:
    cast_name = sub_path[1]
    query_cast = Cast.query.filter_by(name=cast_name)
    if query_cast.count() > 0:
      c = query_cast.first()
    else:
      c = Cast(name=cast_name)
    row.cast.append(c)
    db.session.add(row)

db.session.commit()
