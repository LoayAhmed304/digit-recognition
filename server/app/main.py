from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import predict
import utils


model = utils.load_model('../models/mnist_model_256_3.h5')
print("Loaded model successfully.")

app = FastAPI()
app.add_middleware(CORSMiddleware, 
                allow_origins="https://digit.loay.work",
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"])

@app.post("/predict")
def predict_image(pixels: list[float]):
    return predict.predict_digit(model, pixels)