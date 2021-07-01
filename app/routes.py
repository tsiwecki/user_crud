
from flask import Flask, request
from app.database import (
    scan, insert, 
    deactivate_user,
    select_user,
    )

app = Flask(__name__)


@app.route("/users")
def get_all_users():
    out = {
        "ok": True,
        "message": "Success"
    }    
    out["body"] = scan()
    return out


@app.route("/users", methods=["POST"])
def create_user():
    out = {
        "ok" : True,
        "message" : "Success"
    }
    user_data = request.json
    out["last_row_id"] = insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        user_data.get("active"),
    )
    return out, 201


@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    out = {
            "ok" : True,
            "message" : "Success"
    }
    deactivate_user(uid)
    return out, 200

@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    #out = {
        #"ok": True,
        #"message": "Success"
    #}
    out["users"] = select_user(uid)
    return render_templete("user_detail.html", data=out)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


    