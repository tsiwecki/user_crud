
from flask import g # Global context
import sqlite3

DATABASE = "user.db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def output_formater(results: None):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["first_name"] = result[1]
        res_dict["last_name"] = result[2]
        res_dict["hobbies"] = result[3]
        res_dict["active"] = result[4]
        out.append(res_dict)
    return out


def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(first_name, last_name, hobbies=None, active=None):
    value_tuple = (first_name, last_name, hobbies, active)
    query = """
            INSERT INFO user (
                first_name,
                last_name,
                hobbies,
                activate
            ) VALUES (?, ?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id

def deactivate_user(user_id):
    cursor = get_db()
    cursor.execute("UPDATE user SET active=0 WHERE id=?", (user_id, ))
    cursor.commit()
    cursor.close()


def select_user(user_id):
    cursor = get_db().execute("SELECT * FROM user WHERE id=?", (user_id, ))  
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results) 

