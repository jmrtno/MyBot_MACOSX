
import time

def comments():
    with open ('/Users/javiermartin/Desktop/mibot/comments.txt', encoding='utf8') as r:
        comment = r.readlines()
        return(list(map(str.strip, comment)))
comment = comments()

def read_account():
    with open ('/Users/javiermartin/Desktop/mibot/account_password.txt', encoding = 'utf-8') as a:
        acc = a.readlines()
        return (list(map(str.strip, acc[0])))
acc = read_account()

def read_password():
    with open ('/Users/javiermartin/Desktop/mibot/account_password.txt', encoding = 'utf-8') as p:
        passw = p.readlines()
        return (list(map(str.strip, passw[1])))
passw = read_password()

def send_delayed_user(username, text, delay=1):
    for u in text:
        endtime = time.time() + delay
        username.send_keys(u)
        time.sleep(endtime-time.time())

def send_delayed_password(password, text, delay=1):
    for p in text:
        endtime = time.time() + delay
        password.send_keys(p)
        time.sleep(endtime-time.time())