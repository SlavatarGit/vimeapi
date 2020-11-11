import requests, logging


# Vars
DEV_TOKEN = None
DEV_API   = "https://api.vimeworld.ru/"


# Functions
def check_data_on_error(data):
    try:
        if data["error"]["error_code"]:
            logging.error(f"Request have error: {data['error']['error_code']} - {data['error']['error_msg']}")
            return False
    except:

        logging.info("Request dont have errors")
        return True

def check_token(token, type="AUTH"):
    data = requests.get(f"{DEV_API}misc/token/{token}?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        if data["valid"]:
            if data["type"] == type.upper:
                logging.debug(f"Valid token: {token}:{type}")
                return data

        logging.error(f"Invalid token, : {token}:{type}")
        return None

def achievements():
    data = requests.get(f"{DEV_API}misc/achievements?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def maps():
    data = requests.get(f"{DEV_API}misc/maps?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def games():
    data = requests.get(f"{DEV_API}misc/maps?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def locale(lang="ru"):
    data = requests.get(f"{DEV_API}locale/{lang}?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def match_list(before=0, after=1, count=5):
    if before:
        request = "before=" + str(before)
    else:
        request = "after=" + str(after)

    data = requests.get(f"{DEV_API}match/list?{request}&count={count}&token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def match_latest():
    data = requests.get(f"{DEV_API}match/latest?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def match(id=246473141751119872):
    data = requests.get(f"{DEV_API}match/{id}?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def online_staff():
    data = requests.get(f"{DEV_API}online/staff?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def online_streams():
    data = requests.get(f"{DEV_API}online/streams?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def online():
    data = requests.get(f"{DEV_API}online?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def leaderboard(type="user", sort="lvl", size=100, offset=0):
    data = requests.get(f"{DEV_API}leaderboard/get/{type}/{sort}?size={size}&offset={offset}&token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def leaderboard_list():
    data = requests.get(f"{DEV_API}leaderboard/list?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def guild(id=None, name=None, tag=None):
    request = "id=1"
    if id != None:
        request = "id=" +str(id)
    elif name != None:
        request = "name=" +str(name)
    elif tag != None:
        request = "tag=" +str(tag)

    data = requests.get(f"{DEV_API}match/list?{request}&token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def guild_search(what):
    data = requests.get(f"{DEV_API}guild/search?query={what}&token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_sessions(ids = [1, 2, 3, 4, 5]):
    data = requests.post(f"{DEV_API}user/session?token={DEV_TOKEN}", json=ids).json()

    if check_data_on_error(data):
        return data

def user_matches(user=1):
    data = requests.get(f"{DEV_API}user/{user}/matches?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_leaderboards(user=1):
    data = requests.get(f"{DEV_API}user/{user}/leaderboards?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_achievements(user=1):
    data = requests.get(f"{DEV_API}user/{user}/achievements?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_session(user=1):
    data = requests.get(f"{DEV_API}user/{user}/session?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_friends(user=1):
    data = requests.get(f"{DEV_API}user/{user}/friends?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user(user=1):
    if isinstance(user, int):
        data = requests.get(f"{DEV_API}user/{user}?token={DEV_TOKEN}").json()
    else:
        request = ""
        for u in user:
            request += str(u) + ","

        data = requests.get(f"{DEV_API}user/{request}?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def user_name(user="xtrafrancyz"):
    data = requests.get(f"{DEV_API}user/name/{user}?token={DEV_TOKEN}").json()

    if check_data_on_error(data):
        return data

def request_limit():
    data = requests.get(f"{DEV_API}online?token={DEV_TOKEN}").headers
    return {"X-RateLimit-Limit":       data["X-RateLimit-Limit"],
            "X-RateLimit-Remaining":   data["X-RateLimit-Remaining"],
            "X-RateLimit-Reset-After": data["X-RateLimit-Reset-After"]}
