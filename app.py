from flask import Flask, request, send_file, render_template, Response ,jsonify
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

@app.route('/api/jpgtopng', methods=['POST'])
def convert_jpg_to_png():
    # Get the image file from the request parameter
    file = request.files['file']

    # Open the image file with Pillow
    img = Image.open(file)

    # Convert the image to PNG format
    png_img = io.BytesIO()
    img.save(png_img, format='PNG')
    png_img.seek(0)

    # Create a response object with the PNG image as an attachment
    response = make_response(png_img.read())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='image.png')
if __name__ == "__main__":
            app.run(debug=True)