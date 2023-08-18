from flask import Flask, render_template, request
from video_generator import VideoGenerator
from video_editor import VideoEditor
from audio_processor import AudioProcessor

app = Flask(__name__)
text_to_video_app = TextToVideoApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_video', methods=['POST'])
def generate_video():
    text = request.form['text']
    video_file = text_to_video_app.generate_video(text)
    return video_file

@app.route('/customize_video', methods=['POST'])
def customize_video():
    style = request.form['style']
    effects = request.form.getlist('effects')
    text_to_video_app.customize_video(style, effects)
    return 'Success'

@app.route('/add_audio', methods=['POST'])
def add_audio():
    audio_file = request.files['audio']
    text_to_video_app.add_audio(audio_file)
    return 'Success'

@app.route('/preview_video')
def preview_video():
    text_to_video_app.preview_video()
    return 'Success'

@app.route('/edit_video')
def edit_video():
    text_to_video_app.edit_video()
    return 'Success'

@app.route('/export_video', methods=['POST'])
def export_video():
    format = request.form['format']
    text_to_video_app.export_video(format)
    return 'Success'

if __name__ == '__main__':
    app.run()
