# Problème des sous-séquences maximales

Ce projet analyse et compare plusieurs algorithmes de résolution du problème des sous-séquences maximales, en évaluant leur complexité, leurs performances pratiques et leur applicabilité à divers contextes. Il s'agit d'un problème fondamental en informatique avec des applications dans de nombreux domaines allant des finances à l'analyse de séries temporelles.

## 📌 Description du projet
Le problème des sous-séquences maximales consiste à trouver la sous-séquence contiguë d'un tableau d'entiers ayant la plus grande somme possible. Ce problème se retrouve dans des applications telles que la finance, où il sert à identifier les périodes les plus rentables dans une série de transactions, ou encore dans le traitement du signal, où il permet de détecter des changements significatifs dans les données.

## 📊 Algorithmes implémentés
Ce projet étudie et compare **quatre algorithmes** différents, chacun avec ses propres avantages et limitations :

1. **🔹 Algorithme Naïf (O(n³))** : Explore toutes les sous-séquences possibles. Très lent mais intuitif.
2. **🔹 Algorithme Moins Naïf (O(n²))** : Optimise le premier en évitant le recalcul redondant des sommes.
3. **🔹 Algorithme Diviser pour Régner (O(n log n))** : Divise le problème en sous-problèmes récursifs et combine leurs solutions.
4. **🔹 Algorithme Incrémental (O(n))** : Utilise une approche dynamique pour mettre à jour la somme maximale en parcourant le tableau une seule fois.

## 🛠️ Implémentation
L'implémentation est réalisée en **C++** et comprend :
- ✅ Les **algorithmes** avec des tests unitaires.
- ✅ Un **générateur de données aléatoires** pour simuler des entrées réalistes.
- ✅ Un **outil de mesure des performances** basé sur `std::chrono`.
- ✅ Une **validation des résultats** avec des jeux de test variés.
- ✅ Un **script Python** pour visualiser les performances à travers des graphiques.

## 📂 Fichiers du projet
```
 📁 projet-sous-sequences-maximales
 ├── 📁 header
 │   ├── implementations.h  -> Contient les fonctions nécessaires.
 |   ├── implementations_matrices.h -> Contient les fonctions nécessaires pour les matrices 2D.
 ├── 📁 src
 │   ├── 🖥️implementations.cpp  -> Contient l'implémentation des algorithmes.
 │   ├── implementations_matrices.cpp -> Contient l'implémentation des algorithmes adaptées aux matrices 2D.
 ├── 📁 visualization -> Contient les visuels générés par le script python
 ├── 🔬main.cpp  > Gère les tests et la mesure des performances.
 ├── 📊 results.csv  -> Contient les résultats des tests de performances.
 ├── 📈 visualization.py  -> Script Python pour l'analyse des performances.
 ├── 📝 README.md  -> Ce fichier
```

## 🚀 Installation et Exécution
### 🔧 Prérequis
- Un **compilateur C++** (GCC, Clang, MSVC...)
- **Python** (pour la visualisation des données)

### 🔨 Compilation
```sh
g++ -o main main.cpp src/implementations.cpp src/implementations_matrices.cpp -I header/ -std=c++11
```

### ▶️ Exécution
```sh
./main
```

### 📊 Analyse des résultats
```sh
python visualization.py
```

## ⚡ Comparaison des performances
Les tests sont effectués sur des entrées de tailles croissantes et les temps d'exécution sont enregistrés dans `results.csv`. 

📌 **Observations principales :**
- 🟢 **L'algorithme incrémental (O(n))** est **le plus performant**.
- 🔴 **L'algorithme naïf (O(n³))** devient rapidement impraticable.
- 📈 **Les performances sont illustrées** avec des graphiques dans `visualization.py`.

## 🎯 Applications possibles
📌 **Ce projet peut être appliqué dans différents domaines :**
- 💰 **Finance** : Identification des périodes les plus rentables dans des séries de transactions.
- 🔬 **Traitement du signal** : Détection des variations significatives dans des données séquentielles.
- 🧬 **Biologie computationnelle** : Analyse de séquences génomiques pour détecter des motifs intéressants.
- 🔧 **Optimisation** : Résolution de problèmes de maximisation dans divers contextes.

## 👤 Auteur
👨‍💻 **Paul Christopher AIMÉ**


## 📜 Licence
📝 **Ce projet est sous licence MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer selon les termes de cette licence.