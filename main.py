from processing import *


TAILLE = 6  
MUR    = 'M'
BANANE = 'B'
DK     = 'D'
VIDE   = ' '


dk_board = [
  [' ',' ',' ','M',' ',' '],  
  [' ','M',' ','M','M','B'],
  [' ','M',' ','M',' ',' '],
  [' ','M','M','M',' ','M'],
  [' ',' ',' ',' ',' ','M'],
  ['D','M',' ',' ',' ','M']]

ligne_DK   = 5  
colonne_DK = 0  

affiche_quadrillage = True
affiche_lettres     = True
affiche_images      = False

def affiche_tableau():
  larg = width//TAILLE  
  haut = height//TAILLE 
  
  if affiche_quadrillage:
    # on commence par un quadrillage
    # d'abord les lignes verticales
    for n in range(TAILLE):
      line ((n+1)*larg, 0, (n+1)*larg, height)
    # puis les lignes horizontales
    for n in range(TAILLE):
      line (0, (n+1)*haut, width, (n+1)*larg)
    # reste plus qu'à afficher le contenu du tableau
  textSize(larg)
  fill(0)
  for ligne in range(TAILLE):
    for colonne in range(TAILLE):
      if dk_board[ligne][colonne] == MUR:
        if affiche_images:
          image(image_mur,colonne*larg,ligne*haut,larg, haut)
      if dk_board[ligne][colonne] == BANANE:
        if affiche_images:
          image(image_banane,colonne*larg,ligne*haut,larg, haut)
      if dk_board[ligne][colonne] == DK:
        if affiche_images:
          image(image_DK,colonne*larg,ligne*haut,larg, haut)
      if affiche_lettres:
        if affiche_images:
          fill(0,0,0,165)
        else:
          fill(0)
        text(dk_board[ligne][colonne], colonne*larg+5, (ligne+1)*haut-5)

def setup():
  global image_fond, image_mur, image_banane,image_DKh, image_DKb,image_DKd,image_DKg, image_DK 
  size(300,300)   # taille de la fenêtre graphique
  frameRate(30)   # draw() sera appelée 30 fois par seconde
  stroke(0)       # couleur des tracés en noir
  strokeWeight(2) # 2 pixels de large
  image_fond   = loadImage("fondDK.jpg")
  image_mur    = loadImage("mur.png")
  image_banane = loadImage("arrivee.png")
  image_DKh    = loadImage("dk_haut.png")
  image_DKb    = loadImage("dk_bas.png")
  image_DKg    = loadImage("dk_gauche.png")
  image_DKd    = loadImage("dk_droite.png")
  image_DK     = loadImage("dk_droite.png")


  

def draw():
  background(220)
  if affiche_images:
    image(image_fond, 0,0, width,height)
  affiche_tableau() # on affiche le dk_board
  
def keyPressed(): 
  global ligne_DK, colonne_DK, image_DK, affiche_quadrillage, affiche_images, affiche_lettres
  possible = [VIDE,BANANE]
  if key in ['q','Q']:
    affiche_quadrillage = not affiche_quadrillage
  if key in ['i','I']:
    affiche_images = not affiche_images
  if key in ['l','L']:
    affiche_lettres = not affiche_lettres
  if key == CODED: # si une touche "spéciale" est pressée...
    if keyCode == UP: # si flêche vers le haut
      image_DK = image_DKh
      # si la montée est possible...
      if ligne_DK > 0 and dk_board[ligne_DK-1][colonne_DK] in possible:
        # on met du "vide" là où se trouve DK
        dk_board[ligne_DK][colonne_DK] = VIDE
        # puis on "déplace" DK
        ligne_DK -= 1
      dk_board[ligne_DK][colonne_DK] = DK
  if keyCode == DOWN: # si flêche vers le bas
      image_DK = image_DKb
      # si la descente est possible...
      if ligne_DK < TAILLE-1 and dk_board[ligne_DK+1][colonne_DK] in possible:
        # on met du "vide" là où se trouve DK
        dk_board[ligne_DK][colonne_DK] = VIDE
        # puis on "déplace" DK
        ligne_DK += 1
      dk_board[ligne_DK][colonne_DK] = DK
  if keyCode == LEFT: # si flêche vers la gauche
      image_DK = image_DKg
      # si aller à gauche est possible...
      if colonne_DK > 0 and dk_board[ligne_DK][colonne_DK-1] in possible:
        # on met du "vide" là où se trouve DK
        dk_board[ligne_DK][colonne_DK] = VIDE
        # puis on "déplace" DK
        colonne_DK -= 1
      dk_board[ligne_DK][colonne_DK] = DK
  if keyCode == RIGHT: # si flêche vers la droite
      image_DK = image_DKd
      # si aller à droite est possible...
      if colonne_DK < TAILLE-1 and dk_board[ligne_DK][colonne_DK+1] in possible:
        # on met du "vide" là où se trouve DK
        dk_board[ligne_DK][colonne_DK] = VIDE
        # puis on "déplace" DK
        colonne_DK += 1
      dk_board[ligne_DK][colonne_DK] = DK
      
run()