from fastkml import kml
import geojson
import sys

def kml_to_geojson(kml_file, geojson_file):
    try:
        with open(kml_file, 'r', encoding='utf-8') as f:
            kml_data = f.read()

        k = kml.KML()
        k.from_string(kml_data)
        features = []
        
        for doc in k.features():
            for placemark in doc.features():
                geom = placemark.geometry
                properties = {"name": placemark.name, "description": placemark.description}
                features.append(geojson.Feature(geometry=geom, properties=properties))

        geojson_data = geojson.FeatureCollection(features)
        
        with open(geojson_file, 'w', encoding='utf-8') as f:
            geojson.dump(geojson_data, f, indent=2)

        print(f"Conversion successful! GeoJSON saved to {geojson_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python kml_to_geojson.py <input.kml> <output.geojson>")
    else:
        kml_to_geojson(sys.argv[1], sys.argv[2])
