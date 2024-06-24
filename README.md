To query entries from database:
- User.query.filter_by(id=1)
- User.query.all()

To delete records:
- db.session.delete(User.query.get(1)) // gets user of id=1
Must commit changes to take place: db.session.commit()
