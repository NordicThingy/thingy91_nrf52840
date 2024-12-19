import pandas as pd
import re

# Chemin du fichier texte
file_path = r'C:\Users\Gwénaël\OneDrive\Bureau\BUT\Projet_nordic\test nrf connect.txt'

# Liste pour stocker les données extraites
data = []

# Variables temporaires pour stocker les valeurs de x, y, z, T, P, H
x, y, z, T, P, H = None, None, None, None, None, None

# Ouvrir le fichier et lire ligne par ligne
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Lire chaque ligne et extraire les valeurs
for line in lines:
    # Extraire les valeurs de x, y, z
    if 'x =' in line:
        match = re.search(r'x\s=\s+([-\d.]+)', line)
        if match:
            x = float(match.group(1))
    if 'y =' in line:
        match = re.search(r'y\s=\s+([-\d.]+)', line)
        if match:
            y = float(match.group(1))
    if 'z =' in line:
        match = re.search(r'z\s=\s+([-\d.]+)', line)
        if match:
            z = float(match.group(1))
    # Extraire la température (T), la pression (P) et l'humidité (H)
    if 'T:' in line:
        match = re.search(r'T:\s([\d.]+)', line)
        if match:
            T = float(match.group(1))
    if 'P:' in line:
        match = re.search(r'P:\s([\d.]+)', line)
        if match:
            P = float(match.group(1))
    if 'H:' in line:
        match = re.search(r'H:\s([\d.]+)', line)
        if match:
            H = float(match.group(1))
    # Ajouter les données complètes à la liste une fois tous les champs collectés
    if x is not None and y is not None and z is not None and T is not None and P is not None and H is not None:
        data.append({'x': x, 'y': y, 'z': z, 'T': T, 'P': P, 'H': H})
        # Réinitialiser les variables pour le prochain paquet
        x, y, z, T, P, H = None, None, None, None, None, None

# Convertir les données en DataFrame
df = pd.DataFrame(data)

# Afficher le DataFrame ou l'enregistrer en fichier Excel
print(df)

# Sauvegarder les données dans un fichier Excel
output_file = r'C:\Users\Gwénaël\OneDrive\Bureau\BUT\Projet_nordic\données_extraites_BLE.xlsx'
df.to_excel(output_file, index=False)
print(f"Les données ont été sauvegardées dans {output_file}.")