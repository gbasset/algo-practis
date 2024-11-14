liste = list(range(5))
print(liste)
L = [4,5,8,77]
L.append(10)
print(L)
# definir une fonction def et return

def carre(x):
    return x **2
print(carre(5))

# paramètres optionnels
def affichage(*prenoms):
    return print('Le prénom choisi est : ', prenoms[2])
print(affichage('ZIZI','kuiui','io'))

def ma_fonction_arguments_arbritraires(**personne):
    return print('le nom est', personne['name'])
print(ma_fonction_arguments_arbritraires(prenom = 'Juju', name = 'Duduche', age = 36))

def maFonctionAvecParametreDefaut(ville = 'Paris'):
    return print(ville)
print(maFonctionAvecParametreDefaut())

# Fonction Recursive
def compte_a_rebour(nb):
    print('nombre: ', nb)
    nb_suivant = nb - 1
    if nb_suivant > 0 :
        compte_a_rebour(nb_suivant)
compte_a_rebour(14)
monNombre = 0
def calculer_nb(nb):
    nb_suivant = nb + 1
    if nb < 100:
        if nb_suivant < 100:
            print("nb_" , nb_suivant)
            return calculer_nb(nb_suivant)
        else:
            return nb_suivant
    return nb

monNombre = calculer_nb(42)
print('monNombre',monNombre)

def calculerSomme(n):
    if n > 0:
        print('n:::',n)
        return n + calculerSomme(n - 1)
    return 0

somme = calculerSomme(42)

print('somme : ', somme)

# Lambda
f = lambda  x : x + 50
f(10)


