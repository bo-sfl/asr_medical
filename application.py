from flask import Flask, render_template, request
from werkzeug import secure_filename
from functions import process
import os

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
        # save file on local container
        audio.save('DeepSpeech-mozilla/uploaded_file.wav')

        # then launch deepspeech
        print("Casting MAGIC!")
        target_folder = os.getcwd() + "/DeepSpeech-mozilla"

        return process.deepspeech_predict(target_folder, 'uploaded_file.wav')

        # then launch classifier
        # then extract and output results

#        process.save_to_bucket(audio)
        # process and save the converted file
        # process.convert_for_asr(audio)

        # return 'file %s uploaded successfully' %secure_filename(audio.filename)


# @app.route('/send', methods = ['GET', 'POST'])
# def send():
#    if request.method == 'POST':
#       f = request.files['file']
#       # f.save(secure_filename(f.filename))
#       return 'file %s uploaded successfully' %f.filename


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

# for azure app in flask template
#"https://sfl-all-asr-app.azurewebsites.net/send"
