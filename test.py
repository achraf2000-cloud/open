import datetime
try :
 f=open("c:/form.txt","w")
 x=datetime.datetime.now()
 f.write(str(x))
 f.write("\nC'est la date et l'heure")
 f.close()
 if int(x.month)==12 :
    print("C'est la date d'aujourd'hui")
 else :
    print("Ce n'est pas aujourd'hui")
except Exception as v :
    print("erreur", format(v))

f=open("c:/form.txt","r")
print(f.read())