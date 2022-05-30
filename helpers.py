import sqlite3
import requests

def connect_db(db:sqlite3.Connection): # './userdata/data.db'
    db.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, userid TEXT, empstdid INT, uid INT, usertype INT)')
    db.execute('CREATE TABLE IF NOT EXISTS parents (name TEXT, userid TEXT, empstdid INT, uid INT, usertype INT)')
    db.commit()

def update_db(db:sqlite3.Connection,data:tuple):
    cursor = db.cursor()
    cursor.execute('INSERT INTO students(name, userid, empstdid, uid, usertype) VALUES(?, ?, ?, ?, ?)', data)
    # cursor.execute('DROP TABLE students')
    db.commit()


def update_db_parents(db:sqlite3.Connection,data:tuple):
    cursor = db.cursor()
    cursor.execute('INSERT INTO parents(name, userid, empstdid, uid, usertype) VALUES(?, ?, ?, ?, ?)', data)
    # cursor.execute('DROP TABLE students')
    db.commit()

def get_user_data(userid:str):
    url = "https://www.sscampuscare.in/Logon/UserConfirm"
    data = {"Userid":userid}
    x = requests.post(url, data = data).json()
    try:
        return x["Data"][0][0]
    except:
        return False

def make_data_tuple(data:dict):
    return (data["UserName"], data["UserID"],data["EmployeeIDStudentID"], data["UID"],data["UserTypeID"])

def image_exists(path):
    x = requests.get(path)
    return x.status_code != 404

def download_image(url,name):
    r = requests.get(url)
    if r.status_code != 404:
        with open(f"./userdata/images/{name}.jpg","wb") as file:
            file.write(r.content)
