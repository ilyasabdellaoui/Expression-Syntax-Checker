def creer_pile():
    return []

def empiler(x, pile):
    pile.append(x)

def depiler(pile):
    return pile.pop()

def hauteur(pile):
    return len(pile)

def est_pile_vide(pile):
    return hauteur(pile)==0

def sommet(pile):
    return pile[-1]

def verify(exp):
#Creation d'un pile vide:
    p=creer_pile()
#Parcourir la liste exp qui contient l'expression mathematique:
    for i in range(len(exp)):
        if exp[i] == '(':
            empiler(i, p)
        elif exp[i] == ')':
            if est_pile_vide(p):
                return "Parenthésage non valide: Une parenthèse fermante ')' à l'indice "+str(i)+" n'est pas ouverte !"
            else:
                j = depiler(p)
                print("Parenthéses {} et {} correct".format(i, j))
    if est_pile_vide(p):
        return 'Parenthésage valide'
    else:
        return "Parenthésage non valide: Une parenthèse ouvrante '(' à l'indice "+str(sommet(p))+" n'est pas fermée !"
