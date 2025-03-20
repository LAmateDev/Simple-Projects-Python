import random 

alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alf = alfabeto.split()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sim = "* ! @ # $ % & "
sim2 = sim.split()

def criar_senha():
    l1 = []
    x = None

    for i in range(5):
        e = random.choice(alf)
        l1.append(e)
        n = random.choice(num)
        l1.append(n)
    
    for i in range(2):
        s = random.choice(sim2)
        l1.append(s)
    
    random.shuffle(l1)
    x = ''.join(str(elemento) for elemento in l1)
    return x

senha = criar_senha()
print(senha)


    

    
    
