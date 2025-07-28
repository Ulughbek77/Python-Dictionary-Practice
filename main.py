def get_full_names(data):
    return [f"{user['name']['first']} {user['name']['last']}" for user in data]
