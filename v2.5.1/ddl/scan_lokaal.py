import os
import json

def scan_ddl_map():
    base_path = "."  # De map waar het script staat
    diagrammen = {}

    print("Bezig met scannen van lokale mappen...")

    for root, dirs, files in os.walk(base_path):
        for file in files:
            # We kijken naar de bestandsnaam zonder de extensie en database-type
            # Bijv: 'Onderwijs_Leerlingen_mysql.sql' -> 'Onderwijs_Leerlingen'
            if file.endswith(('.sql', '.json')):
                name_part = file.replace('_mysql.sql', '') \
                                .replace('_mssql.sql', '') \
                                .replace('_oracle.sql', '') \
                                .replace('_postgresql.sql', '') \
                                .replace('.json', '') \
                                .replace('_sql', '')
                
                if name_part not in diagrammen:
                    diagrammen[name_part] = []
                diagrammen[name_part].append(file)

    # Opslaan naar een JSON voor vergelijking
    with open('lokale_scan_resultaten.json', 'w', encoding='utf-8') as f:
        json.dump(diagrammen, f, indent=4)

    print("-" * 30)
    print(f"Klaar! Gevonden resultaten:")
    print(f"Totaal aantal unieke diagram-namen: {len(diagrammen)}")
    print(f"Totaal aantal losse bestanden: {sum(len(v) for v in diagrammen.values())}")
    print(f"Resultaten opgeslagen in: lokale_scan_resultaten.json")
    print("-" * 30)

if __name__ == "__main__":
    scan_ddl_map()