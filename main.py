# 1
def get_full_names(data):
    return [f"{user['name']['first']} {user['name']['last']}" for user in data]
# 2
def get_users_by_country(data, country_name):
    return [
        {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "email": user['email']
        }
        for user in data if user['location']['country'] == country_name
    ]
# 3
def count_users_by_gender(data):
    result = {"male": 0, "female": 0}
    for user in data:
        gender = user['gender']
        if gender in result:
            result[gender] += 1
    return result
# 4
def get_emails_of_older_than(data, age):
    return [user['email'] for user in data if user['dob']['age'] > age]
# 5
def sort_users_by_age(data, descending=False):
    sorted_users = sorted(data, key=lambda x: x['dob']['age'], reverse=descending)
    return [
        {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "age": user['dob']['age']
        }
        for user in sorted_users
    ]
# 6
def get_usernames_starting_with(data, letter):
    return [user['login']['username'] for user in data if user['login']['username'].startswith(letter)]

# 7
def get_average_age(data):
    total_age = sum(user['dob']['age'] for user in data)
    return round(total_age / len(data), 2)
# 8
def group_users_by_nationality(data):
    result = {}
    for user in data:
        nat = user['nat']
        result[nat] = result.get(nat, 0) + 1
    return result
# 9
def get_all_coordinates(data):
    return [
        (user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude'])
        for user in data
    ]
# 10
def get_oldest_user(data):
    oldest = max(data, key=lambda x: x['dob']['age'])
    return {
        "name": f"{oldest['name']['first']} {oldest['name']['last']}",
        "age": oldest['dob']['age'],
        "email": oldest['email']
    }
