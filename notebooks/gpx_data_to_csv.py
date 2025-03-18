# verwendet gpx-Files aus \data\sample_gpx\ und liest die relevanten Daten aus
# und schreibt diese in gpx_ergebnisse_csv
# je nach Speicherort 'rr' bzw. 'cx' bekommen die Routen eine Kennzeichnung


import gpxpy
import pandas as pd
from haversine import haversine, Unit
import glob
import os

def read_gpx(file):
    try:
        with open(file, 'r', encoding='utf-8') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
    except UnicodeDecodeError:
        with open(file, 'r', encoding='latin1') as gpx_file:
            gpx = gpxpy.parse(gpx_file)

    data = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                data.append({
                    'latitude': point.latitude,
                    'longitude': point.longitude,
                    'elevation': point.elevation,
                    'time': point.time
                })

    track_name = gpx.tracks[0].name if gpx.tracks and gpx.tracks[0].name else os.path.basename(file)
    return pd.DataFrame(data), track_name

def calculate_stats(df):
    total_distance = 0.0
    elevation_gain = 0.0

    for i in range(1, len(df)):
        loc1 = (df.iloc[i-1]['latitude'], df.iloc[i-1]['longitude'])
        loc2 = (df.iloc[i]['latitude'], df.iloc[i]['longitude'])
        distance = haversine(loc1, loc2, unit=Unit.METERS)
        total_distance += distance

        if df.iloc[i]['elevation'] is not None and df.iloc[i-1]['elevation'] is not None:
            elevation_diff = df.iloc[i]['elevation'] - df.iloc[i-1]['elevation']
            if elevation_diff > 0:
                elevation_gain += elevation_diff

    return total_distance, elevation_gain

# Basisverzeichnis definieren (eine Ebene höher)
base_dir = os.path.join('..', 'data', 'sample_gpx')

# Unterordner definieren
cx_dir = os.path.join(base_dir, 'cx')
rr_dir = os.path.join(base_dir, 'rr')

# GPX-Dateien aus beiden Unterordnern sammeln
cx_files = glob.glob(os.path.join(cx_dir, '*.gpx'))
rr_files = glob.glob(os.path.join(rr_dir, '*.gpx'))

print(f"Gefundene CX-Dateien: {len(cx_files)}")
print(f"Gefundene RR-Dateien: {len(rr_files)}")

results = []

# CX-Dateien verarbeiten
for file in cx_files:
    try:
        df, track_name = read_gpx(file)
        if not df.empty:
            distance, elevation_gain = calculate_stats(df)
            distance_km = f"{(distance / 1000):.2f}".replace('.', ',') + " km"
            elevation_gain_formatted = f"{int(elevation_gain)} m"

            results.append({
                'file': os.path.basename(file),
                'name': track_name,
                'distance_km': distance_km,
                'elevation_gain': elevation_gain_formatted,
                'type': 'cx'  # Typ "cx" hinzufügen
            })
    except Exception as e:
        print(f"Fehler bei CX-Datei {file}: {str(e)}")

# RR-Dateien verarbeiten
for file in rr_files:
    try:
        df, track_name = read_gpx(file)
        if not df.empty:
            distance, elevation_gain = calculate_stats(df)
            distance_km = f"{(distance / 1000):.2f}".replace('.', ',') + " km"
            elevation_gain_formatted = f"{int(elevation_gain)} m"

            results.append({
                'file': os.path.basename(file),
                'name': track_name,
                'distance_km': distance_km,
                'elevation_gain': elevation_gain_formatted,
                'type': 'rr'  # Typ "rr" hinzufügen
            })
    except Exception as e:
        print(f"Fehler bei RR-Datei {file}: {str(e)}")

if results:
    # Erweiterte Anzeigeoptionen
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    results_df = pd.DataFrame(results)
    # Explizite Spaltenreihenfolge
    if all(col in results_df.columns for col in ['file', 'name', 'distance_km', 'elevation_gain', 'type']):
        results_df = results_df[['file', 'name', 'type', 'distance_km', 'elevation_gain']]

    print("\nErgebnisse:")
    print(results_df)

    # Speichere in CSV-Datei mit Semikolon als Trennzeichen
    results_df.to_csv('gpx_ergebnisse.csv', index=False, sep=';')
    print("Ergebnisse wurden in 'gpx_ergebnisse.csv' gespeichert.")
else:
    print("Keine gültigen GPX-Daten gefunden.")
