from flask import Flask, render_template, request
from text_to_video.video_generator import VideoGenerator
from text_to_video.video_editor import VideoEditor
from text_to_video.audio_processor import AudioProcessor

app = Flask(__name__)
video_generator = VideoGenerator()
video_editor = VideoEditor()
audio_processor = AudioProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_video', methods=['POST'])
def generate_video():
    text = request.form['text']
    video_file = video_generator.generate_video(text)
    return video_file

@app.route('/customize_video', methods=['POST'])
def customize_video():
    style = request.form['style']
    effects = request.form.getlist('effects')
    video_editor.customize_video(style, effects)
    return 'Success'

@app.route('/add_audio', methods=['POST'])
def add_audio():
    audio_file = request.files['audio']
    audio_processor.process_audio(audio_file)
    return 'Success'

@app.route('/preview_video')
def preview_video():
    video_editor.preview_video()
    return 'Success'

@app.route('/edit_video')
def edit_video():
    video_editor.edit_video()
    return 'Success'

@app.route('/export_video', methods=['POST'])
def export_video():
    format = request.form['format']
    video_editor.export_video(format)
    return 'Success'

if __name__ == '__main__':
    app.run()
