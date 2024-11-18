import pytest

from L1SDN_FP_TD8 import *

# Exercice 1 - Tests pour le Carré magique

def test_somme_ligne():
    tableau = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    assert somme_ligne(0, tableau) == 15
    assert somme_ligne(1, tableau) == 15
    assert somme_ligne(2, tableau) == 15

def test_somme_colonne():
    tableau = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    assert somme_colonne(0, tableau) == 15
    assert somme_colonne(1, tableau) == 15
    assert somme_colonne(2, tableau) == 15

def test_somme_diagonale():
    tableau = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    assert somme_diagonale(0, tableau) == 15
    assert somme_diagonale(1, tableau) == 15

def test_possede_elements_1_a_N():
    tableau = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    assert possede_elements_1_a_N(tableau) == True

def test_est_carre_magique():
    carre_magique = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    assert est_carre_magique(carre_magique) == True
    non_carre_magique = [[2, 7, 6], [9, 5, 2], [4, 3, 8]]
    assert est_carre_magique(non_carre_magique) == False

# Exercice 2 - Tests pour Dessin Textuel

def test_grille():
    assert grille(3, 3) == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert grille(2, 2) == [['.', '.'], ['.', '.']]

def test_dessiner_point():
    g = grille(3, 3)
    dessiner_point(g, 1, 1, 'X')
    assert g == [['.', '.', '.'], ['.', 'X', '.'], ['.', '.', '.']]

def test_dessiner_rectangle():
    g = grille(3, 3)
    dessiner_rectangle(g, 0, 0, 1, 1, 'O')
    assert g == [['O', 'O', '.'], ['O', 'O', '.'], ['.', '.', '.']]

# Exercice 3 - Tests pour Morpion

def test_est_libre():
    g = grille(3, 3)
    assert est_libre(g, 1, 1) == True
    dessiner_point(g, 1, 1, 'X')
    assert est_libre(g, 1, 1) == False

def test_placer_pion():
    g = grille(3, 3)
    placer_pion(g, 'X', 1, 1)
    assert g[1][1] == 'X'

def test_est_gagnant():
    g = [['X', 'X', 'X'], ['.', '.', '.'], ['.', '.', '.']]
    assert est_gagnant(g) == True
    g = [['X', '.', '.'], ['X', '.', '.'], ['X', '.', '.']]
    assert est_gagnant(g) == True
    g = [['X', '.', '.'], ['.', 'X', '.'], ['.', '.', 'X']]
    assert est_gagnant(g) == True
    g = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    assert est_gagnant(g) == False

if __name__ == "__main__":
    pytest.main()