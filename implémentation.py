def create_stack():
    return []

def empiler(x, stack):
    stack.append(x)

def depiler(stack):
    return stack.pop()

def height(stack):
    return len(stack)

def is_empty(stack):
    return height(stack)==0

def sommet(stack):
    return stack[-1]

def verify(exp):
#Creation d'un pile vide:
    p=create_stack()
#Parcourir la liste exp qui contient l'expression mathematique:
    for i in range(len(exp)):
        if exp[i]=='(':
            empiler(i, p)
        elif exp[i]==')':
            if is_empty(p):
                return ") à l'indice "+str(i)+" n'est pas ouverte !"
            else:
                j=depiler(p)
                print("Parenthése {} et {} correct".format(i,j))
    if is_empty(p):
        return 'Parenthésage valide'
    else:
        return "à l'indice "+str(sommet(p))+" n'est pas fermée !"

exp="(a+b*(c+d*(e+f)))"
print(verify(exp))