# coding=utf-8
from clock_in import auto_clock_in

try:
    f = open("accpwd.cfg", "r")
except:
    print("No such file!")

for line in f.readlines():
    acc_pwd = line.split(",", 1)
    acc_pwd[1] = acc_pwd[1][:-1]
    print(acc_pwd)
    result = auto_clock_in(acc_pwd[0], acc_pwd[1], debug=0, show=0)
    if result ==1:
        print(acc_pwd[0]+":", "Done :)")
    else:
        print(acc_pwd[0]+":", "Failed :(")
f.close()
