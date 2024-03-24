import os
import pathlib
from pydub import AudioSegment
from flask import Flask, request, render_template

app = Flask(__name__)
a = os.getcwd()

def trans_any_audio_types(filepath, input_audio_type, output_audio_type):
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    if os.getcwd() != a+"/static":
        print(os.getcwd())
        os.chdir('./static/')
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")

@app.route('/conv/')
def convert_page():
    with open('index.html') as f:
        html = f.read()
    return html

@app.route('/upload',methods=['POST'])
def upload():
    global file_extension
    f = request.files['file']
    file_extension = pathlib.Path(f.filename).suffix
    EXT = file_extension.strip('.')
    f.save('temp'+file_extension)
    trans_any_audio_types('temp'+file_extension,EXT,'mp3')
    return render_template('page1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)