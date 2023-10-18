#1) Ecrire une fonction commence_par prenant en argument une lettre et un mot et qui renvoie True 
# si le mot commence par la lettre donnée en argument, False sinon.
def  commence_par(lettre,mot):
    if mot[0]==lettre:
        return True
    else:
        return False
    
print(commence_par('h','hello'))
print(commence_par('o','hello'))

#2) Ecrire une fonction contient_voyelle qui prend en argument un mot et qui renvoie True si le mot 
#contient une voyelle, False sinon.
def contient_voyelle(mot):   
    test=False
    i=0
    while (i<len(mot)):
        if mot[i] in 'aeiouy':
        #{'a', 'e', 'i', 'o', 'u', 'y'}:
            test=True            
            break
        i=i+1
    return test

print(contient_voyelle('mot'))


#parcours à l'envers
mot='arrivee'
for i in range(len(mot)-1,-1,-1): 
    print(mot[i])

#3) Ecrire une fonction derniere_consonne qui prend en argument un mot et qui renvoie deux valeurs de retour: l'indice de sa dernière consonne ainsi que la dernière consonne (comme pour les listes, on considérera que l'indice de la première lettre est zéro). 
#On ne traitera pas le cas problématique où le mot ne contient pas de consonne.
def derniere_consonne(mot):
    i=len(mot)-1
    while (i>-1):  
        if mot[i] not in 'aeiouy':
            indice=i
            break
        else:
            i=i-1
    return indice,mot[indice]

print(derniere_consonne('arrivee'))
#4)
def double_consonne(mot):
    test=False
    p=None
    i=0
    while (i<=(len(mot)-2)):
        if mot[i]not in 'aeiouy' and mot[i]==mot[i+1]:
            test=True
            p=mot[i]
            break
        else:
            test=False
            i=i+1
    return test,p
    

mot='arrivee'
print(double_consonne(mot))

mot='bonbon'
print(double_consonne(mot))

mot='reussite'
print(double_consonne(mot))
#5)
def envers(li):
    l=li[::-1]
    return(l)
    
li=[1,2,3]
envers(li)
print('li',li)

#forward
def forward(li):
    l=li[::1]
    print(l)

forward(li)

#6)
def palindrome(mot):    
    if mot==envers(mot):
        return True
    else:
        return False
    
mot='ici'
print(palindrome(mot))

mot='aller'
print(palindrome(mot))

#7)
def mot_autorise(mot,l):
    if mot in l:
        return False
    else:
        return True

mot='fric'
l= ['sous', 'fric', 'thune', 'ble']
print(mot_autorise(mot,l))

mot='argent'
l= ['sous', 'fric', 'thune', 'ble']
print(mot_autorise(mot,l))
