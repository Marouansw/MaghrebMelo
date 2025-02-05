from flask import Flask, request, render_template
import librosa
import numpy as np
import tensorflow as tf
import os

# Load pre-trained model
model = tf.keras.models.load_model('au_model.h5')

# Define class names (update with your class labels)
class_dict = {0: 'andalusian', 1: 'chaabi', 2: 'gnawa', 3: 'imazighn', 4: 'rai', 5: 'rap'}

# Feature extraction function
def extract_features(file_path, duration=20):
    """
    Extracts features (Mel spectrogram) from the audio file for prediction.
    """
    
    audio, rate = librosa.load(file_path, duration=duration)
    
    # Extract Mel spectrogram features
    mel_spectrogram = librosa.feature.melspectrogram(y=audio, sr=rate, n_fft=2048, hop_length=512)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=np.max)
    
    # Ensure the shape matches the input shape of the model
    mel_spectrogram_db = mel_spectrogram_db[:, :862]  # Ensure 646 frames 
    mel_spectrogram_db = np.expand_dims(mel_spectrogram_db, axis=-1)  # Adding channel dimension
    
    return np.expand_dims(mel_spectrogram_db, axis=0)  

app = Flask(__name__)

# Home route to render the upload page
@app.route('/')
def home():
    return render_template('upload.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return render_template('upload.html', error="No file uploaded")

    file = request.files['audio']
    if file.filename == '':
        return render_template('upload.html', error="No file selected")
    
    # Save the uploaded file temporarily
    file_path = 'temp_audio.wav'
    file.save(file_path)

    try:
        # Extract features and make prediction
        features = extract_features(file_path)
        predictions = model.predict(features)
        predicted_class = class_dict[np.argmax(predictions)]

        return render_template('result.html', prediction=predicted_class)
    except Exception as e:
        return render_template('upload.html', error=f"Error processing file: {e}")
    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

# Run the app
if __name__ == '__main__':
    app.run(port=7860)  
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)
