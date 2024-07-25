from flask import Flask, request, jsonify
import openai
import requests
import os

app = Flask(__name__)

api_key = os.getenv('OPENAI_API_KEY')
# Verifique se estamos no Heroku

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key=api_key)

def download_file(url, local_filename):
    
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/convert', methods=['POST'])
def convert_audio():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400
    
    url = data['url']

    input_path = 'audios/input_audio.ogg'
    #output_path = 'audios/output_audio.mp3'
    
    try:
        # Baixar o arquivo
        download_file(url, input_path)
        
        # Converter o arquivo
        #audio = AudioSegment.from_ogg(input_path)
        #audio.export(output_path, format='mp3')
        audio_file = open("audios/input_audio.ogg", "rb")
        
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="text"
        )
        resposta = str(transcription)
        
        return jsonify({'message': resposta, 'output_file': input_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
