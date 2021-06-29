import requests

test user = {
    "first-Nmae": "John",
    "last_name": "Doe",
    "hobbies": "Skiing",
    "active": 1

}

def test_user_creation():
    out = requests.post("http:127.0.0.1:5000/users", json=TEST_user)
    if out.status_code == "201":
        print(out.json())
    else:
        print("Something went wrong.")

def test_user_deactivate():
    out = requests.delete("http://127.0.0.1:5000/users/2")
    if out.ststus_code == 200:
        print(out.json())
    else:
        print("Something is wrong with delete.")

if __name__ == "__main__":
    test_user_creation()