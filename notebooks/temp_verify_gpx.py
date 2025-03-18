import gpxpy

with open('FruehKlassi25.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

print(len(gpx.tracks))  # Sollte größer als 0 sein
