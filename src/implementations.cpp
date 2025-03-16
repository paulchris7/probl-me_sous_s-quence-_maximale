#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>
#include <fstream>
#include <iomanip>
#include "../headers/implementations.h"

using namespace std;


// Algorithme naïf - O(n³)
int algorithmeNaif(const vector<int>& T) {
    int n = T.size();
    int max_somme = T[0];
    
    for (int k = 0; k < n; k++) {
        for (int l = k; l < n; l++) {
            int somme = 0;
            for (int i = k; i <= l; i++) {
                somme += T[i];
            }
            max_somme = max(max_somme, somme);
        }
    }
    
    return max_somme;
}

// Algorithme moins naïf - O(n²)
int algorithmeMoinsNaif(const vector<int>& T) {
    int n = T.size();
    int max_somme = T[0];
    
    for (int k = 0; k < n; k++) {
        int somme = 0;
        for (int l = k; l < n; l++) {
            somme += T[l];
            max_somme = max(max_somme, somme);
        }
    }
    
    return max_somme;
}

// Algorithme diviser pour régner - O(n log n)

int maxSousSequenceTraversant(const vector<int>& T, int debut, int milieu, int fin) {
    // Partie gauche maximale se terminant au milieu
    int somme = 0;
    int max_gauche = T[milieu];
    
    for (int i = milieu; i >= debut; i--) {
        somme += T[i];
        max_gauche = max(max_gauche, somme);
    }
    
    // Partie droite maximale commençant juste après le milieu
    somme = 0;
    int max_droite = 0; // Peut être 0 si la partie droite est vide ou négative
    
    for (int i = milieu + 1; i <= fin; i++) {
        somme += T[i];
        max_droite = max(max_droite, somme);
    }
    
    return max_gauche + max_droite;
}

int diviserPourRegner(const vector<int>& T, int debut, int fin) {
    if (debut == fin) {
        return T[debut];
    }
    
    int milieu = (debut + fin) / 2;
    
    // Cas 1: Sous-séquence maximale dans la partie gauche
    int max_gauche = diviserPourRegner(T, debut, milieu);
    
    // Cas 2: Sous-séquence maximale dans la partie droite
    int max_droite = diviserPourRegner(T, milieu + 1, fin);
    
    // Cas 3: Sous-séquence maximale traversant le milieu
    int max_traverse = maxSousSequenceTraversant(T, debut, milieu, fin);
    
    // Retour du maximum des trois cas
    return max({max_gauche, max_droite, max_traverse});
}

int algorithmeDiviserPourRegner(const vector<int>& T) {
    return diviserPourRegner(T, 0, T.size() - 1);
}

// Algorithme incrémental - O(n)
int algorithmeIncremental(const vector<int>& T) {
    int n = T.size();
    int max_global = T[0];
    int max_courant = T[0];
    
    for (int i = 1; i < n; i++) {
        max_courant = max(T[i], max_courant + T[i]);
        max_global = max(max_global, max_courant);
    }
    
    return max_global;
}

// Génération de données aléatoires
vector<int> genererDonneesAleatoires(int n, int min_val, int max_val) {
    vector<int> T(n);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(min_val, max_val);
    
    for (int i = 0; i < n; i++) {
        T[i] = dis(gen);
    }
    
    return T;
}

// Validation des résultats des algorithmes
bool verifierResultats(const vector<int>& T) {
    int res1 = algorithmeNaif(T);
    int res2 = algorithmeMoinsNaif(T);
    int res3 = algorithmeDiviserPourRegner(T);
    int res4 = algorithmeIncremental(T);
    
    return (res1 == res2) && (res2 == res3) && (res3 == res4);
}