# MISSION (Music by Expression)

Recommending music based on your facial expressions using FER 2013 dataset and Spotify API

# Project Description:

The emotion recognition model is trained on FER 2013 dataset. It can detect 7 emotions but we use 5. The project works by getting live video feed from web cam, pass it through the model to get a prediction of emotion. Then according to the emotion predicted, the app will fetch playlist of songs from Spotify\* through spotipy wrapper and recommend the songs by displaying them on the screen.

\*Note: playlist is generated by community through local survey in Central Java, Indonesia.

# Features:

- Real time expression detection and song recommendations.
- Neumorphism UI for website.

# Running the app:

Setting environment:

1. Make sure [Anaconda](https://www.anaconda.com/download) installed on your system.
2. Download [here](https://github.com/fahmifuady/Orbit-Final-Project/releases/tag/v0.1.0-alpha) and extract it. or you can clone this repository by
   > <code>git clone https://github.com/fahmifuady/Orbit-Final-Project.git</code>
3. Install all required dependencies.
   > <code>conda env create -f P310.yaml</code>
4. Activate MISSION environment.
   > <code>conda activate P310</code>
5. Activate MISSION web app
   > <code>python app.py</code>

If you already have an environment setup, you can run it straight away:

> <code>python app.py</code>

# Tech Stack:

- Tensorflow
- Keras
- Flask
- Bootstrap
- TailwindCSS
- Spotipy

# Dataset:

The dataset used for this project is the famous FER2013 dataset. Models trained on this dataset can classify 7 emotions. The dataset can be found [here](https://www.kaggle.com/msambare/fer2013).

Note that the dataset is highly imbalanced with happy class having maxiumum representation. This might be a factor resulting low accuracy after training.

# Model Architecture:

- The model architecture is a sequential model consisting of Conv2d, Maxpool2d, Dropout and Dense layers:

1. Conv2D layers throughout the model have different filter size from 32 to 128, all with activation 'relu'
2. Pooling layers have pool size (2,2)
3. Dropout is set to 0.25 as anything above results in poor performance
4. Final Dense layer has 'softmax' activation for classifying 7 emotions

- Used 'categorical_crossentropy' for loss with 'Adam' optimizer with 'accuracy' metric

Note:- Tried Implementing various other models like VGG16 but accuracy was far too low. This model architecture gives good enough accuracy. A bit more tinkering with hyper parameters might lead to a better accuracy

# Image Processing and Training:

- The images were normalised, resized to (48,48) and converted to grayscale in batches of 64 with help of 'ImageDataGenerator' in Keras API.
- Training took around 30 minutes on [Google Collab](https://colab.research.google.com/) for 50 epoch with an accuracy of ~75 %

# Current condition:

The entire project works perfectly fine. Live detection gives good frame rates due to multithreading.

# Project Components:

- Spotipy is a module for establishing connection to and getting tracks from Spotify using Spotipy wrapper.
- haarcascade is for face detection.
- camera.py is the module for video streaming, frame capturing, prediction and recommendation which are passed to main.py.
- main.py is the main flask application file.
- index.html in 'templates' directory is the web page for the application. Basic HTML and CSS.

# Issue:

The app in current state can't be deployed on web as:

- Opencv tries to open the camera on whatever device the app is running on. Code in current state makes use of webcam if available on server side not client side. So when app is run locally on a laptop Video Streaming through webcam is possible. But if it's deployed to a cloud, the app is stored in a data center somewhere which obviously doesn't have web camera connected to it and hence it doesn't work.

# Further Development:

- Instead of CSVs, create a databse and connect it to application. The DB will fetch songs for recommendations and new songs can be updated directly onto database
- Add a feature which will update specified playlists for better and more recent recommendations, a specific day over a fixed duration say every sunday and append it to database
- Directly play the song or redirect to the song on Spotify when user clicks on it.
- Rewrite code such that Video Streaming is done on client side instead of server side so as it make the app deployable

Note: Model accuracy is not that great. It is ~75%. Further training and fine tuning required.
