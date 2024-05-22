import random
import tkinter
from tkinter import messagebox
import time
canvasWidth = 3440
canvasHeight = 1400
fenetre = tkinter.Tk()
canvas = tkinter.Canvas(fenetre, width=canvasWidth, height=canvasHeight, bg="gray21")
canvas.pack()
raquette = canvas.create_rectangle(0, 0, 40, 10, fill="red3")
balle = canvas.create_oval(0, 0, 10, 10, fill="darkorange")
fenetreOuverte = True
score = 0
def boucle_principale():
    while fenetreOuverte == True:
        deplacer_raquette()
        deplacer_balle()
        fenetre.update()
        time.sleep(0.02)
        if fenetreOuverte == True:
            verifier_game_over()
gaucheAppuyé = 0
droitAppuyé = 0
def quand_touche_appuyé(event):
    global gaucheAppuyé, droiteAppuyé
    if event.keysym == "Left":
        gaucheAppuyé = 1
    elif event.keysym == "Right":
        droiteAppuyé = 1
def quand_touche_relachée(event):
    global gaucheAppuyé, droiteAppuyé
    if event.keysym == "Left":
        gaucheAppuyé = 0
    elif event.keysym == "Right":
        droiteAppuyé = 0
vitesseRaquette = 6
def deplacer_raquette():
    mouvRaquette = vitesseRaquette*droiteAppuyé - vitesseRaquette*gaucheAppuyé
    (gaucheRaquette, hautRaquette, droiteRaquette, basRaquette) = canvas.coords(raquette)
    if ((gaucheRaquette > 0 or mouvRaquette > 0) and (droiteRaquette < canvasWidth or mouvRaquette < 0)):
        canvas.move(raquette, mouvRaquette, 0)
mouvBalleX = 4
mouvBalleY = -4
défHautRaquette = canvasHeight -40
défBasRaquette = canvasHeight -30
def deplacer_balle():
    global mouvBalleX, mouvBalleY, score
    (gaucheBalle, hautBalle, droiteBalle, basBalle) = canvas.coords(balle)
    if mouvBalleX > 0 and droiteBalle > canvasWidth:
        mouvBalleX = -mouvBalleX
    if mouvBalleX < 0 and gaucheBalle < 0:
        mouvBalleX = -mouvBalleX
    if mouvBalleY < 0 and hautBalle < 0:
        mouvBalleY = -mouvBalleY
    if mouvBalleY > 0 and basBalle > défHautRaquette and basBalle < défBasRaquette:
        (gaucheRaquette, hautRaquette, droiteRaquette, basRaquette) = canvas.coords(raquette)
        if droiteBalle > gaucheRaquette and gaucheBalle < droiteRaquette:
            mouvBalleY = -mouvBalleY
            mouvBalleX = random.randint(-10,10)
            print (mouvBalleX)
            score = score + 1
    canvas.move(balle, mouvBalleX, mouvBalleY)
mscore = 0
if score == 1 :
    mscore = mscore + 1
message_meilleur_score = "Tu  a eu le meilleur score !"
def verifier_game_over():
    (gaucheBalle, hautBalle, droiteBalle, basBalle) = canvas.coords(balle)
    if hautBalle > canvasHeight:
        message_game_over = "ton score est de " + str(score) + " veux tu rejouer ?"
        rejouer = tkinter.messagebox.askyesno(message= message_game_over)
        if rejouer == True:
            i
            ok_rejouer = tkinter.messagebox.askyesno(message = message_meilleur_score)
            if ok_rejouer == True:
                réinitialiser()
        else:
            if mscore == 1:
                ok = tkinter.messagebox.askyesno(message = message_meilleur_score)
                if ok == True:
                    fermer()
        
def fermer():
    global fenetreOuverte
    fenetreOuverte = False
    fenetre.destroy()
def réinitialiser():
    global score
    global gaucheAppuyé, droiteAppuyé
    global mouvBalleX, mouvBalleY
    gaucheAppuyé = 0
    droiteAppuyé = 0
    mouvBalleX = 4
    mouvBalleY = -4
    canvas.coords(raquette, 10, défHautRaquette, 50, défBasRaquette)
    canvas.coords(balle, 20, défHautRaquette-10, 30, défHautRaquette)
fenetre.protocol("WM_DELETE_WINDOW", fermer)
fenetre.bind("<KeyPress>", quand_touche_appuyé)
fenetre.bind("<KeyRelease>", quand_touche_relachée)
réinitialiser()
boucle_principale()    
score = 0

