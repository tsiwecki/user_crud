
from flask import flask, request
from app.database import (
    scan, insert, 
    deactivate_user
    )

app = Flask(__name__)


@app.routes("/users")
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
        "ok" = True,
        "message" = "Success"
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
            "ok" = True,
            "message" = "Success"
    }
    deactivate_user(uid)
    return out, 200


    