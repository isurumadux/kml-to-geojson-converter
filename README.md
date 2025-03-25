<<<<<<< HEAD
# kml-to-geojson
A simple Python script to convert KML (Keyhole Markup Language) files into GeoJSON format. This script extracts geographical features and metadata from a KML file and transforms them into a GeoJSON feature collection.
=======

# KML to GeoJSON Converter

A simple Python script to convert KML (Keyhole Markup Language) files into GeoJSON format. This script extracts geographical features and metadata from a KML file and transforms them into a GeoJSON feature collection.



## Features
✅ Converts KML files into GeoJSON format ✅ Extracts geometry and metadata (name & description) ✅ Lightweight and easy to use
## Requirements

Ensure you have Python installed and install the required dependencies:

```bash
  pip install fastkml geojson
```
    
## Usage
Run the script with the following command:

> `python kml_to_geojson.py <input.kml> <output.geojson>`

> `python kml_to_geojson.py example.kml example.geojson`
## Usage/Examples

```javascript
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [80.7718, 7.8731]
      },
      "properties": {
        "name": "Sample Location",
        "description": "This is a test location."
      }
    }
  ]
}
}
```


## Contributing

Contributions are always welcome!

Feel free to submit pull requests or report issues!.

>>>>>>> 9cad585 (commit-0325)
