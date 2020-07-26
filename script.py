import json
import requests as r
import random as rand

url = "http://127.0.0.1:8000/users/"

phnNumber_list = [
    "+91-855-524-0133",
    "+91-755-566-5622",
    "+91-915-553-6554",
    "+91-925-559-1295",
    "+91-975-556-9307",
    "+91-945-555-7091",
    "+91-925-556-1647",
    "+91-855-517-2022",
    "+91-855-594-9545",
    "+91-855-518-6477",
    "+91-755-577-5479",
    "+91-965-556-4696",
    "+91-855-587-0426",
    "+91-915-550-3173",
    "+91-755-536-9831",
    "+91-945-556-4362",
    "+91-965-559-9564",
    "+91-945-550-7583",
    "+91-995-552-1772",
    "+91-855-550-7056",
    "+91-755-545-5240",
    "+91-755-560-3703",
    "+91-755-586-4595",
    "+91-935-555-5083",
    "+91-755-560-4211",
    "+91-995-551-6917",
    "+91-855-521-4032",
    "+91-755-579-8344",
    "+91-855-540-2224",
    "+91-855-546-8283",
    "+91-985-551-1510",
    "+91-965-550-5365",
    "+91-755-550-9521",
    "+91-855-592-8268",
    "+91-755-502-1947",
    "+91-755-529-6326",
    "+91-755-543-6071",
    "+91-985-555-5804",
    "+91-755-550-9213",
    "+91-855-583-0111",
    "+91-955-552-7210",
    "+91-755-540-6418",
    "+91-915-551-5091",
    "+91-855-527-3416",
    "+91-755-538-5461",
    "+91-755-594-7694",
    "+91-855-521-0465",
    "+91-755-561-7771",
    "+91-925-556-8731",
    "+91-755-513-1664",
    "+91-755-585-5678",
    "+91-855-552-2251",
    "+91-755-531-1553",
    "+91-755-567-9964",
    "+91-955-556-2140",
    "+91-855-554-5265",
    "+91-855-588-1845",
]

name_list = [
    "Zayyan Mcgill",
    "Beth Fleming",
    "Matias Leach",
    "Aaliyah Rowe",
    "Lennie Austin",
    "Yousaf Benitez",
    "Pippa Bannister",
    "Yuvraj Hawkins",
    "Jayden Cartwright",
    "Enrique Greenaway",
]

password_list = [
    "i4qu8rwgho",
    "vinjj1w1c6",
    "1bnhqjj3nt",
    "gn06iey6vw",
    "xlajnlujg7",
    "zacuelqtuf",
    "my4e121e4p",
    "mm277k0m3r",
    "c5rkkfdgic",
    "nufb59a4an",
]

email_list = [
    "qozapafeh-5612@yopmail.com",
    "evujydder-2307@yopmail.com",
    "confaloniero@viocrypot.ml",
    "arandal@sbcglobal.net",
    "hstiles@aol.com",
    "andale@att.net",
    "ntegrity@me.com",
    "uchamp@verizon.net",
    "juerd@icloud.com",
    "nwiger@sbcglobal.net",
]

# for i in range(54):
#     x = r.delete(url)
#     print(x.text)

# phn = rand.choice(phnNumber_list)
# name = rand.choice(name_list)
# password = rand.choice(password_list)
# email = rand.choice(email_list)

# mod = {"phnNumber": phn, "name": name, "password": password, "email": email}

# f = open("C:/Users/Gurpreet/Desktop/data.json", "w")

# for i in range(50):
#     phn = rand.choice(phnNumber_list)
#     name = rand.choice(name_list)
#     password = rand.choice(password_list)
#     email = rand.choice(email_list)

#     mod = {"phnNumber": phn, "name": name, "password": password, "email": email}
#     s = json.dumps(mod)

#     f.write(s)
#     f.write(",")

# f.close()


# x = r.post(url, data=mod)
# z = r.get(url)

# print(z.text)
# print(x.text)
l = [
    {
        "phnNumber": "+91-755-586-4595",
        "name": "Beth Fleming",
        "password": "c5rkkfdgic",
        "email": "confaloniero@viocrypot.ml",
    },
    {
        "phnNumber": "+91-755-502-1947",
        "name": "Pippa Bannister",
        "password": "i4qu8rwgho",
        "email": "juerd@icloud.com",
    },
    {
        "phnNumber": "+91-985-551-1510",
        "name": "Lennie Austin",
        "password": "mm277k0m3r",
        "email": "ntegrity@me.com",
    },
    {
        "phnNumber": "+91-965-559-9564",
        "name": "Pippa Bannister",
        "password": "nufb59a4an",
        "email": "juerd@icloud.com",
    },
    {
        "phnNumber": "+91-755-540-6418",
        "name": "Zayyan Mcgill",
        "password": "zacuelqtuf",
        "email": "juerd@icloud.com",
    },
    {
        "phnNumber": "+91-855-518-6477",
        "name": "Lennie Austin",
        "password": "mm277k0m3r",
        "email": "andale@att.net",
    },
    {
        "phnNumber": "+91-915-550-3173",
        "name": "Matias Leach",
        "password": "my4e121e4p",
        "email": "confaloniero@viocrypot.ml",
    },
    {
        "phnNumber": "+91-755-513-1664",
        "name": "Zayyan Mcgill",
        "password": "1bnhqjj3nt",
        "email": "evujydder-2307@yopmail.com",
    },
    {
        "phnNumber": "+91-855-540-2224",
        "name": "Matias Leach",
        "password": "1bnhqjj3nt",
        "email": "juerd@icloud.com",
    },
    {
        "phnNumber": "+91-755-594-7694",
        "name": "Yousaf Benitez",
        "password": "gn06iey6vw",
        "email": "evujydder-2307@yopmail.com",
    },
    {
        "phnNumber": "+91-915-553-6554",
        "name": "Pippa Bannister",
        "password": "mm277k0m3r",
        "email": "evujydder-2307@yopmail.com",
    },
    {
        "phnNumber": "+91-755-586-4595",
        "name": "Enrique Greenaway",
        "password": "xlajnlujg7",
        "email": "uchamp@verizon.net",
    },
    {
        "phnNumber": "+91-755-579-8344",
        "name": "Matias Leach",
        "password": "1bnhqjj3nt",
        "email": "hstiles@aol.com",
    },
    {
        "phnNumber": "+91-855-592-8268",
        "name": "Lennie Austin",
        "password": "c5rkkfdgic",
        "email": "nwiger@sbcglobal.net",
    },
    {
        "phnNumber": "+91-755-579-8344",
        "name": "Beth Fleming",
        "password": "mm277k0m3r",
        "email": "confaloniero@viocrypot.ml",
    },
    {
        "phnNumber": "+91-985-551-1510",
        "name": "Lennie Austin",
        "password": "1bnhqjj3nt",
        "email": "andale@att.net",
    },
    {
        "phnNumber": "+91-855-552-2251",
        "name": "Pippa Bannister",
        "password": "zacuelqtuf",
        "email": "juerd@icloud.com",
    },
    {
        "phnNumber": "+91-985-555-5804",
        "name": "Beth Fleming",
        "password": "nufb59a4an",
        "email": "nwiger@sbcglobal.net",
    },
    {
        "phnNumber": "+91-975-556-9307",
        "name": "Aaliyah Rowe",
        "password": "xlajnlujg7",
        "email": "uchamp@verizon.net",
    },
    {
        "phnNumber": "+91-755-585-5678",
        "name": "Beth Fleming",
        "password": "zacuelqtuf",
        "email": "qozapafeh-5612@yopmail.com",
    },
    {
        "phnNumber": "+91-925-559-1295",
        "name": "Enrique Greenaway",
        "password": "nufb59a4an",
        "email": "nwiger@sbcglobal.net",
    },
    {
        "phnNumber": "+91-855-583-0111",
        "name": "Zayyan Mcgill",
        "password": "mm277k0m3r",
        "email": "andale@att.net",
    },
    {
        "phnNumber": "+91-755-566-5622",
        "name": "Aaliyah Rowe",
        "password": "gn06iey6vw",
        "email": "qozapafeh-5612@yopmail.com",
    },
    {
        "phnNumber": "+91-855-587-0426",
        "name": "Pippa Bannister",
        "password": "1bnhqjj3nt",
        "email": "confaloniero@viocrypot.ml",
    },
    {
        "phnNumber": "+91-915-553-6554",
        "name": "Pippa Bannister",
        "password": "c5rkkfdgic",
        "email": "qozapafeh-5612@yopmail.com",
    },
    {
        "phnNumber": "+91-855-518-6477",
        "name": "Pippa Bannister",
        "password": "i4qu8rwgho",
        "email": "qozapafeh-5612@yopmail.com",
    },
    {
        "phnNumber": "+91-855-588-1845",
        "name": "Pippa Bannister",
        "password": "gn06iey6vw",
        "email": "nwiger@sbcglobal.net",
    },
    {
        "phnNumber": "+91-855-527-3416",
        "name": "Enrique Greenaway",
        "password": "c5rkkfdgic",
        "email": "qozapafeh-5612@yopmail.com",
    },
    {
        "phnNumber": "+91-975-556-9307",
        "name": "Yousaf Benitez",
        "password": "c5rkkfdgic",
        "email": "nwiger@sbcglobal.net",
    },
    {
        "phnNumber": "+91-975-556-9307",
        "name": "Pippa Bannister",
        "password": "vinjj1w1c6",
        "email": "evujydder-2307@yopmail.com",
    },
    {
        "phnNumber": "+91-945-555-7091",
        "name": "Beth Fleming",
        "password": "mm277k0m3r",
        "email": "andale@att.net",
    },
    {
        "phnNumber": "+91-755-567-9964",
        "name": "Matias Leach",
        "password": "xlajnlujg7",
        "email": "evujydder-2307@yopmail.com",
    },
    {
        "phnNumber": "+91-755-540-6418",
        "name": "Yousaf Benitez",
        "password": "c5rkkfdgic",
        "email": "andale@att.net",
    },
    {
        "phnNumber": "+91-855-554-5265",
        "name": "Jayden Cartwright",
        "password": "mm277k0m3r",
        "email": "qozapafeh-5612@yopmail.com",
    },
]

x = r.post(url, l[0])

print(x.text)
