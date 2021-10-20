from app.database import db


def _toJson(elem):
    return {'product_id': elem[0], 'owner_id': elem[1], 'name': elem[2],
            'description': elem[3], 'price': elem[4], 'state': elem[5],
            'image': elem[6], 'category_id': elem[7]}


def getAllProductsOfUserByID(user_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE owner_id = %s"
    values = (user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    toReturn = list()
    for elem in myresult:
        toReturn.append(_toJson(elem))
    return toReturn


def getProductById(product_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s"
    values = (product_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(myresult[0])


def getProductByIds(user_id, product_id):
    mycursor = db.cursor()

    query = "SELECT * FROM Products WHERE product_id = %s and owner_id = %s"
    values = (product_id, user_id,)
    mycursor.execute(query, values)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return 404

    return _toJson(myresult[0])


def addProduct(data):
    mycursor = db.cursor()
    print(data)
    query = "INSERT INTO Products (product_id, owner_id, name, description, price, state, image, category_id) " \
            "VALUES (%s, %s, %s, %s, %f, %i, %s, %i)"
    values = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    mycursor.execute(query, values)
    db.commit()


def deleteProduct(product_id):
    mycursor = db.cursor()
    query = "DELETE FROM Products WHERE product_id = %s"
    mycursor.execute(query)


def updateProduct(product_id, owner_id, data):
    mycursor = db.cursor()
    print(data)
    for item in data:
        if data[item] is not None:
            query = "UPDATE Products SET " + item + " = %s WHERE product_id = %s and owner_id = %s"
            values = (data[item], product_id, owner_id,)
            mycursor.execute(query, values)

    db.commit()
    # myresult = mycursor.fetchall()
    # print(myresult)

"""
import requests
url = 'http://127.0.0.1:5000/user/1/product/1'
myobj = {'price': '299', 'name': 'testing'}
x = requests.put(url, data=myobj)
"""




