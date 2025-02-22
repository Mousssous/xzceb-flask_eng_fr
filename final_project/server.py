from machinetranslation.tests import translator
from flask import Flask, render_template, request
import json
import machinetranslation.tests.translator as t

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text_translated=t.english_to_french(textToTranslate)
    return text_translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text_translated=t.french_to_english(textToTranslate)
    return text_translated

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
