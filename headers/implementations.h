#ifndef IMPLEMENTATIONS_H
#define IMPLEMENTATIONS_H

#include <vector>

using namespace std;

// Déclaration des algortihmes
int algorithmeNaif(const vector<int>& T);
int algorithmeMoinsNaif(const vector<int>& T);
int maxSousSequenceTraversant(const vector<int>& T, int debut, int milieu, int fin);
int diviserPourRegner(const vector<int>& T, int debut, int fin);
int algorithmeDiviserPourRegner(const vector<int>& T);
int algorithmeIncremental(const vector<int>& T);


// Fonctions utilitaires
vector<int> genererDonneesAleatoires(int n, int min_val, int max_val);
double mesurerTemps(Func&& func, const vector<int>& T);
bool verifierResultats(const vector<int>& T);

#endif // IMPLEMENTATIONS_H