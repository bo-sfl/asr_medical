from flask import Flask, render_template, request
from werkzeug import secure_filename
from functions import process

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('interface.html')


@app.route('/send', methods = ['POST'])
def submit_file():
    audio = request.files['file']
    response = process.check_format(audio)
    # response = check_format(audio)
    if response == 0:
        return 'file %s format is not correct, please use a valid .wav file' %secure_filename(audio.filename)
    else:
        # save raw file
        process.save_to_bucket(audio)
        # process and save the converted file
        # process.convert_for_asr(audio)
        return 'file %s uploaded successfully' %secure_filename(audio.filename)

# @app.route('/send', methods = ['GET', 'POST'])
# def send():
#    if request.method == 'POST':
#       f = request.files['file']
#       # f.save(secure_filename(f.filename))
#       return 'file %s uploaded successfully' %f.filename


if __name__ == '__main__':
    app.run()
