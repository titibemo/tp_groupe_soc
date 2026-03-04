## Sujet de TP en groupe — Comparaison de méthodes de clustering sur données réelles (cybersécurité)

### Contexte professionnel

Vous travaillez pour une équipe **SOC (Security Operations Center)** chargée de surveiller l’activité réseau d’une entreprise.

L’équipe souhaite utiliser des techniques d’apprentissage non supervisé pour :

* identifier des comportements réseau typiques
* détecter des machines anormales
* repérer des activités suspectes
* comprendre la structure du trafic

Votre mission consiste à analyser un jeu de données réseau réel et à comparer plusieurs méthodes de **clustering** afin d’identifier différents profils d’activité.

---

# Jeu de données réel

Dataset : **UNSW-NB15 Network Intrusion Dataset**

Source officielle :

[https://research.unsw.edu.au/projects/unsw-nb15-dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset)

Une version facilement accessible est disponible sur Kaggle :

[https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15](https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15)

Ce dataset contient des enregistrements de trafic réseau simulant des communications normales et des attaques.

Variables importantes :

* dur : durée de la connexion
* proto : protocole réseau
* sbytes : nombre d’octets envoyés par la source
* dbytes : nombre d’octets envoyés par la destination
* sttl : TTL de la source
* dttl : TTL de la destination
* spkts : nombre de paquets source
* dpkts : nombre de paquets destination
* rate : taux de transfert

Chaque ligne correspond à **une connexion réseau**.

---

# Objectif du TP

Appliquer plusieurs méthodes de clustering afin de :

* identifier des profils de trafic réseau
* comparer les structures de clusters
* détecter les observations atypiques
* analyser les différences entre algorithmes

---

# Méthodes de clustering à comparer

Chaque groupe devra appliquer au minimum :

1. **K-Means**
2. **Clustering hiérarchique agglomératif (Ward)**
3. **DBSCAN**

---

# Organisation du TP

Les étudiants travaillent en groupes de 3 à 4 personnes.

Chaque groupe doit produire :

* une analyse exploratoire
* plusieurs modèles de clustering
* une comparaison argumentée
* une interprétation sécurité

---

# Partie 1 — Exploration des données

Objectifs :

1. Comprendre la structure du dataset.
2. Identifier les variables pertinentes pour le clustering.
3. Analyser les distributions des variables.
4. Détecter les valeurs extrêmes.

Questions :

* Pourquoi certaines variables doivent-elles être normalisées ?
* Pourquoi certaines variables catégorielles doivent être encodées ?

---

# Partie 2 — Préparation des données

Travail demandé :

1. Sélectionner un sous-ensemble de variables numériques pertinentes.
2. Appliquer une normalisation.
3. Réduire éventuellement la dimension des données (PCA).

Questions :

* Pourquoi la réduction de dimension peut-elle améliorer le clustering ?
* Quel pourcentage de variance doit être conservé ?

---

# Partie 3 — Application des méthodes de clustering

Chaque groupe doit appliquer les algorithmes suivants :

### K-Means

* déterminer le nombre de clusters optimal
* analyser les centres de clusters

### Clustering hiérarchique

* construire un dendrogramme
* déterminer un nombre de clusters pertinent

### DBSCAN

* choisir les paramètres epsilon et min_samples
* identifier les points considérés comme bruit

---

# Partie 4 — Comparaison des méthodes

Pour chaque méthode, analyser :

* nombre de clusters obtenus
* structure des clusters
* cohérence des groupes
* sensibilité aux paramètres

Utiliser des métriques comme :

* silhouette score
* distance intra-cluster
* distance inter-cluster

---

# Partie 5 — Interprétation métier

Pour chaque cluster identifié :

1. Décrire les caractéristiques du trafic.
2. Identifier s’il correspond à :

   * trafic normal
   * trafic volumineux
   * comportement atypique
3. Identifier les anomalies potentielles.

Questions :

* DBSCAN détecte-t-il des connexions suspectes ?
* Les clusters de K-Means correspondent-ils à des profils réseau ?

---

# Partie 6 — Analyse critique

Chaque groupe devra répondre aux questions suivantes :

1. Quelle méthode produit les clusters les plus cohérents ?
2. Quelle méthode est la plus robuste au bruit ?
3. Quelle méthode est la plus adaptée à la cybersécurité ?
4. Quelles limites observez-vous ?
