# Email validation by RegEx
""" ? for onw time enter value
    ^ for range 
    \ for search
    $ for search from last
"""
import re
email_con="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"   # main condition
user_email = input('Enter your email : ->')
if re.search(email_con,user_email):
    print("Your have right email")
else:
    print("Wrong email")
