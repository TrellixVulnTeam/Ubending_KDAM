import re
from app.database import db

def getAccountByEmail(email):
    mycursor = db.cursor()

    query = "SELECT * FROM Users WHERE email = %s"
    values = (email,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(list(myresult[0]))

def checkPasswords(password, repeat_password):

    if password != repeat_password:
        return 1
    elif len(password) < 8:
        return 2
    elif re.search('[0-9]',password) is None:
        return 3
    elif re.search('[A-Z]',password) is None:
        return 4

    return 0

def addUserToDB(email, password):
    mycursor = db.cursor()
    username = "User"
    location = "BCN"
    userphoto = 0
    query = "INSERT INTO User (username, password, email, location, userphoto) " \
            "VALUES (%s, %s, %s, %s, %d)"
    values = (username, password, email, location, userphoto)
    mycursor.execute(query, values)
    db.commit()