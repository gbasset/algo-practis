#/* ÉNONCÉ 📚 */

#/* Créez un algorithme qui retourne la chaîne de caractères passée en argument à l'envers. */

#/* Tests à passer 🧪 */
def reverseFn(str):
    arr = list(reversed(list(str)))
    return ''.join(arr)




print(reverseFn("Bonjour à tous"));                         #// suot à ruojnoB
print(reverseFn("Être haut comme trois pommes"));           #// semmop siort emmoc tuah ertÊ
print(reverseFn("Ne pas chercher midi à quatorze heures")); #// serueh ezrotauq à idim rehcrehc sap eN