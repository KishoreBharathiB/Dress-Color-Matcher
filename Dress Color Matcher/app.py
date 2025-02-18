from flask import Flask, request, render_template, send_from_directory, jsonify
import os
import cv2
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_main_color(image_path, k=4):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    kmeans = KMeans(n_clusters=k)
    kmeans.fit(image)
    colors = kmeans.cluster_centers_
    labels = np.unique(kmeans.labels_, return_counts=True)[1]
    main_color = colors[labels.argmax()]
    return main_color

def match_colors(existing_color, new_colors):
    min_distance = float('inf')
    best_match = None

    for file_path, color in new_colors:
        distance = np.linalg.norm(existing_color - color)
        if distance < min_distance:
            min_distance = distance
            best_match = file_path

    print(f"Best match found: {best_match}")  # Print result to the terminal
    return best_match

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    existing_file = request.files['existingDress']
    new_files = request.files.getlist('newDresses')

    existing_file_path = os.path.join(app.config['UPLOAD_FOLDER'], existing_file.filename)
    existing_file.save(existing_file_path)
    existing_color = extract_main_color(existing_file_path)

    new_colors = []
    for file in new_files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        color = extract_main_color(file_path)
        new_colors.append((file_path, color))

    best_match = match_colors(existing_color, new_colors)
    best_match_filename = os.path.basename(best_match) if best_match else None

    return jsonify({'best_match': best_match_filename})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
