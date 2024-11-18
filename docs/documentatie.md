# Documentatie

Deze documentatie is geschreven in [Markdown](https://www.markdownguide.org) en wordt gepubliceerd met [MkDocs](https://www.mkdocs.org). Voor de vormgeving wordt gebruik gemaakt van het [Material theme](https://squidfunk.github.io/mkdocs-material/). Daarnaast gebruiken we [Pygments](https://squidfunk.github.io/mkdocs-material/extensions/codehilite/#installation) om 'highlighting' van code te kunnen gebruiken, en we gebruiken [PyMdown Extensions](https://squidfunk.github.io/mkdocs-material/extensions/pymdown/).

## Installatie vooraf

Om mkdocs en het Material theme te gebruiken installeer je eerst de benodigde bibliotheken (Python 3). Installeer daarnaast Pygments en de PyMdown extensions.

```
pip install mkdocs
pip install mkdocs-material
pip install pygments
pip install pymdown-extensions
```

## Gebruik

De documentatie ingechekt en gepubliceerd op GitHub, bij aanpassingen van de documentatie ga je naar de root directory van de documentatie (waar de **mkdocs.yml** staat), en voer het volgende commando uit:

```
mkdocs gh-deploy
```

