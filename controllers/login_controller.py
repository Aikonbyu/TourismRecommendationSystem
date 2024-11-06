from controllers import users

def login(username, password):
    id, user = users.get_user_by_name_password(username, password)
    if user:
        return id, True
    else:
        return id, False