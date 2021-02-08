# import bibliothèque
import numpy as np
import sys
import random
import pygame
from tkinter import*



# couleurs
bleu = (67,121,171)
noir = (0,0,0,)
blanc = (255,255,255)
rouge = (250,48,37)
jaune = (255,255,0)
gris = (208,208,208)

# création grille
ligne = 6
colonne = 7


# ...

taille = 100
largeur = 7*taille
hauteur = (6+1)*taille
radius = int(taille/2 - 5)
ecran = pygame.display.set_mode((largeur,hauteur))

pygame.font.init()
font = pygame.font.SysFont('Users\neveu\Downloads\minecraftia.ttf', 50)
win1 = font.render('PLAYER 1 WON', True, rouge)
win2 = font.render('PLAYER 2 WON', True, bleu)
egal = font.render('EGALITE', True, blanc)



def plateaufull(plateau):
    #envoie True si la grille est pleine, si il n'y a plus de 0
    a = 0 in plateau
    if a == True:
        return False
    else:
        return True

def tour(joueur,plateau):
    run = True
    while run:
        col = position()+1
        try:
            col = int(col)
            print(col)
            if col < 8 and col > 0:
                run = False
                print (insert(col,joueur,plateau))
                pygame.display.update()

            else:
                print('Entrez un nombre compris entre 1 et 7')
        except ValueError:
            print(e)
            print('Entrez une valeur valide')

def insert(col,joueur,plateau):
    #Prends valeur colonne demandée dans tour() et remplace le 0 par 1 ou 2 (selon le joueur)
    sol = -1

    try:
        while plateau[sol][col-1] !=0:

            sol=sol-1
    except:
        print('Colonne pleine')
    else:
        plateau[sol][col-1] = joueur
        draw(taille,hauteur,ecran,radius,plateau)
    return plateau

def win(plateau,joueur):
    # vérifier victoires horizontales
    for c in range(colonne-3):
        for l in range(ligne):
            if plateau[l][c] == joueur and  plateau[l][c+1] == joueur and  plateau[l][c+2] == joueur and  plateau[l][c+3] == joueur:
                return True

    # vérifier victoires verticales
    for c in range(colonne):
        for l in range(ligne-3):
            if plateau[l][c] == joueur and  plateau[l+1][c] == joueur and  plateau[l+2][c] == joueur and  plateau[l+3][c] == joueur:
                return True
    # vérifier victoires diagonales monantes
    for c in range(colonne-3):
        for l in range(ligne-3):
            if plateau[l][c] == joueur and  plateau[l+1][c+1] == joueur and  plateau[l+2][c+2] == joueur and  plateau[l+3][c+3] == joueur:
                return True

    # vérifier victories diagonales descendantes
    for c in range(colonne-3):
        for l in range(ligne):
            if plateau[l][c] == joueur and  plateau[l-1][c+1] == joueur and  plateau[l-2][c+2] == joueur and  plateau[l-3][c+3] == joueur:
                return True

def IA(joueur,plateau):
    time.sleep(0.70)
    col = random.randint(1,7)
    print(insert(col,joueur,plateau))

def choixrej():
    main()
    
def rejouer():
    time.sleep(1.5)
    fagain = Tk()
    fagain.title("Puissance 4")
    fagain.geometry("800x600")
    fagain.minsize(540,360)
    fagain.maxsize(1080,720)

    playagain = Label(fagain, text='PLAY AGAIN ?', font=('Fipps',35))
    playagain.pack()

    yesbtn = Button(fagain, text='Yes', font=('Minecraftia',20),command= choixrej)
    yesbtn.pack(pady = 70)

    nobtn = Button(fagain, text='No', font=('Minecraftia',20),command = quit)
    nobtn.pack()

    fagain.mainloop()
    
def position():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (posx,posy) = pygame.mouse.get_pos()
                return int(posx/100)

def pygameboard(plateau):
    # création fenetre
    pygame.init()
    pygame.display.set_caption('Puissance 4')    
    radius = int(taille/2 - 5)

    for c in range(colonne):
        for l in range(ligne):
            pygame.draw.rect(ecran,gris,(c*taille,l*taille+taille,taille,taille))
            if plateau[l][c] == 0:
                pygame.draw.circle(ecran,blanc, (int(c*taille+taille/2),int(l*taille+taille+taille/2)), radius)
    pygame.display.update()  

def draw(taille,hauteur,ecran,radius,plateau):
    for c in range(colonne):
        for l in range(ligne):
            pygame.draw.rect(ecran,gris,(c*taille,l*taille+taille,taille,taille))
            if plateau[l][c] == 0:
                pygame.draw.circle(ecran,blanc, (int(c*taille+taille/2),int(l*taille+taille+taille/2)), radius)
            elif plateau[l][c] == 1:
                pygame.draw.circle(ecran,rouge, (int(c*taille+taille/2),int(l*taille+taille+taille/2)), radius)
            else:
                pygame.draw.circle(ecran,bleu, (int(c*taille+taille/2),int(l*taille+taille+taille/2)), radius)
    pygame.display.update()

def confirm(a,plateau):
    if a == 'duo':
        return tour(2,plateau)
    else:
        return IA(2,plateau)

def main():

    # choix solo ou duo
    print("----- Jeu du puissance 4 -----")
    a = input("Tu veux jouer en: solo ou duo ?")

    
    
    plateau = np.zeros((ligne,colonne))
    pygameboard(plateau)
    

    while not (plateaufull(plateau)): #tant que la grille n'est pas totalement remplie ...

        tour(1,plateau)
        if win(plateau,1):
            print("LE JOUEUR 1 A GAGNE !!!")
            ecran.blit(win1, (200, 30))
            pygame.display.update()
            rejouer()
        else:
            confirm(a,plateau) #----> renvoie choix du joueur (soit solo ou duo)
        if win(plateau,2):
            print("LE JOUEUR 2 A GAGNE !!!")
            ecran.blit(win2, (200, 30))
            pygame.display.update()
            rejouer()




    if plateaufull(plateau) == True: # si la grille est totalement remplie et que le dernier coup n'est pas une victoire alors c'est une égalité
        ecran.blit(egal, (250, 30))
        pygame.display.update()
        rejouer()
        print("Egalité")


main()

