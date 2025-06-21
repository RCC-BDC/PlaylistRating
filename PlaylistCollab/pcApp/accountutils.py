from .models import UserAccount
from django.contrib.auth.hashers import make_password
from uuid import uuid4


def createUser(requestData):
    username = requestData.get("username")
    password = requestData.get("password")
    hashed_pass = make_password(password)
    token_val = str(uuid4())

    users = UserAccount.objects.filter(Username=username)
    # ToDO Make better error handling here
    if users.exists():
        return False

    newUser = UserAccount(Username=username, Password=hashed_pass, Token=token_val)
    newUser.save()
    return True
