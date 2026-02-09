import json
import random
import string
from pathlib import Path
class BankAccount:
    database='db.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.load(fs.read())
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An exception occurred as {err}")
    @staticmethod
    def update():
        with open(BankAccount.database,'w') as fs:
            fs.write(json.dumps(BankAccount.data))
    def createAccount(self):
        data={
            "name":input("Enter your Full Name: "),
            "age": int(input("Enter your age: ")),
            "email":input("Enter your email address: "),
            "pin":input("Enter your pin: "),
            "phone":input("Enter your Phone Number: "),
            "account no.":1234,
            "balance":0
        }
        if data["age"]<18 or len(data["pin"]<4):
            print("Account can't be created.")
        if '@' not in data["email"]:
            print("Please enter a valid email!")
        for i in data:
            print(f"{i}:{data[i]}")
        print("Please note down your account number.")
        BankAccount.data.append(data)