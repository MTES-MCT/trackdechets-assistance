# Site web Trackdéchets & application d'assistance

**CMS pour le site web Trackdéchet et le funnel d'assistance**

<img height="100px" style="margin-right: 20px" src="./src/static/img/trackdechets.png" alt="Logo Trackdéchets"></img>
<img height="100px" src="./src/static/img/marianne_mte.svg" alt="Logo MTES MCT"></img>

# Introduction

Micro-cms pour administrer:

- le contenu de l'assistance questions-réponses guidées de Trackdéchets
- le site web Trackdéchets et le calendrier des formations


<img height="300px"  src="./readme_medias/assistance.png" alt="Assistance Trackdéchets"></img>

<img height="300px" src="./readme_medias/website.png" alt="Site web Trackdéchets"></img>

# Pré-requis

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/)

# Installation

Installation des dépendances

```
$ uv sync --frozen
```

Pour les dépendances de test et de développement.

```
$ uv sync --frozen --group test --group dev
```

# Environnement

Se référer au fichier src/core/settings/env.dist

# Linting

Utiliser :

```
    $ ./lint.sh
```

## Licence

Le code source du logiciel est publié sous licence [MIT](https://fr.wikipedia.org/wiki/Licence_MIT).
