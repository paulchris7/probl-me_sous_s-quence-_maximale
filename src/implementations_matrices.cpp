#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include "../header/implementations_matrices.h"

using namespace std;

// Algorithme de Kadane pour trouver la sous-séquence maximale dans un tableau 1D
int kadane(const vector<int>& array) {
    int max_global = array[0];
    int max_courant = array[0];
    
    for (int i = 1; i < array.size(); i++) {
        max_courant = max(array[i], max_courant + array[i]);
        max_global = max(max_global, max_courant);
    }
    
    return max_global;
}

// Algorithme pour trouver la sous-matrice maximale - O(n³)
int sousMatiiceMaximale(const vector<vector<int>>& matrix) {
    int n = matrix.size();    // Nombre de lignes
    int m = matrix[0].size(); // Nombre de colonnes
    
    int max_somme = matrix[0][0]; // Initialisation avec le premier élément
    
    // Cas de toutes les sous-matrices possibles
    for (int debut_col = 0; debut_col < m; debut_col++) {
        
        // Tableau temporaire pour stocker la somme des éléments de chaque ligne
        vector<int> temp(n, 0);
        
        for (int fin_col = debut_col; fin_col < m; fin_col++) {
            
            // Ajout des valeurs de la colonne fin_col au tableau temporaire
            for (int i = 0; i < n; i++) {
                temp[i] += matrix[i][fin_col];
            }
            
            // Application de l'algorithme de Kadane pour trouver la somme maximale dans temp
            int max_kadane = kadane(temp);
            
            // Mise à jour de la somme maximale
            max_somme = max(max_somme, max_kadane);
        }
    }
    
    return max_somme;
}

// Algorithme naïf pour trouver la sous-matrice maximale - O(n^6)
int sousMatriceMaximaleNaive(const vector<vector<int>>& matrix) {
    int n = matrix.size();    // Nombre de lignes
    int m = matrix[0].size(); // Nombre de colonnes
    
    int max_somme = matrix[0][0]; // Initialisation avec le premier élément
    
    // Cas de toutes les sous-matrices possibles
    for (int debut_ligne = 0; debut_ligne < n; debut_ligne++) {
        for (int debut_col = 0; debut_col < m; debut_col++) {
            for (int fin_ligne = debut_ligne; fin_ligne < n; fin_ligne++) {
                for (int fin_col = debut_col; fin_col < m; fin_col++) {
                    
                    // Calcul de la somme de cette sous-matrice
                    int somme = 0;
                    for (int i = debut_ligne; i <= fin_ligne; i++) {
                        for (int j = debut_col; j <= fin_col; j++) {
                            somme += matrix[i][j];
                        }
                    }
                    
                    // Mise à jour la somme maximale
                    max_somme = max(max_somme, somme);
                }
            }
        }
    }
    
    return max_somme;
}

// Algorithme moins naïf pour trouver la sous-matrice maximale - O(n⁴) mais avec des optimisations
int sousMatriceMaximaleMoinsNaive(const vector<vector<int>>& matrix) {
    int n = matrix.size();    // Nombre de lignes
    int m = matrix[0].size(); // Nombre de colonnes
    
    // Prétraitement: calcul des sommes préfixes
    vector<vector<int>> prefixSums(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            prefixSums[i][j] = matrix[i-1][j-1] + prefixSums[i-1][j] + prefixSums[i][j-1] - prefixSums[i-1][j-1];
        }
    }
    
    int max_somme = matrix[0][0]; // Initialisation avec le premier élément
    
    // Cas de toutes les sous-matrices possibles
    for (int debut_ligne = 0; debut_ligne < n; debut_ligne++) {
        for (int debut_col = 0; debut_col < m; debut_col++) {
            for (int fin_ligne = debut_ligne; fin_ligne < n; fin_ligne++) {
                for (int fin_col = debut_col; fin_col < m; fin_col++) {
                    
                    // Calcul de la somme de cette sous-matrice en O(1) en utilisant les sommes préfixes
                    int somme = prefixSums[fin_ligne+1][fin_col+1] - prefixSums[fin_ligne+1][debut_col] 
                              - prefixSums[debut_ligne][fin_col+1] + prefixSums[debut_ligne][debut_col];
                    
                    // Mise à jour la somme maximale
                    max_somme = max(max_somme, somme);
                }
            }
        }
    }
    
    return max_somme;
}