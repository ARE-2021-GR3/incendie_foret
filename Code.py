import random

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation
from matplotlib import colors

cmap = colors.ListedColormap(["white", "green", "orange", "red"])


# Paramètres du modèle
voisin = 1          # Taille du voisinnage
max_tour = 100      # Nombre de tours
n,m = 100,100       # Taille de la forêt
p_igni = 0.000005   # Pourcentage de chance d'ignition
p_vege = 0.005      # Pourcentage de chance que la végétation repousse
densite = 0.5       # Densité de la forêt
seuil = 3           # Temps que met le feu pour s'eteindre
p_meteo = 0.01      # Pourcentage de chance que la météo change  


# Paramètres météo
vent_ouest = 0      # Force du vent : 0, 1 ou 2
pluie = 0         # Taux de précipitation (empeche le feu de se propager)


# Génère la forêt
def generate_foret(n,m) :
  A = np.zeros((n,m))
  for i in range (0,n) :
    for j in range (0,m) :
      p = random.random()
      if p < densite :
        A[j,i] = 0    # Forêt (0)
      else :
        A[j,i] = -1   # Vide (-1)
  return A


# Met en feu l'arbre qui est aux coordonnées (x,y)
def arbre_en_feu(x,y,monde) :
  if (monde [y,x] == 0) : 
    monde [y,x] = 1
  return monde


# Met un arbre en feu au hasard
def feu_au_hasard(monde) :
  x = random.randint(0, n-1)
  y = random.randint(0, m-1)
  if (monde [y,x] == 0) : 
    arbre_en_feu(x,y,monde)
  else :
    feu_au_hasard(monde)
  return monde


# Fais apparaitre un feu au hasard, avec p_igni de chance
def apparition_feu(monde) :
  for i in range(0,n) :
    for j in range(0,m) :
      if (monde [j,i] == 0) : 
        p = random.random()
        if p < p_igni :
          monde [j,i] = 1
  return monde

# Fais apparaitre de la végétation, avec p_vege de chance
def apparition_vege(monde) :
  for i in range(0,n) :
    for j in range(0,m) :
      if (monde [j,i] == -1) : 
        p = random.random()
        if p < p_vege :
          monde [j,i] = 0
  return monde


# Donne les coordonnées des voisins d'une case
def voisinage(x,y,monde) :
  voisinage = []
  i = voisin
  while i > 0 :
    if x-voisin >= 0 and vent_ouest < 2 :
      voisinage.append((x-i,y)) 
    if y-voisin >= 0 :
      voisinage.append((x,y-i))
    if x+voisin < n :
      voisinage.append((x+i,y))
    if y+voisin < m :
      voisinage.append((x,y+i))

    if vent_ouest > 0 :
      if x+voisin < n and y-i >= 0 :
        voisinage.append((x+i,y-i))
      if x+voisin < n and y+i < m :
        voisinage.append((x+i,y+i))

    if vent_ouest > 1 :
      if x+voisin < n :
        voisinage.append((x+i,y))
    
    i = i-1

  return voisinage


# Fais propager un feu une fois
def feu_propage(monde) :
  S = set()
  for i in range(0,n) :
    for j in range(0,m) :
      if (monde [j,i] in range(1,seuil)) : 
        S.add((i,j))
        monde [j,i] = monde [j,i]+1
      elif monde [j,i] == seuil :
        monde [j,i] = -1
  for (k,l) in S :
    copain = voisinage(k,l,monde)
    for (a,b) in copain :
      p = random.random()
      if p >= pluie :
        arbre_en_feu(a,b,monde)
  return monde


# Une boucle
def une_boucle(monde) :
  apparition_feu(monde)
  apparition_vege(monde)
  feu_propage(monde)
  return monde


# Change la météo au hasard
def meteo_hasard() :
  p = random.random()
  global vent_ouest
  global pluie
  if p < p_meteo/2 :
    vent_ouest = random.choice([0,1,2])
  elif p < p_meteo :
    pluie = random.choice([0,0.5,0.9])

# Donne le nombre total de case en feu 
def nb_case_feu(monde) :
  somme = 0
  for i in range(0,n) :
    for j in range(0,m) :
      if (monde [j,i] >= 1) :
        somme=somme+1
  return somme


# Trace les graphiques "Nombre d'arbres en feu en fonction du temps"
def graph(monde) :
  X = [i for i in range(max_tour)]
  Y = []
  for i in range(max_tour) :
    Y.append(nb_case_feu(monde))
    feu_propage(monde)
  fig = plt.figure(figsize=(4.5, 4.5))
  plt.plot(X,Y)
  plt.xlabel("Tour")
  plt.ylabel("Nombre d'arbres en feu")
  plt.show()

# Trace trois courbes en fonction de la météo
def tous_les_graph() :
  global vent_ouest
  global pluie

  monde = feu_au_hasard(generate_foret(n,m))
  monde_vent = np.zeros((n,m))
  for i in range (0,n) :
    for j in range (0,m) :
      monde_vent [j,i] = monde [j,i]
  monde_pluie= np.zeros((n,m))
  for i in range (0,n) :
    for j in range (0,m) :
      monde_pluie [j,i] = monde [j,i]

  vent_ouest = 0
  pluie = 0  
  X = [i for i in range(max_tour)]
  Y = []
  for i in range(max_tour) :
    Y.append(nb_case_feu(monde))
    feu_propage(monde)
  vent_ouest = 2
  pluie = 0
  A = [i for i in range(max_tour)]
  B = []
  for i in range(max_tour) :
    B.append(nb_case_feu(monde_vent))
    feu_propage(monde_vent)
  vent_ouest = 0
  pluie = 0.7
  C = [i for i in range(max_tour)]
  D = []
  for i in range(max_tour) :
    D.append(nb_case_feu(monde_pluie))
    feu_propage(monde_pluie)

  fig = plt.figure(figsize=(4.5, 4.5))
  plt.plot(X,Y, label="Normal")
  plt.plot(A,B, label="Vent : 1")
  plt.plot(C,D, label="Pluie : 0.7")
  plt.xlabel("Tour")
  plt.ylabel("Nombre d'arbres en feu")
  plt.legend()
  plt.show()
  vent_ouest = 0
  pluie = 0

tous_les_graph()


# Animation de l'incendie avec la météo
monde=feu_propage(feu_au_hasard(generate_foret(n,m)))

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(monde, cmap=cmap)

def animate(i):
  im.set_data(animate.monde)
  ax.set_title("Vent ouest = "+str(vent_ouest)+"           Pluie = "+str(pluie))
  animate.monde = une_boucle(animate.monde)
  meteo_hasard()
  

animate.monde = monde

interval = 50
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=50)
plt.show()
