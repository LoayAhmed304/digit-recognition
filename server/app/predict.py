import numpy as np
from tensorflow.keras.models import Sequential

"""
Return the predicted digit and confidence score for the given pixels.
Args:
    model (Sequential): The trained model.
    pixels (list[float]): A list of 1-D 784 pixel values representing the image.
Returns:
    dict: A dictionary containing the predicted character and confidence score.
"""
def predict_digit(model: Sequential, pixels: list[float]):
        if len(pixels) != 784:
            return {"error": "Expected 784 pixels"}
    
        image_array = np.array(pixels).reshape(1, 784)
        
        prediction_result = model.predict(image_array)
        character = int(np.argmax(prediction_result))
        confidence = float(np.max(prediction_result))
        
        # convert result to char
        result = str(character)

        return {
            "character": result, 
            "confidence": confidence
        }