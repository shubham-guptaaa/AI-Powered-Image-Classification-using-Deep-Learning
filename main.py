import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Model Path
MODEL_PATH = os.path.join(BASE_DIR, "cnn_cifar10_model.keras")

# Allowed File Type
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# CIFAR-10 class names
CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Start Flask app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the trained model
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully:", MODEL_PATH)
except Exception as e:
    model = None
    print("Error loading model:", e)

# Check if uploaded file is allowed
def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Preprocess Image
def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB").resize((32, 32))
    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Home route
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction_text=None, image_url=None)

# Handle image upload and prediction
@app.route("/predict", methods=["POST"])
def predict():
    # Check if file is uploaded
    if "image" not in request.files:
        return render_template("index.html", prediction_text="No file part found.", image_url=None)
    
    file = request.files["image"]

    # Check if filename is valid
    if file.filename == "":
        return render_template("index.html", prediction_text="No file selected.", image_url=None)

    if not is_allowed_file(file.filename):
        return render_template("index.html", prediction_text="File type not allowed.", image_url=None)
    
    # Save uploaded file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    # Ensure model is loaded
    if model is None:
        return render_template(
            "index.html",
            prediction_text="Model not loaded on server.",
            image_url=url_for('static', filename=f"uploads/{filename}")
        )

    # Predict image
    try:
        processed_img = preprocess_image(file_path)
        predictions = model.predict(processed_img)
        predicted_index = int(np.argmax(predictions, axis=1)[0])
        predicted_label = CLASS_NAMES[predicted_index]
        confidence_score = float(np.max(predictions))

        prediction_text = f"Predicted: {predicted_label} (Confidence: {confidence_score:.2f})"

        return render_template(
            "index.html",
            prediction_text=prediction_text,
            image_url=url_for('static', filename=f"uploads/{filename}")
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error during prediction: {e}",
            image_url=url_for('static', filename=f"uploads/{filename}")
        )

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
