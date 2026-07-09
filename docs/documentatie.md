# Deployment

Deze handleiding beschrijft hoe je op basis van een XMI-bestand een nieuwe versie van het GGM (Gemeentelijk Gegevensmodel) publiceert. Dit proces genereert automatisch:

- een nieuwe Excel-specificatie,
- een set vertaalde `.qea`-bestanden (voor Enterprise Architect),
- een volledige set Markdown-documentatie,
- en een gepubliceerde versie van de documentatie op GitHub Pages.

> Dit proces wordt geautomatiseerd met behulp van [Taskfile](https://taskfile.dev/), `crunch_uml`, `mkdocs`, `mike` en andere tools.

Hiernaast zijn er utils die gebruikt kunnen worden om geautomatiseerd aanpassingen in de GGM-repository te maken. De belangrijkste util werkt doordat wijzigingen in een Excel direct naar de repository worden geschreven. 

---

## Wat doet deze deployment?

Zodra je een nieuwe versie van het model in XMI-formaat hebt, wil je daaruit automatisch alle benodigde output genereren voor publicatie en gebruik:

1. **Validatie**: Zijn alle tools en instellingen correct?
2. **Import**: Het XMI-bestand wordt geïmporteerd in een lokale Crunch UML-database.
3. **Documentatie**: Markdown-bestanden worden gegenereerd uit het model.
4. **Excel**: Een Excel-specificatie wordt automatisch aangemaakt.
5. **Vertalingen**: Het i18n-bestand wordt bijgewerkt via lokale Ollama (of na bevestiging via Google/Bing) en vervolgens wordt per taal een `.qea` gemaakt. Bij `full-deploy` wordt gevraagd of de bestaande vertaling hergebruikt wordt (alleen ontbrekende waarden aanvullen) of dat de hele vertaling opnieuw moet.
6. **Publicatie**: De documentatie wordt gepubliceerd via GitHub Pages met versiebeheer via `mike`.

---

## Randvoorwaarden

Om de deployment automatisch te kunnen uitvoeren moet je [Taskfile](https://taskfile.dev/) geïnstalleerd hebben en ook mkdocs met een aantal extensies. Mkdocs met de benodigde extensies kun je met het volgende commando installeren. 

En wanneer je dat in je `.md` bestand plaatst, zal het eruitzien als:

```bash
pip install mkdocs mkdocs-material mike \
    pymdown-extensions \
    markdown-include \
    mkdocs-git-revision-date-plugin \
    mkdocs-git-authors-plugin \
    mkdocs-glightbox \
    mkdocs-minify-plugin \
    typing_extensions \
    mkdocs-glightbox
```

### Vertaling via lokale Ollama (aanbevolen)

Vanaf `crunch_uml` 0.4.11 kunnen vertalingen lokaal via [Ollama](https://ollama.com/) worden gedaan, zonder dat tekst naar publieke endpoints wordt gestuurd. Voor de aanbevolen lokale modus moet Ollama draaien op `http://localhost:11434` en het aanbevolen model gepulld zijn:

```bash
ollama serve &
ollama pull mistral-small3.1:24b
```

`OLLAMA_MODEL` en `OLLAMA_URL` zijn in `.env` instelbaar.

Als Ollama niet draait, of het aanbevolen model is niet gepulld, dan vraagt `task util:generate-i18n` expliciet:

- of een ander gepulld model gebruikt moet worden (met lijst van beschikbare modellen), óf
- of de vertaling via de publieke `translators`-backend (Google/Bing) mag — zodat de vertaling nooit ongemerkt over het internet loopt.

### Benodigde bestanden onder de versie-directory

| Bestand               | Verplicht? | Beschrijving                                                     |
|------------------------|------------|------------------------------------------------------------------|
| `model.xmi`            | ✅         | Het informatiemodel in XMI-formaat                              |
| `model.qea`            | ✅         | De `.qea`-versie van het model, gebruikt voor het maken van vertalingen |
| `translations.json`    | ✅         | Een i18n-bestand met vertalingen per taal                        |

In het geval van het voorbeeld `.env`-bestand moet er dus een directory zijn genaamd `v1.0.0` met bovengenoemde bestanden erin.

## Stap 1 – Stel de `.env` goed in

Voor elke nieuwe versie pas je het bestaande `.env`-bestand aan, zodat duidelijk is voor welke nieuwe versie het deployment is. Dit bestand bepaalt ook welke bestanden en directories gebruikt worden. Het is belangrijk dat `VERSION` exact overeenkomt met de directory van de versie die je gaat deployen.

### 📄 Voorbeeld `.env`-bestand:

```env
VERSION=v1.0.0
XMI_FILE=ggm_model.xmi
GGM_FILE=ggm_model.qea
EXCEL_FILE=ggm_model.xlsx
TRANSLATIONS_DIR=translations
i18N_FILE=translations.json
...
```

## Stap 2 – deployment maken

Gebruik onderstaand overzicht om losse taken uit te voeren en zo delen van de deployment te maken, of alles in één keer te deployen met `full-deploy`.

### 📋 Overzicht beschikbare taken

| Taaknaam                | Wat het doet                                                               |
|-------------------------|----------------------------------------------------------------------------|
| `check-tools`           | Controleert of benodigde tools zijn geïnstalleerd (`crunch_uml`, `mkdocs`, etc.) |
| `check-vars`            | Controleert of `.env` juist is geconfigureerd en of paden kloppen          |
| `import-xmi`            | Importeert het XMI-bestand en maakt een lokale database. (kan meerdere minuten duren) |
| `generate-docs`         | Genereert Markdown-bestanden vanuit het model                              |
| `generate-excel`        | Maakt een Excel-specificatie                                               |
| `generate-translations` | Maakt per taal een vertaalde `.qea`-versie (o.b.v. `translations.json`)    |
| `util:generate-i18n`    | Bouwt/vernieuwt het i18n-bestand via lokale Ollama (met fallback-bevestiging voor Google/Bing). Standaard worden alleen ontbrekende vertalingen aangevuld; met `task util:generate-i18n UPDATE_I18N=False` wordt alles opnieuw vertaald. |
| `deploy-docs`           | Bouwt de documentatie lokaal met MkDocs en mike zodat deze lokaal gestest kunnen worden, en later gepubliceerd. |
| `publish-docs`          | Publiceert de documentatie naar GitHub Pages (`gh-pages` branch)           |
| `full-deploy`           | Voert alles hierboven in één keer uit. Vraagt voorafgaand aan de vertalingen of de bestaande vertaling hergebruikt wordt of dat alles opnieuw moet. Publicatie via `publish-docs` op GitHub pages zit hier niet in. |

### Taken uitvoeren

Bekijk alle taken:

```bash
task --list
```

Start één enkele taak (taken die randvoorwaardelijk zijn worden eerst uitgevoerd):

```bash
task generate-excel
```

Voer alle taken uit:

```bash
task full-deploy
```

## Stap 3 – lokaal testen

Voordat je publiceert, kun je de gegenereerde documentatie lokaal testen. Gebruik deze opdracht om de documentatie te bouwen en te bekijken:

```bash
task deploy-docs
mike serve
```

Je kunt de documentatie dan bekijken op http://localhost:8000 

## Stap 4 – publiceren

### Test lokaal

Als alles goed werkt kun je de documentatie publiceren op GitHub pages. Deze stap werkt alleen als je toegang hebt tot de GitHub repository van het GGM:

```bash
task publish-docs
```

Let op: dit publiceert direct naar de gh-pages branch van de GitHub-repository. Je wordt gevraagd om bevestiging voordat de site echt live gaat.

## Utils

De utils maken geen gebruik van een eerder ingelezen XMI, maar lezen de benodigde informatie steeds opnieuw in.  

### 📋 Overzicht beschikbare utils

| Taaknaam                | Wat het doet                                                               |
|-------------------------|----------------------------------------------------------------------------|
| `util-import-xlsx`      | Importeert het excel-bestand in dat in `.env` staat aangegeven en leest alle waarden naar de EA repository, en update alles wat in de Excel-file is aangepast. Gebruik voor de excel-file het formaat zoals die wordt gegenereerd in `generate-excel`. Er mogen tabbladen en kolommen worden verwijderd (behalve de `id`-kolommen), zolang de kolomnamen maar overeenkomen.|

