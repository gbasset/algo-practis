# exceptions
def inverse(n):
    try:
        return 1/n
    except ZeroDivisionError:
        print('Division par zéro interdite')
        return None
nb = inverse(5)
print(nb)