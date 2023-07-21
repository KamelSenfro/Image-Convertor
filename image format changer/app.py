from flask import Flask, request, send_file, render_template, Response,jsonify
from PIL import Image
import io
app = Flask(__name__)

# Route for the index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route for jpgtopng page
@app.route("/jpgtopng", methods=["GET"])
def jpg_to_png():
    return render_template("jpgtopng.html")

# Route for pngtojpg page
@app.route("/pngtojpg", methods=["GET"])
def png_to_jpg():
    return render_template("pngtojpg.html")

# Route for webptopng page
@app.route("/webptopng", methods=["GET"])
def webp_to_png():
    return render_template("webptopng.html")

# Route for bmptopng page
@app.route("/bmptopng", methods=["GET"])
def bmp_to_png():
    return render_template("bmptopng.html")

# Route for pngtopdf page
@app.route("/pngtopdf", methods=["GET"])
def png_to_pdf():
    return render_template("pngtopdf.html")

@app.route("/api/jpgtopng", methods=["POST"])
def convert_jpg_to_png():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided."}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No selected image file."}), 400

        if file.mimetype != 'image/jpeg':
            return jsonify({"error": "Selected file is not in JPG format."}), 400

        image = Image.open(file)
        png_data = io.BytesIO()
        image.save(png_data, format='PNG')
        png_data.seek(0)

        return jsonify({"image_data": png_data.read().hex()}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
            app.run(debug=True)