import hashlib
import binascii
import json


veprimi = input("Cfare veprimi do te kryesh 1(futje te nje pass te ri) 2(nxjerrje te nje  paswordi) 3(pass i vertet) : ")

if int(veprimi) == 1:
    app = input("Jep aplikacionin qe do futesh: ")
    email = input("Ju lutem fusni email qe do perdorni: ")
    fjalkalimi = input("Ju lutem fusni fjalkalimin tua: ")

    dk = hashlib.pbkdf2_hmac('sha256', fjalkalimi.encode(), b's', 100000)
    paswordi_enkoduar = binascii.hexlify(dk)
    paswordi_coptuar = str(paswordi_enkoduar).split("'")

    def write_json(data):
        with open('lista.json', 'w') as f:
            json.dump(data, f, indent=4)

    with open('lista.json') as json_file:
        data = json.load(json_file)
        temp = data['em-details']
        y = {"Aplikacioni": app,
             "Email": email,
             "Password": paswordi_coptuar[1]
             }
        # appending data to emp_details
        temp.append(y)
    write_json(data)

    def write_json2(data2):
        with open('pas2.json', 'w') as j:
            json.dump(data2, j, indent=4)

    with open('pas2.json') as file:
        data2 = json.load(file)
        temp2 = data2['Pasword-details']
        t = {"Aplikacioni": app,
             "email":email,
             "paswordi": fjalkalimi,
             "hash": paswordi_coptuar[1]
             }
        # appending data to emp_details
        temp2.append(t)
    write_json2(data2)


elif int(veprimi) == 2:

    paswordi_adminit = input("Jep paswordin e adminit: ")
    progami = input('Jep te dhenat e cilit program do : ')
    hash_admin = hashlib.pbkdf2_hmac('sha256', paswordi_adminit.encode(), b's', 100000)
    admini_enkoduar = binascii.hexlify(hash_admin)
    admini_vetem_hash = str(admini_enkoduar).split("'")

    with open('admin.json') as ad:
        adin = json.load(ad)
        tema = adin['Admin']
        tema_ndar1 = str(tema).split(":")
        tema_ndar2 = str(tema_ndar1[1]).split("'")
        if tema_ndar2[1] == admini_vetem_hash[1]:
            with open('lista.json') as json_file:
                data = json.load(json_file)
                temp = data['em-details']
                for i in range(0,len(temp)):
                    e_dhena = temp[i]
                    if progami == e_dhena['Aplikacioni']:
                        x = {
                            'Email': e_dhena['Email'],
                            'Fjalkalimi': e_dhena['Password']
                        }
                        print(x)
                    else:
                        print('Ky aplikacion nuk egziston ne te dhenat e tua!! Shiko per gabime drejtshkrimore!')
        else:
            print('Error')
elif int(veprimi) == 3:
    paswordi_adminit = input("Jep password e adminit: ")
    hash_admin = hashlib.pbkdf2_hmac('sha256', paswordi_adminit.encode(), b's', 100000)
    admini_enkoduar = binascii.hexlify(hash_admin)
    admini_vetem_hash = str(admini_enkoduar).split("'")

    with open('admin.json') as ad:
        adin = json.load(ad)
        tema = adin['Admin']
        tema_ndar1 = str(tema).split(":")
        tema_ndar2 = str(tema_ndar1[1]).split("'")
        if tema_ndar2[1] == admini_vetem_hash[1]:
            hashi = input("Jep vleren e cilit pasword do te gjesh : ")
            with open('pas2.json') as r:
                data3 = json.load(r)
                temp3 = data3['Pasword-details']
                for i in range(0,len(temp3)):
                    gjejm_pasin = temp3[i]
                if hashi == gjejm_pasin['hash']:
                    print(gjejm_pasin['paswordi'])
                else:
                    print('Ky password nuk egziston!!!')
else:
    print('Vler e pa deklaruar ne fillim!')