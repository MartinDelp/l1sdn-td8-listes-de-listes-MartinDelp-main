# Exercice 1 - Carré magique

def somme_ligne(position_ligne, tableau):
    """Calcul la somme des éléments de la ligne à <position_ligne> du <tableau>
    :param position_ligne: (int) la position d'une ligne du tableau
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la ligne à <position_ligne> du <tableau>"""
    res = 0 
    for i in range (len(tableau[position_ligne])):
        res += tableau[position_ligne][i]
    return res
        

def somme_colonne(position_colonne, tableau):
    """Calcul la somme des éléments de la colonne à <position_colonne> du <tableau>
    :param position_colonne: (int) la position d'une colonne du tableau
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la colonne à <position_colonne> du <tableau>"""
    res = 0 
    for i in range (len(tableau[position_colonne])):
        res += tableau[position_colonne][i]
    return res
        

def somme_diagonale(diagonale, tableau):
    """Calcul de la somme des éléments sur la <diagonale>. 
    Si <diagonale>=0 c'est la diagonale partant du coin supérieur gauche au coin inférieur droit, 
    Si <diagonale>=1 c'est du coin inférieur gauche au coin supérieur droit.
    :param diagonale: (int) l'identifiant de la diagonale
    :param tableau: (list) un tableau
    :return: (int) la somme des éléments de la <diagonale> du <tableau>"""
    res = 0 
    for i in range (len(tableau[diagonale])):
        res += tableau[diagonale][i]
    return res

def possede_elements_1_a_N(tableau):
    """Test si tous les éléments de 1 à N sont présent dans le <tableau> où N est le nombre de cases du <tableau>
    :param grille: (list)
    :return: (bool) si tous les éléments de 1 à N sont présent dans le tableau"""
    n = len(tableau)**2
    l = [ 0 for i in range(n)]
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if l[tableau[i][j]-1] == 0:
                l[tableau[i][j]-1]=1
            else:
                return False
    return sum(l) == len(l)

def est_carre_magique(carre_magique):
    """Test si la grille <carre_magique> est un carre_magique.
    :param carre_magique: (list)
    :return: (bool) True si c'est un carre_magique, False sinon"""
    if not possede_elements_1_a_N(carre_magique):
        return False
    d = somme_diagonale(0, carre_magique)
    if d != somme_diagonale(1, carre_magique):
        return False
    for i in range(len(carre_magique)):
        if d != somme_ligne(i, carre_magique) or somme_colonne(i, carre_magique) != d:
            return False 
    return True

# Exercice 2 - Dessin Textuel

def grille(x, y):
    """Retourne une grille de points
    :param x: (int) le nombre de colonnes
    :param y: (int) le nombre de lignes
    :return: (list) une grille de x lignes et y colonnes"""
    res = []
    for i in range(y):
        res.append([])
        for j in range(x):
            res[i].append(".")
    return res
    
def afficher_grille(g):
    """Affiche la grille <g>
    :param g: (list) une grille
    :return: (None)"""
    for i in range(len(g)):
        for j in range(len(g[i])):
            print(g[i][j], end="")
        print()

def dessiner_point(grille, x, y, symbole):
    """Modifie <grille> en changeant le symbole à (<x>,<y>) par <symbole>
    :param grille: (list) une grille
    :param x: (int) le numéro de colonne
    :param y: (int) le numéro de ligne
    :symbole: (str) le symbole a mettre
    :return: (None)"""
    grille[x][y] = symbole


def dessiner_rectangle(grille, x1, y1, x2, y2, symbole):
    """Remplace les cases du rectangle dont le point supérieur gauche est (<x1>, <y1>) et le coin 
    inférieur droit est (<x2>, y2>) dans <grille> par <symbole>
    :param grille: (list) la grille
    :param x1: (int) numéro de colonne du point supérieur gauche du rectangle
    :param y1: (int) numéro de ligne du point supérieur gauche du rectangle
    :param x2: (int) numéro de colonne du point inférieur droit du rectangle
    :param y2: (int) numéro de ligne du point inférieur droit du rectangle
    :param symbole: (str) le symbole à mettre
    :return: (None)"""
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            dessiner_point(grille, x, y, symbole)

# Exercice 3 - Morpion

def est_libre(grille, x, y):
    """Test si la case (<x>,<y>) de <grille> est disponible ou non.
    :param grille: (list) la grille
    :param x: (int) numéro de colonne
    :param y: (int) numéro de ligne
    :return: (bool) True si la case (<x>,<y>) de <grille> est vide"""
    return grille[y][x] == '.'

def placer_pion(grille, pion, x, y):
    """Place <pion> dans <grille> à la case (<x>,<y>)
    :param grille: (list) la grille
    :param pion: (str) soit "x" soit "o"
    :param x: (int) numéro de colonne
    :param y: (int) numéro de ligne
    :return: (None)"""
    dessiner_point(grille, x, y, pion)

def est_gagnant(grille):
    """Test s'il y a un gagnant ou non dans <grille>
    :param grille: (list) la grille
    :return: (bool) True s'il y a une ligne/colonne/diagonale de même symbole"""
    for i in range(3):
        if (grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] in "xoXO") or (grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] in "xoXO"):
            return True
    return (grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] in "xoXO") or (grille[2][0] == grille[0][2] == grille[1][1] and grille[2][0] in "xoXO")

def partie():
    """Joue une partie de morpion
    :return: (None)"""
    grille = [[".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]]
    afficher_grille(grille)
    pass