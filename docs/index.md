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

## C1 : Entité

**Nom complet :** Entité

> Cette classe comprend toutes les autres classes de cette ontologie. Elle est la racine de tout et est la classe mère de toutes les classes par héritage.

**Classe mère :** Aucune

**Classes filles :**
- [C2 : Ministère](#c2--ministère)
- [C3 : Direction Centrale](#c3--direction-centrale)
- [C4 : Administration Publique](#c4--administration-publique)
- [C5 : Entreprise publique](#c5--entreprise-publique)

**Propriétés :**
- [P1 : Administre](#p1--administre) &rarr; [C1 : Entité](#c1--entité)
- [P2 : Possède](#p2--possède) &rarr; [C5 : Entreprise publique](#c5--entreprise-publique)

---

## C2 : Ministère

**Nom complet :** Ministère

> Classe regroupant tous les ministères.

**Classe mère :** [C1 : Entité](#c1--entité)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C3 : Direction Centrale

**Nom complet :** Direction Centrale

> Classe regroupant toutes les entités agissant à l'échelle nationale et qui dépendent d'un ministère.

**Classe mère :** [C1 : Entité](#c1--entité)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C4 : Administration Publique

**Nom complet :** Administration Publique

> Classe regroupant toutes les administrations publiques, quelles que soient leur échelle.

**Classe mère :** [C1 : Entité](#c1--entité)

**Classes filles :**
- [C6 : ODAC](#c6--odac)
- [C7 : APUL](#c7--apul)
- [C8 : ASSO](#c8--asso)
- [C9 : SCN](#c9--scn)

**Propriétés :** Aucune

---

## C5 : Entreprise publique

**Nom complet :** Entreprise publique

> Classe regroupant toutes les entreprises publiques.

**Classe mère :** [C1 : Entité](#c1--entité)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C6 : ODAC

**Nom complet :** Organisme Divers d'Administration Centrale

> Classe regroupant toutes les ODAC, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4--administration-publique)

**Classes filles :**
- [C10 : EPIC](#c10--epic)
- [C11 : EPA](#c11--epa)
- [C12 : AAI](#c12--aai)

**Propriétés :** Aucune

---

## C7 : APUL

**Nom complet :** Administration Publique Locale

> Classe regroupant toutes les APUL, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4--administration-publique)

**Classes filles :**
- [C13 : Administration Territoriale](#c13--administration-territoriale)
- [C14 : Administration Locale Diverse](#c14--administration-locale-diverse)

**Propriétés :** Aucune

---

## C8 : ASSO

**Nom complet :** Administration de Sécurité Sociale

> Classe regroupant toutes les Administrations de Sécurité Sociale, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4--administration-publique)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C9 : SCN

**Nom complet :** Service à Compétence Nationale

> Classe regroupant tous les Services à Compétence Nationale, qui sont un type d'administration publique.

**Classe mère :** [C4 : Administration Publique](#c4--administration-publique)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C10 : EPIC

**Nom complet :** Établissement Public à Caractère Industriel et Commercial

> Classe regroupant toutes les EPIC, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6--odac)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C11 : EPA

**Nom complet :** Établissement Public à Caractère Administratif

> Classe regroupant toutes les EPA, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6--odac)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C12 : AAI

**Nom complet :** Autorité Administrative Indépendante

> Classe regroupant toutes les AAI, qui sont un type d'ODAC.

**Classe mère :** [C6 : ODAC](#c6--odac)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C13 : Administration Territoriale

**Nom complet :** Administration Territoriale

> Classe regroupant toutes les Administrations Territoriales, qui sont un type d'APUL.

**Classe mère :** [C7 : APUL](#c7--apul)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

## C14 : Administration Locale Diverse

**Nom complet :** Administration Locale Diverse

> Classe regroupant toutes les Administrations Territoriales autres que les APUL.

**Classe mère :** [C7 : APUL](#c7--apul)

**Classes filles :** Aucune

**Propriétés :** Aucune

---

# Propriétés

## P1 : Administre

**Nom complet :** Administre

> Relation de dépendance entre deux entités.

**Domaine :** [C1 : Entité](#c1--entité)

**Portée :** [C1 : Entité](#c1--entité)

---

## P2 : Possède

**Nom complet :** Possède

> Relation de possession entre une entité et une entreprise publique.

**Domaine :** [C1 : Entité](#c1--entité)

**Portée :** [C5 : Entreprise publique](#c5--entreprise-publique)

