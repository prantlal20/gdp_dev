from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
from datetime import datetime

app = Flask(__name__)

# Basisordner für Uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    folder_name = request.form.get('folder', 'default_project')
    os.makedirs(os.path.join(UPLOAD_FOLDER, folder_name), exist_ok=True)

    file = request.files.get('photo')
    if not file:
        return jsonify({"success": False, "message": "No file sent"})

    # Komprimieren und speichern
    img = Image.open(file)
    img = img.convert("RGB")
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
    save_path = os.path.join(UPLOAD_FOLDER, folder_name, filename)
    img.save(save_path, "JPEG", quality=70)

    return jsonify({"success": True, "filename": filename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
