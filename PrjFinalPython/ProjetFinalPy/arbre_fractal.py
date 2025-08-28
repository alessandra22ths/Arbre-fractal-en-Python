import turtle  # On importe le module turtle pour dessiner

# Initialise 
def initialiser_turtle():
    turtle.speed("fastest")  
    turtle.left(90)          
    turtle.penup()           
    turtle.goto(0, -200)     
    turtle.pendown()         

# Dessine une branche en avançant
def dessiner_branche(longueur):
    turtle.forward(longueur)

# Revient à la position précédente
def retourner_position(longueur):
    turtle.backward(longueur)

# Fonction récursive qui dessine l'arbre
def arbre_fractal(longueur, niveau):
    if niveau == 0:
        return  
    dessiner_branche(longueur)  
    turtle.left(30)  
    arbre_fractal(longueur * 0.7, niveau - 1)  
    turtle.right(60)  
    arbre_fractal(longueur * 0.7, niveau - 1)  
    turtle.left(30)  
    retourner_position(longueur)  

# Fonction principale qui lance le programme
def dessiner_arbre():
    initialiser_turtle()     
    arbre_fractal(100, 5)    
    turtle.done()            

dessiner_arbre()  # Appel de la fonction principale
