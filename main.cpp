#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include "headers/implementations.h"
#include "header/implementations_matrices.h"

using namespace std;
using namespace std::chrono;


int main() {    
    // Création du fichier csv pour collecter les resultats
    ofstream fichier_resultat("resultats_performance.csv");
    fichier_resultat << "Taille,Naif(ms),MoinsNaif(ms),DiviserPourRegner(ms),Incremental(ms)" << endl;
    

    vector<int> tailles = {10, 50, 100, 500, 1000, 2000, 5000, 10000};
    
    for (int taille : tailles) {
        if (taille > 1000) {
            // Pour les grandes tailles, l'algorithme naïf ne sera pas executer
            cout << "Taille " << taille << "..." << endl;
            vector<int> donnees = genererDonneesAleatoires(taille, -100, 100);
            
            double temps_moins_naif = mesurerTemps(algorithmeMoinsNaif, donnees);
            double temps_diviser = mesurerTemps(algorithmeDiviserPourRegner, donnees);
            double temps_incremental = mesurerTemps(algorithmeIncremental, donnees);
            
            fichier_resultat << taille << ",N/A," << temps_moins_naif << "," 
                           << temps_diviser << "," << temps_incremental << endl;
        }
        else {
            cout << "Taille " << taille << "..." << endl;
            vector<int> donnees = genererDonneesAleatoires(taille, -100, 100);
            
            // Vérification des resultats identiques de tous les algorithmes
            if (!verifierResultats(donnees)) {
                cout << "Erreur: les algorithmes donnent des résultats différents!" << endl;
                return 1;
            }
            
            double temps_naif = mesurerTemps(algorithmeNaif, donnees);
            double temps_moins_naif = mesurerTemps(algorithmeMoinsNaif, donnees);
            double temps_diviser = mesurerTemps(algorithmeDiviserPourRegner, donnees);
            double temps_incremental = mesurerTemps(algorithmeIncremental, donnees);
            
            fichier_resultat << taille << "," << temps_naif << "," << temps_moins_naif << "," 
                           << temps_diviser << "," << temps_incremental << endl;
        }
    }
    
    fichier_resultat.close();
    cout << "Mesures de performance terminées. Résultats sauvegardés dans 'resultats_performance.csv'" << endl;



    // Exemple d'utilisation avec une petite matrice
    vector<vector<int>> matrix = {
        {1, -2, -1, 4},
        {-8, 3, 8, -2},
        {2, -4, 6, 1},
        {-1, 1, -7, 3}
    };
    
    cout << "Sous-matrice maximale (Incrementale): " << sousMatiiceMaximale(matrix) << endl;
    cout << "Sous-matrice maximale (Naive): " << sousMatriceMaximaleNaive(matrix) << endl;
    cout << "Sous-matrice maximale (Moins Naive): " << sousMatriceMaximaleMoinsNaive(matrix) << endl;
    
    return 0;
}