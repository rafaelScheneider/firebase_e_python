import firebase_admin
from firebase_admin import db
import json

cred_obj = firebase_admin.credentials.Certificate('jsonkey.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://pythonlearning-ad521-default-rtdb.firebaseio.com/'})

refchng = db.reference('/')

with open("informacao.json", "r") as arquivo:
    file_contents = json.load(arquivo)
refchng.set(file_contents)

refget = db.reference("/")
print(refget.get())
