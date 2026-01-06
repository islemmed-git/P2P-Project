# 📁 Projet P2P – Ingénierie des réseaux Tout IP

## 🎓 Présentation

Ce projet a été réalisé dans le cadre du module **Ingénierie des réseaux Tout IP**.  
Il s’agit d’une implémentation d’un **système de partage de fichiers Peer-to-Peer (P2P)** reposant sur :

- un **serveur central** pour l’authentification simplifiée et la recherche,
- des **pairs** capables de partager et de télécharger des fichiers directement entre eux.

Le projet est volontairement **simple et pédagogique** afin d’illustrer les concepts réseaux.

---

## 👥 Répartition du travail

Islem : serveur central + serveur FTP

Akram : client FTP

---

## 👥 Ordre d’exécution

1️⃣ Lancer le serveur central

    python central_server.py

2️⃣ Lancer le serveur FTP

    python ftp_server.py

3️⃣ Enregistrer le fichier auprès du serveur central

    python register_file.py

4️⃣ Lancer le client

    python ftp_client.py

---

## 🧠 Principe de fonctionnement

Le système repose sur **trois rôles logiques** :

### 1️⃣ Serveur central

- Gère l’enregistrement des fichiers partagés
- Effectue la recherche par mots-clés
- Retourne l’IP et le port du pair qui possède le fichier
- **Ne stocke aucun fichier**

### 2️⃣ Serveur FTP (pair fournisseur)

- Héberge les fichiers partagés
- Envoie les fichiers aux autres pairs (download uniquement)

### 3️⃣ Client FTP (pair client)

- Recherche un fichier via le serveur central
- Télécharge le fichier directement depuis le pair fournisseur

👉 **Le transfert des fichiers ne passe jamais par le serveur central.**

---

## 🧩 Architecture logique

                     Islem
        ┌─────────────────────────┐
        │ Serveur central (PC1)   │
        │ - Recherche             │
        │ - Annuaire              │
        │                         │
        │ Serveur FTP (PC2)       │
        │ - Partage du fichier   │
        └──────────▲─────────────┘
                   │
        Résultat (IP + fichier)
                   │
        ┌──────────┴──────────┐
        │        Akram        │
        │ Client FTP (PC3)   │
        │ - Recherche        │
        │ - Téléchargement   │
        └───────────────────┘

---

## 📁 Organisation du projet

p2p_project/

- central_server.py # Serveur central
- ftp_server.py # Serveur FTP (partage)
- register_file.py # Enregistrement du fichier
- ftp_client.py # Client FTP
- Ingénierie des réseaux tout IP.pdf

---

## ⚙️ Prérequis

- Python 3.x
- Un ou deux ordinateurs
- Connexion réseau :
  - même Wi-Fi
  - ou même réseau local

---

## 🌐 Configuration réseau

Les machines doivent être **sur le même réseau**.

Exemple d’IP :

- Islem : `1.1.1.1`
- Akram : `1.1.1.2`

Test de connectivité :
ping IP_ISLEM
