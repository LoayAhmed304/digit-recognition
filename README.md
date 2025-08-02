# Digit Recognition App

A simple web app that recognizes handwritten digits using a trained neural network.

## Demo
Visit https://digit.loay.work

## Tech Stack
- **Backend**: FastAPI + TensorFlow
- **Frontend**: React + TS
- **Deployment**: Docker + Nginx


## Running it locally

### 1- Clone the repo and cd into it
```sh
git clone github.com/LoayAhmed304/digit-recognition
cd digit-recognition
```

### 2- Install python requirements
```sh
cd server
pip install -r requirements.txt
```

### 3- Train the model (if you don't have a pre-trained one)
```sh
python model.py
```
It'll be saved in models/mnist_model.h5

### 4- Docker compose everything
In the root directory (digit-recognition)
```sh
docker compose up --build -d
```



