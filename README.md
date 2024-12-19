# Connexion entre le nrf9160 et nrf52840 dans le nordic thingy91 et connexion bluetooth

Ce programme permet de créer un pont de connectivité entre le nRF9160 et le nRF52840 sur le Thingy:91. Il facilite la réception des données via Bluetooth Low Energy (BLE). Grâce à ce bridge, vous pouvez facilement interagir avec les capteurs et les services fournis par le Thingy:91.

**Matériel nécessaire:**
- Thingy:91
- Câble micro USB
- nRF Connect for Desktop
- Visual Studio Code (VS Code)
- nRF Connect sur téléphone

**Installation et Configuration:**
Pour exécuter ce projet, vous devez installer et configurer le nRF Connect for Desktop et Visual Studio Code (VS Code). 

Note : Assurez-vous que la chaîne d'outils (Toolchain) et le SDK sont installés sur le disque C:\ de l'ordinateur, dans un dossier dédié. Le dossier contenant le code pour le Thingy:91 doit également être placé dans un dossier de programmation sur le disque C:\.

Suivez les étapes ci-dessous pour la configuration :
1. Installation des outils en ligne de commande nRF
  - Téléchargez et installez les nRF Command Line Tools depuis le lien suivant : https://www.nordicsemi.com/Products/Development-tools/nRF-Command-Line-Tools/Download.
  - Les nRF Command Line Tools incluent nrfjprog, un outil essentiel pour flasher le firmware sur vos kits de développement Nordic.

2. Installation de Visual Studio Code
  - Rendez-vous sur https://code.visualstudio.com/download et installez la version de VS Code correspondant à votre système d'exploitation.

3. Installation du nRF Connect Extension Pack dans VS Code
  - Dans la barre d'activités de VS Code, cliquez sur l'icône Extensions.
  - Recherchez nRF Connect for VS Code Extension Pack, puis cliquez sur Installer.

Le nRF Connect Extension Pack dans VS Code permet de :
  - Développer, créer, déboguer et déployer des applications embarquées basées sur le SDK nRF Connect.
  - Interagir avec le compilateur, l'éditeur de liens, le système de construction complet, un débogueur compatible RTOS, et le SDK nRF Connect.
  - Utiliser un éditeur visuel pour les fichiers Devicetree et un terminal série intégré.

4. Installation de la chaîne d'outils (Toolchain) sur VS Code
- Lors du premier lancement de l'extension nRF Connect for VS Code (cliquez sur l'extension dans la barre de gauche), vous serez invité à installer une Toolchain. Si aucune n'est détectée, procédez ainsi :
    - Cliquez sur Installer la Toolchain.
    - Choisissez une version compatible avec la version du SDK nRF Connect que vous utiliserez (la dernière version recommandée).
    - L'installation peut prendre quelques minutes.

5. Installation du SDK nRF Connect

Dans nRF Connect pour VS Code, cliquez sur Gérer le SDK.

Dans cette section, vous pourrez installer, désinstaller et sélectionner la version active du SDK.
- Cliquez sur Installer le SDK pour afficher les versions disponibles et choisir celle que vous souhaitez utiliser et installer la, le mieux est de sélectionner la dernière sans parenthèse.
- Une fois ces étapes terminées, votre environnement est prêt pour le développement avec le SDK nRF Connect et Visual Studio Code.


**Utilisation du code:**
1. Chargement du code
- Ouvrir VS Code
- Télécharger et décompresser le dossier, puis ouvrez le dossier contenant le code dans VS Code (thingy52840_connexion).

2. Build du code :
- Dans l'extension nRF Connect dans la barre d'activité, cliquez sur Add Build Configuration.
- Dans Board Target, choisissez thingy91_nrf52840.
- Cliquez sur Build Configuration et attendez la fin du processus de compilation.

**Envoi du code au Thingy:91:**
- Connectez la carte Thingy:91 à votre ordinateur via un câble micro-USB.
- Allumez la carte en appuyant sur le bouton SW1 puis en activant l'interrupteur ON/OFF.
![image](https://github.com/user-attachments/assets/ea1b6834-e06b-45cd-a242-337154133790)
- Ouvrez nRF Connect for Desktop, puis l'outil Programmer (à installer si nécessaire).
- Cliquez sur Select a Device et sélectionnez le Thingy:91 dans la liste.
- Dans Add File, cliquez sur Browse, allez dans le dossier du code > build/zephyr, et sélectionnez app_signed.hex.
- Cliquez ensuite sur Write, puis Write à nouveau dans la fenêtre de confirmation pour flasher le code.

**Connexion et réception des messages en BLE:**

Activer le Bluetooth sur le Thingy:91
- Branchez le Thingy:91 à votre ordinateur à l'aide du câble micro USB.
- Ouvrez le fichier Config situé dans la carte Thingy:91 dans le dossier qui s'ouvre lors du branchement.
- Modifiez la ligne BLE_ENABLED=0 en BLE_ENABLED=1.
- Sauvegardez les modifications.
- Éjectez proprement la carte Thingy:91 depuis votre ordinateur en allant dans l'affichage des icônes cachés et ejecter la carte branché sur le port USB.
- Débranchez le Thingy:91.
Le Bluetooth est maintenant activé sur votre Thingy:91.

**Utiliser nRF Connect pour Téléphone afin de lire les données:**
- Installez l'application "nRF Connect" si ce n'est pas déjà fait.
- Ouvrez nRF Connect sur votre téléphone.
- Cliquez sur le bouton Scan pour rechercher les appareils BLE à proximité.
- Filtrez les résultats en tapant thingy dans la barre de tri sous "Filter by name or address". Cela facilitera la localisation de votre appareil lors des prochaines connexions.
- Cliquez sur le bouton CONNECT de l'appareil nommé Thingy:91 UART.
- Vous êtes maintenant connecté à votre appareil.
- Pour lire les données, appuyez sur Nordic UART Service puis sur le symbole avec 3 flèches de téléchargement à côté de TX Characteristic.

**Extraction des données dans un fichier excel depuis les données reçues en BLE:**
- Dans nRF Connect sur téléphone, vérifiez que vous êtes bien connecté à l'appareil en BLE
- Cliquez sur Nordic UART Service puis les trois flèches
- Appuyez ensuite sur les 3 points en haut à droite puis Show log
- Dans la nouvelle page, cliquez sur enregistrez en bas (casette d'enregistrement), cela enregistrera un fichier txt
- Sauvegardez le fichier à un endroit auquel vous pouvez accéder puis envoyer vous ce fichier sur ordinateur
- Sur l'ordinateur, ouvrez le fichier "Extraction_Données_BLE" situé dans ce répertoire Github
- Faites le code avec Run > Run Without Debugging et choisir le débugger Python, vous devriez avoir une erreur
- Tapez la commande : pip install pandas
- Copier le chemin d'accès au fichier txt et écrivez le à la place de "chemin/accès/fichier.txt" en enlevant les guillemets et en laissant les apostrophes de base
- Créer un fichier excel sur le bureau et copiez le chemin d'accès à celui-ci puis écrivez la dans "chemin/accès/fichier_excel.xlxs" en enlevant les guillemets et en laissant les apostrophes de base
- Exécutez de nouveau le programme Python
- Vos données seront enregistrées dans le fichier xlxs pour du traitement de données
