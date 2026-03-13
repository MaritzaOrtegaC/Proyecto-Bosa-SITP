import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/estaciones')
def get_bosa_data():
    try:
        # 1. DB: Abrimos el archivo descargado de internet
        with open('paraderos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 2. BACKEND: Filtro por coordenadas
        bosa_features = []
        for feature in data['features']:
            # Extraemos coordenadas del punto
            lon = feature['geometry']['coordinates'][0]
            lat = feature['geometry']['coordinates'][1]
            if (-74.22 <= lon <= -74.15) and (4.58 <= lat <= 4.65):
                bosa_features.append(feature)
                
        return jsonify({
            "type": "FeatureCollection",
            "features": bosa_features
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)