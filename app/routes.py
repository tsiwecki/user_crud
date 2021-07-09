
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)
from app.database import User


@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/users/<int:uid>")
def get_user(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("user_detail.html", user=user)

@app.route("/users/<int:uid>")
def delete_user(uid):
    query = "DELETE FROM db WHERE id=?"
    cursor = get_user(uid)
    cursor.execute(query, (uid, ))
    cursor.commit()
    return True

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404