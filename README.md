# Geodaten-Visualisierung mit Jupyter Notebooks

Dieses Repository enthält Jupyter Notebooks zur Visualisierung von GPX-Track-Daten mit Open-Source-Tools. Die Notebooks demonstrieren verschiedene Techniken zur Verarbeitung und Darstellung geographischer Daten, insbesondere für die Analyse und Visualisierung von GPS-Tracks mit Bibliotheken wie `geopandas`, `osmnx`, `matplotlib` und `gpxpy`.

## 📂 Projektstruktur
```
geodaten-visualisierung/
├── notebooks/        # Jupyter Notebooks mit Code und Erklärungen
│   ├── 01_single_track.ipynb  # Visualisierung eines einzelnen GPX-Tracks
│   ├── 02_multiple_tracks.ipynb # Vergleich mehrerer GPX-Tracks
├── data/             # Zusatzdaten für Plots und Analysen
├── src/              # Python-Skripte für wiederverwendbare Funktionen
├── images/           # Abbildungen und Screenshots der Visualisierungen
├── README.md         # Diese Dokumentation
├── requirements.txt  # Liste der benötigten Python-Abhängigkeiten
├── LICENSE           # Lizenzinformationen
```

## 📊 Beispielnotebooks

Die folgenden Notebooks sind enthalten:

- **01_single_track.ipynb**: 
  - Liest eine GPX-Datei ein und extrahiert GPS-Daten (Breitengrad, Längengrad, Zeitstempel).
  - Berechnet eine Bounding-Box für den Track und lädt das Straßennetz aus OpenStreetMap mit `osmnx`.
  - Visualisiert den Track zusammen mit zusätzlichen Shapefile-Daten (z. B. Gewässer).
  - Zeigt die zurückgelegte Distanz und die verstrichene Zeit in der Grafik an.
  
- **02_multiple_tracks.ipynb**: 
  - Vergleicht mehrere GPX-Tracks in einer gemeinsamen Visualisierung.
  - Nutzt `geopandas`, um die Tracks auf einer Karte darzustellen.
  - Zeigt Unterschiede in Distanz, Geschwindigkeit und Zeitverlauf zwischen den Tracks.

## 📂 Datenquelle
Die bereitgestellten Beispiel-Datensätze im Ordner `data/` stammen aus öffentlich zugänglichen Quellen oder wurden synthetisch erzeugt.

## 📜 Lizenz
Dieses Projekt steht unter der **Apache 2.0 Lizenz** – siehe die Datei [LICENSE](LICENSE) für Details.

## 💡 Kontakt & Feedback
Fragen oder Anregungen? Erstelle ein [Issue](https://github.com/clmnsspkt/MappingWithPython/issues) oder vernetze dich mit mir auf LinkedIn!

---
🌍 Viel Spaß mit der Geodaten-Visualisierung!



-----------------------
-----------------------


# **Geospatial Data Visualization with Jupyter Notebooks**

This repository contains Jupyter Notebooks for visualizing GPX track data using open-source tools. The notebooks demonstrate various techniques for processing and displaying geographic data, particularly for analyzing and visualizing GPS tracks with libraries such as `geopandas`, `osmnx`, `matplotlib`, and `gpxpy`.

## 📂 **Project Structure**
```
mapping-with-python/
├── notebooks/        # Jupyter Notebooks with code and explanations
│   ├── 01_single_track.ipynb  # Visualization of a single GPX track
│   ├── 02_multiple_tracks.ipynb # Comparison of multiple GPX tracks
├── data/             # Additional data for plots and analysis
├── src/              # Python scripts for reusable functions
├── images/           # Images and screenshots of visualizations
├── README.md         # This documentation
├── requirements.txt  # List of required Python dependencies
├── LICENSE           # License information
```

## 📊 **Example Notebooks**

The following notebooks are included:

- **01_single_track.ipynb**:
  - Reads a GPX file and extracts GPS data (latitude, longitude, timestamp).
  - Computes a bounding box for the track and loads the road network from OpenStreetMap using `osmnx`.
  - Visualizes the track along with additional shapefile data (e.g., water bodies).
  - Displays total distance covered and elapsed time in the plot.

- **02_multiple_tracks.ipynb**:
  - Compares multiple GPX tracks in a single visualization.
  - Uses `geopandas` to display tracks on a map.
  - Highlights differences in distance, speed, and time progression between tracks.

## 📂 **Data Sources**
The sample datasets provided in the `data/` folder come from publicly available sources or have been synthetically generated.

## 📜 **License**
This project is licensed under the **Apache 2.0 License** – see the [LICENSE](LICENSE) file for details.

## 💡 **Contact & Feedback**
Questions or suggestions? Create an [Issue](https://github.com/clmnsspkt/MappingWithPython/issues) or connect with me on LinkedIn!

---
🌍 **Enjoy geospatial data visualization!**

---