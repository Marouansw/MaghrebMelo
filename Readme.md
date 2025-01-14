# Moroccan Music Classifier

This project is a web application designed to classify Moroccan music genres. The application allows users to upload an audio file, and the model predicts the genre based on its features. The backend is built using Flask, and the machine learning model is trained on audio data.

## Getting Started

Follow these instructions to set up and run the application locally.

### Prerequisites

Make sure you have the following installed on your system:
- Python (3.8 or later)
- Git

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd Moroccan-Music-Classifier
   ```

3. **Create a Virtual Environment**
   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. **Install the Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Navigate to the Application Directory**
   ```bash
   cd App
   ```

7. **Run the Application**
   ```bash
   python app.py
   ```

### Accessing the Application

Once the application is running, open your web browser and navigate to:
```
http://127.0.0.1:5001
```

### Usage

- Upload an audio file via the web interface.
- The application will process the file and display the predicted music genre.

## License
This project is licensed under the MIT License.

