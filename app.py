from flask import Flask, render_template, request, redirect, url_for
import os
from analyzer.ppt_parser import extract_text_from_ppt
from analyzer.text_analyzer import analyze_text
from analyzer.layout_checker import analyze_layout
from analyzer.suggestions import generate_suggestions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "ppt_file" not in request.files:
            return "No file part"
        file = request.files["ppt_file"]
        if file.filename == "":
            return "No selected file"
        if file and file.filename.endswith(".pptx"):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return redirect(url_for("slides", filename=file.filename))
    return render_template("index.html")

@app.route("/slides/<filename>")
def slides(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    ppt_data = extract_text_from_ppt(file_path)
    
    # Analyze each slide
    slide_results = []
    for slide in ppt_data:
        text_suggestions = []
        layout_suggestions = analyze_layout(slide)
        for text in slide['texts']:
            text_suggestions.extend(analyze_text(text))
        all_suggestions = generate_suggestions(slide, text_suggestions, layout_suggestions)
        slide_results.append({
            "slide_number": slide['slide_number'],
            "title": slide['title'],
            "texts": slide['texts'],
            "suggestions": all_suggestions
        })
    
    return render_template("slide.html", slides=slide_results)

if __name__ == "__main__":
    app.run(debug=True)