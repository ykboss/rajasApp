#importing libraries
from flask import Flask, render_template, request, flash, redirect, url_for
import pytesseract
from PIL import Image
import os
from googletrans import Translator

app = Flask(__name__)
app.secret_key = 'super_secret_key'

def translate_text(text, src_lang='hi', dest_lang='en'):
    translator = Translator()  # Create a translator instance
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text  # Return the translated text


def nlpFunc(text):
    try:
        translated_text = translate_text(text)  # Translate the Hindi text
        result_dict = {"Translated Text": translated_text, "Original Text": text}
        return result_dict
    except Exception as e:
        flash("Translation error:", e)  # Handle potential translation errors
        return {"Example Key": text}  # Return original text if translation fails


def ocrFunc(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='hin')
    return nlpFunc(text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_option = request.form.get('inputOption')
    user_input_text = request.form.get('text', '').strip()
    user_input_image = request.files.get('image')

    if input_option == 'text' and not user_input_text:
        flash('Please provide text.')
        return redirect(url_for('index'))
    elif input_option == 'image' and not user_input_image:
        flash('Please upload an image.')
        return redirect(url_for('index'))

    if input_option == 'text':
        result = nlpFunc(user_input_text)
    else:
        # Save the image temporarily
        image_path = "temp_image.png"
        user_input_image.save(image_path)
        result = ocrFunc(image_path)
        # Delete the temporary image file after processing
        # os.remove(image_path)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
