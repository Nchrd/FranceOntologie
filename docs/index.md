Cette documentation présente une ontologie conçue pour modéliser les entités gouvernementales en France. L'objectif de cette ontologie est de fournir une structure claire et cohérente pour représenter les différentes entités gouvernementales, leurs relations et leurs responsabilités.

### Que Contient cette Ontologie ?

L'ontologie gouvernementale comprend les principales classes d'entités gouvernementales, telles que les ministères, les secrétariats et les services déconcentrés. Elle définit également les propriétés et les relations entre ces entités, permettant de modéliser des hiérarchies et des responsabilités complexes.

### Comment Utiliser cette Documentation ?

Cette documentation est organisée en plusieurs sections :
- **Classes** : Décrit les différentes classes d'entités gouvernementales.
- **Propriétés** : Décrit les propriétés et les relations entre les entités.

### Contribuer

Cette ontologie est un travail en cours et nous encourageons les contributions de la communauté. Si vous avez des suggestions, des corrections ou des améliorations, n'hésitez pas à ouvrir une issue ou à soumettre une pull request sur le dépôt GitHub.

Nous espérons que cette documentation vous sera utile pour comprendre et utiliser l'ontologie gouvernementale. Bonne lecture !

---

# Classes

## C1 : Entité {#c1_Entite}

**Nom complet :** Entité

> Cette classe comprend toutes les autres classes de cette ontologie. Elle est la racine de tout et est la classe mère de toutes les classes par héritage.

**Classe mère :** Aucune

**Classes filles :**
- [C2 : Ministère](#c2_Ministere)
- [C3 : Direction Centrale](#c3_Direction_Centrale)
- [C4 : Administration Publique](#c4_Administration_Publique)
- [C5 : Entreprise publique](#c5_Entreprise_Publique)

**Propriétés :**
- [P1 : Administre](#p1_Administre) &rarr; [C1 : Entité](#c1_Entite)
- [P2 : Possède](#p2_Possede) &rarr; [C5 : Entreprise publique](#c5_Entreprise_Publique)

---

## C2 : Ministère {#c2_Ministere}

**Nom complet :** Ministère

> Classe regroupant tous les ministères.

**Classe mère :** [C1 : Entité](#c1_Entite)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C3 : Direction Centrale {#c3_Direction_Centrale}

**Nom complet :** Direction Centrale

> Classe regroupant toutes les entités agissant à l'échelle nationale et qui dépendent d'un ministère.

**Classe mère :** [C1 : Entité](#c1_Entite)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C4 : Administration Publique {#c4_Administration_Publique}

**Nom complet :** Administration Publique

> Classe regroupant toutes les administrations publiques, quelles que soient leur échelle.

**Classe mère :** [C1 : Entité](#c1_Entite)

**Classes filles :**
- [C6 : ODAC](#c6_ODAC)
- [C7 : APUL](#c7_APUL)
- [C8 : ASSO](#c8_ASSO)
- [C9 : SCN](#c9_SCN)
- [C15 : GIP](#c15_GIP)

**Propriétés :** Aucune

---

## C5 : Entreprise publique {#c5_Entreprise_Publique}

**Nom complet :** Entreprise publique

> Classe regroupant toutes les entreprises publiques.

**Classe mère :** [C1 : Entité](#c1_Entite)

**Classes filles :** Aucune

**Propriétés :** 
- [P2 : Possède](#p2_Possede) &rarr; [C5 : Entreprise publique](#c5_Entreprise_Publique)

---

## C6 : ODAC {#c6_ODAC}

**Nom complet :** Organisme Divers d'Administration Centrale

> Classe regroupant toutes les ODAC, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4_Administration_Publique)

**Classes filles :**
- [C10 : EPIC](#c10_EPIC)
- [C11 : EPA](#c11_EPA)
- [C12 : AAI](#c12_AAI)

**Propriétés :** Aucune

---

## C7 : APUL {#c7_APUL}

**Nom complet :** Administration Publique Locale

> Classe regroupant toutes les APUL, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4_Administration_Publique)

**Classes filles :**
- [C13 : Administration Territoriale](#c13_Administration_Territoriale)
- [C14 : Administration Locale Diverse](#c14_Administration_Locale_Diverse)

**Propriétés :** Aucune

---

## C8 : ASSO {#c8_ASSO}

**Nom complet :** Administration de Sécurité Sociale

> Classe regroupant toutes les Administrations de Sécurité Sociale, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4_Administration_Publique)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C9 : SCN {#c9_SCN}

**Nom complet :** Service à Compétence Nationale

> Classe regroupant tous les Services à Compétence Nationale, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4_Administration_Publique)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C10 : EPIC {#c10_EPIC}

**Nom complet :** Établissement Public à Caractère Industriel et Commercial

> Classe regroupant toutes les EPIC, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6_ODAC)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C11 : EPA {#c11_EPA}

**Nom complet :** Établissement Public à Caractère Administratif

> Classe regroupant toutes les EPA, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6_ODAC)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C12 : AAI {#c12_AAI}

**Nom complet :** Autorité Administrative Indépendante

> Classe regroupant toutes les AAI, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6_ODAC)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C13 : Administration Territoriale {#c13_Administration_Territoriale}

**Nom complet :** Administration Territoriale

> Classe regroupant toutes les Administrations Territoriales, qui sont un type d'APUL.

**Classe mère :** [C7 : APUL](#c7_APUL)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C14 : Administration Locale Diverse {#c14_Administration_Locale_Diverse}

**Nom complet :** Administration Locale Diverse

> Classe regroupant toutes les Administrations Territoriales autres que les APUL.

**Classe mère :** [C7 : APUL](#c7_APUL)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C15 : GIP {#c15_GIP}

**Nom complet :** Groupement d'Intérêt public

> Classe regroupant tous les Groupements d'Intérets Publics

**Classe mère :** [C4 : Administration publique](#c4_Administration_Publique)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

# Propriétés

## P1 : Administre {#p1_Administre}

**Nom complet :** Administre

> Relation de dépendance entre deux entités.

**Domaine :** [C1 : Entité](#c1_Entite)

**Portée :** [C1 : Entité](#c1_Entite)

---

## P2 : Possède {#p2_Possede}

**Nom complet :** Possède

> Relation de possession entre une entité et une entreprise publique.

**Domaine :** [C1 : Entité](#c1_Entite)

**Portée :** [C5 : Entreprise publique](#c5_Entreprise_Publique)

