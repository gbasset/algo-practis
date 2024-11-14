# les variables et leurs types-
age:int = 31
size = 17.8
chiffre = '56'
person:str = 'Gaëtan'
person2:str = 'John'
print(person is not person2)
print(int(chiffre))
# set Ensembles
monSel = set((5,14,7,8))
monSel.add(56)
print(type(monSel), len(monSel))

# Listes
marmelades:list[str] = ['Dude', 'Coke', 'Nul','Truc']
fruits = ['pommes', 'poires', 'raisins', 'fraises', 'pasteque','pipino','kékéte', 'tutute','jj']
#fruits.append('fraises')

print(fruits)
pepins = fruits[1:4]
print(pepins)
## Le pas, ::2 1 sur 2 ou 3
print(fruits[::5])
# changer un élément
fruits[5] = 'PIPINETTE'
print(fruits[::5])
print(len(fruits))

# les Tuples, immutables
monTuple = (5,6,78,77,76)
print(monTuple, type(monTuple))
print(monTuple[::3])
# strings
maPhrase = 'Hello'
print(maPhrase.lower())
print(maPhrase.capitalize())
print(maPhrase.upper())

# dictionnaire
monDico = {
    'name' : 'JeanJean',
    'nickname' : 'kukute',
    'age': 23 ,
}
monDico['sexe'] = 'zizi'
print(monDico)
print(monDico.keys())
# les conditions
a = 40
b = 7
if a < b :
    print('b super à A')
else :
    print('a est egale ou plus grand que B')

# Les boucles
for fruit in fruits :
    print(fruit)
monRangeList = list(range(7))
print(monRangeList)

for j in range(7):
     print(j)
for j in range(len(fruits)):
    print("fruit", j + 1 , fruits[j])
i = 0
while i < 4 :
    print('increment : ',i)
    i += 1 # incre 1
numberUser = 0
while numberUser < 5:
    userResponse = input("Entrer une valeur numérique :")
    numberUser = int(userResponse)
    print(numberUser)

ch = "france"
for c in ch:
    if c == "a":
             break
    print(c)
kiip = 'Turquie'
for k in kiip:
    if(k != "i"):
        continue
    print("Letter",k)

