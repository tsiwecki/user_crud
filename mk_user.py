from app.routes import db, User

def create_my_user(first_name, last_name, hobbies):
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies,
        )
    )
    db.session.commit()


if __name__ == "__main__":
    create_my_user("Thad", "Siwecki", "hunting, fishing")
    create_my_user("John", "Doe", "Playing golf")
    users = User.query.all()
    print("All users:")
    print(users)
    john = User.query.filter_by(first_name="John").first()
    print("Single user:")
    print(john)
