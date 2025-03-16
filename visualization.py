import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Style pour les graphiques
plt.style.use('ggplot')
sns.set_palette("colorblind")

# Données de performances
tailles = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
temps_naif = [0.0017, 0.0991, 0.6565, 76.3935, 448.165, None, None, None]
temps_moins_naif = [0.0007, 0.0092, 0.0331, 0.9146, 2.4811, 9.6442, 64.599, 260.182]
temps_diviser = [0.0011, 0.0078, 0.013, 0.0597, 0.1166, 0.2434, 0.6773, 1.3166]
temps_incremental = [0.0003, 0.0009, 0.0017, 0.0052, 0.0098, 0.0185, 0.0456, 0.0885]

# DataFrame
df = pd.DataFrame({
    'Taille': tailles,
    'Naïf': temps_naif,
    'Moins Naïf': temps_moins_naif,
    'Diviser pour Régner': temps_diviser,
    'Incrémental': temps_incremental
})

# 1. Graphique linéaire de comparaison de tous les algorithmes
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:
    valid_data = df[['Taille', col]].dropna()
    if not valid_data.empty:
        plt.plot(valid_data['Taille'], valid_data[col], marker='o', linewidth=2, label=col)

plt.title('Comparaison des temps d\'exécution', fontsize=15)
plt.xlabel('Taille du tableau (n)', fontsize=12)
plt.ylabel('Temps d\'exécution (ms)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('visualization/comparaison_lineaire.png', dpi=300, bbox_inches='tight')

# 2. Graphique logarithmique pour mieux visualiser les différences
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:
    valid_data = df[['Taille', col]].dropna()
    if not valid_data.empty:
        plt.loglog(valid_data['Taille'], valid_data[col], marker='o', linewidth=2, label=col)

plt.title('Comparaison des temps d\'exécution (échelle logarithmique)', fontsize=15)
plt.xlabel('Taille du tableau (n)', fontsize=12)
plt.ylabel('Temps d\'exécution (ms)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('visualization/comparaison_log.png', dpi=300, bbox_inches='tight')

# 3. Graphique des ratios de croissance pour confirmer les complexités
# Calcul des ratios lorsque n double
tailles_pairs = [(tailles[i], tailles[i+1]) for i in range(len(tailles)-1) if tailles[i+1] == 2*tailles[i]]
indices_pairs = [(i, i+1) for i in range(len(tailles)-1) if tailles[i+1] == 2*tailles[i]]

# Fonctions de complexité théoriques
def ratio_o_n(n1, n2):
    return n2/n1  # Devrait être environ 2

def ratio_o_nlogn(n1, n2):
    return (n2*np.log2(n2))/(n1*np.log2(n1))  # Devrait être légèrement supérieur à 2

def ratio_o_n2(n1, n2):
    return (n2**2)/(n1**2)  # Devrait être environ 4

def ratio_o_n3(n1, n2):
    return (n2**3)/(n1**3)  # Devrait être environ 8

# Calcul des ratios réels et théoriques
ratios_data = []
for idx, (i, j) in enumerate(indices_pairs):
    n1, n2 = tailles[i], tailles[j]
    
    # Ratios théoriques
    r_th_n = ratio_o_n(n1, n2)
    r_th_nlogn = ratio_o_nlogn(n1, n2)
    r_th_n2 = ratio_o_n2(n1, n2)
    r_th_n3 = ratio_o_n3(n1, n2)
    
    # Ratios réels
    r_incr = temps_incremental[j]/temps_incremental[i] if temps_incremental[i] and temps_incremental[j] else None
    r_div = temps_diviser[j]/temps_diviser[i] if temps_diviser[i] and temps_diviser[j] else None
    r_moins_naif = temps_moins_naif[j]/temps_moins_naif[i] if temps_moins_naif[i] and temps_moins_naif[j] else None
    r_naif = temps_naif[j]/temps_naif[i] if (i < len(temps_naif) and j < len(temps_naif) and 
                                             temps_naif[i] and temps_naif[j]) else None
    
    ratios_data.append({
        'Paire': f"{n1}-{n2}",
        'O(n)': r_th_n,
        'O(n log n)': r_th_nlogn,
        'O(n²)': r_th_n2,
        'O(n³)': r_th_n3,
        'Incrémental': r_incr,
        'Diviser pour Régner': r_div,
        'Moins Naïf': r_moins_naif,
        'Naïf': r_naif
    })

ratios_df = pd.DataFrame(ratios_data)

# Graphique des ratios de croissance
plt.figure(figsize=(12, 7))
positions = np.arange(len(ratios_df['Paire']))
width = 0.15

# Traçage des barres pour chaque algorithme et complexité théorique
plt.bar(positions - 2*width, ratios_df['Incrémental'], width, label='Incrémental (mesuré)')
plt.bar(positions - width, ratios_df['Diviser pour Régner'], width, label='Diviser pour Régner (mesuré)')
plt.bar(positions, ratios_df['Moins Naïf'], width, label='Moins Naïf (mesuré)')
plt.bar(positions + width, ratios_df['Naïf'], width, label='Naïf (mesuré)')

# Ajout des lignes pour les complexités théoriques
plt.axhline(y=2, color='green', linestyle='-', label='O(n) théorique')
plt.axhline(y=ratios_df['O(n log n)'].mean(), color='blue', linestyle='--', label='O(n log n) théorique')
plt.axhline(y=4, color='orange', linestyle='-.', label='O(n²) théorique')
plt.axhline(y=8, color='red', linestyle=':', label='O(n³) théorique')

plt.xlabel('Paires de tailles n₁-n₂', fontsize=12)
plt.ylabel('Ratio de temps d\'exécution T(n₂)/T(n₁)', fontsize=12)
plt.title('Ratios de croissance lorsque la taille n double', fontsize=15)
plt.xticks(positions, ratios_df['Paire'])
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('visualization/ratios_croissance.png', dpi=300, bbox_inches='tight')

# 4. Visualisation du problème de sous-séquence maximale
# Exemple de tableau avec sous-séquence maximale
exemple_tableau = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sous_seq_max = [4, -1, 2, 1]  # La sous-séquence maximale dans cet exemple

plt.figure(figsize=(12, 5))
bars = plt.bar(range(len(exemple_tableau)), exemple_tableau, color=['gray']*3 + ['blue']*4 + ['gray']*2)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.title('Illustration d\'une sous-séquence maximale', fontsize=15)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Valeur', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mise en évidence de la sous-séquence maximale
for i in range(3, 7):
    bars[i].set_color('blue')
    
# Ajout d'une annotation
plt.annotate('Sous-séquence maximale\nsomme = 6', xy=(5, 2), xytext=(5, 3.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             ha='center', fontsize=10)

plt.savefig('visualization/illustration_probleme.png', dpi=300, bbox_inches='tight')

# 5. Visualisation de l'algorithme de Kadane
# Exemple montrant l'évolution de max_courant et max_global
exemple_tableau = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_courant = [-2, 1, -2, 4, 3, 5, 6, 1, 5]  # Valeurs calculées par l'algorithme
max_global = [-2, 1, 1, 4, 4, 5, 6, 6, 6]    # Valeurs calculées par l'algorithme

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Traçage du tableau original
ax1.bar(range(len(exemple_tableau)), exemple_tableau, color='lightgray')
ax1.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax1.set_title('Tableau original', fontsize=12)
ax1.set_ylabel('Valeur')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Traçage de l'évolution de max_courant
ax2.plot(range(len(max_courant)), max_courant, marker='o', color='blue', linewidth=2)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax2.set_title('Évolution de max_courant', fontsize=12)
ax2.set_ylabel('Valeur')
ax2.grid(True, linestyle='--', alpha=0.7)

# Traçage de l'évolution de max_global
ax3.plot(range(len(max_global)), max_global, marker='o', color='green', linewidth=2)
ax3.axhline(y=0, color='black', linestyle='-', alpha=0.3)
ax3.set_title('Évolution de max_global', fontsize=12)
ax3.set_xlabel('Index')
ax3.set_ylabel('Valeur')
ax3.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('visualization/illustration_kadane.png', dpi=300, bbox_inches='tight')

# 6. Visualisation de l'approche diviser pour régner
plt.figure(figsize=(12, 8))

# Fonction pour dessiner un rectangle représentant une partie du tableau
def draw_array_section(ax, start, end, level, label, color='lightgray'):
    height = 0.8
    rect = plt.Rectangle((start, level-height/2), end-start, height, 
                         facecolor=color, alpha=0.6, edgecolor='black')
    ax.add_patch(rect)
    ax.text((start+end)/2, level, label, ha='center', va='center', fontsize=10)

# Visualisation de l'approche diviser pour régner
tableau_taille = 8
ax = plt.gca()
ax.set_xlim(0, tableau_taille)
ax.set_ylim(0, 6)

# Niveau 0: tableau complet
draw_array_section(ax, 0, tableau_taille, 5, "Tableau complet [0-7]")

# Niveau 1: division en deux
draw_array_section(ax, 0, tableau_taille/2, 4, "Moitié gauche [0-3]", 'lightblue')
draw_array_section(ax, tableau_taille/2, tableau_taille, 4, "Moitié droite [4-7]", 'lightgreen')

# Niveau 2: division en quatre
draw_array_section(ax, 0, tableau_taille/4, 3, "[0-1]", 'lightblue')
draw_array_section(ax, tableau_taille/4, tableau_taille/2, 3, "[2-3]", 'lightblue')
draw_array_section(ax, tableau_taille/2, 3*tableau_taille/4, 3, "[4-5]", 'lightgreen')
draw_array_section(ax, 3*tableau_taille/4, tableau_taille, 3, "[6-7]", 'lightgreen')

# Niveau 3: division finale
draw_array_section(ax, 0, 1, 2, "[0]", 'lightblue')
draw_array_section(ax, 1, 2, 2, "[1]", 'lightblue')
draw_array_section(ax, 2, 3, 2, "[2]", 'lightblue')
draw_array_section(ax, 3, 4, 2, "[3]", 'lightblue')
draw_array_section(ax, 4, 5, 2, "[4]", 'lightgreen')
draw_array_section(ax, 5, 6, 2, "[5]", 'lightgreen')
draw_array_section(ax, 6, 7, 2, "[6]", 'lightgreen')
draw_array_section(ax, 7, 8, 2, "[7]", 'lightgreen')

# Cas de traversée du milieu
draw_array_section(ax, tableau_taille/2-1, tableau_taille/2+1, 1, "Traversant", 'orange')

# Supprimer les axes
ax.axis('off')
plt.title('Visualisation de l\'approche diviser pour régner', fontsize=15)

# Ajout des flèches pour montrer la phase de combinaison
plt.arrow(1, 2, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(3, 2, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(5, 2, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(7, 2, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')

plt.arrow(1.5, 1, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(3.5, 1, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(5.5, 1, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
plt.arrow(7.5, 1, 0, -0.5, head_width=0.1, head_length=0.1, fc='black', ec='black')

# Ajout d'une annotation explicative
plt.text(4, 0.2, "La solution finale est le maximum entre:\n1. La solution de la moitié gauche\n2. La solution de la moitié droite\n3. La solution traversant le milieu", 
         ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'))

plt.savefig('illustration_diviser_pour_regner.png', dpi=300, bbox_inches='tight')

# 7. Visualisation du problème pour les matrices

# Matrice d'exemple
matrice_exemple = np.array([
    [1, -2, -1, 4],
    [-8, 3, 8, -2],
    [2, -4, 6, 1],
    [-1, 1, -7, 3]
])

# Sous-matrice maximale
sous_matrice_max_coords = [(1, 1), (1, 2), (2, 1), (2, 2)]  # Coordonnées (i, j)

plt.figure(figsize=(8, 6))
ax = plt.gca()
im = ax.imshow(matrice_exemple, cmap='coolwarm')

# Ajout d'une barre de couleur
cbar = plt.colorbar(im)
cbar.set_label('Valeur')

# Ajout des valeurs dans les cellules
for i in range(matrice_exemple.shape[0]):
    for j in range(matrice_exemple.shape[1]):
        text_color = 'white' if abs(matrice_exemple[i, j]) > 5 else 'black'
        ax.text(j, i, matrice_exemple[i, j], ha='center', va='center', color=text_color)

# Mise en évidence de la sous-matrice maximale
for i, j in sous_matrice_max_coords:
    rect = plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=False, edgecolor='lime', linewidth=3)
    ax.add_patch(rect)

# Ajout d'une annotation
plt.title('Illustration du problème de sous-matrice maximale', fontsize=15)
plt.annotate('Sous-matrice maximale\nsomme = 13', xy=(1.5, 1.5), xytext=(3, 0),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             ha='center', fontsize=10)

plt.savefig('visualization/illustration_matrices.png', dpi=300, bbox_inches='tight')

print("Tous les graphiques ont été générés avec succès!")