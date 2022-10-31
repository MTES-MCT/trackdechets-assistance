# Trackdéchets assistance

**CMs pour l'assistance Trackdéchets**

<img height="100px" style="margin-right: 20px" src="./src/static/img/trackdechets.png" alt="Logo Trackdéchets"></img>
<img height="100px" src="./src/common_static/img/marianne_mte.svg" alt="Logo MTES MCT"></img>

# Introduction

Micro-cms pour administrer le contenu de l'assistance questions-réponses guidées de Trackdéchets.

# Pré-requis

- Python > 3.9
- pipenv

# Installation

Initialisation et activation d'un environnement

```
$ pipenv shell
```

Installation des dépendances

```
$ pipenv install -d
```

# Environnement

Se référer au fichier src/core/settings/env.dist

# Linting

Utiliser : 

```
    $ ./lint.sh
```

et pour les templates :

```
    $ djlint templates --profile=django --reformat
```

## Licence

Le code source du logiciel est publié sous licence [MIT](https://fr.wikipedia.org/wiki/Licence_MIT).
