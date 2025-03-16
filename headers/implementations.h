#ifndef IMPLEMENTATIONS_H
#define IMPLEMENTATIONS_H

#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Déclaration des algortihmes
int algorithmeNaif(const vector<int>&);
int algorithmeMoinsNaif(const vector<int>&);
int maxSousSequenceTraversant(const vector<int>&, int, int, int);
int diviserPourRegner(const vector<int>&, int, int);
int algorithmeDiviserPourRegner(const vector<int>&);
int algorithmeIncremental(const vector<int>&);


// Fonctions utilitaires
vector<int> genererDonneesAleatoires(int, int, int);

template <typename Func>
double mesurerTemps(Func&& func, const vector<int>& T) {
    auto start = high_resolution_clock::now();
    int resultat = func(T);
    auto end = high_resolution_clock::now();
    duration<double, milli> elapsed = end - start;
    return elapsed.count();
}

bool verifierResultats(const vector<int>&);

#endif // IMPLEMENTATIONS_H