"""
This module contains utility functions for data preprocessing and scaling.
It includes functions to split datasets, scale data, and check data integrity.
It might not be used in the current application.
But it is essential for preparing data for most machine learning models.
"""

import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras import models
import matplotlib.pyplot as plt

# Initial configs
np.set_printoptions(precision=2)
tf.get_logger().setLevel('ERROR')
tf.autograph.set_verbosity(0)


"""
Input:
    x: Data input
    y: Data output
    ratio: The percentage of the data to be trained
Output:
    Tuple (x_train, y_train, x_cv, y_cv, x_test, y_test)
"""
def split_data_set(x, y, ratio):
   x_train, x_, y_train, y_ = train_test_split(x, y, test_size=ratio, random_state=1)
   x_cv, x_test, y_cv, y_test = train_test_split(x_, y_, test_size=0.5, random_state=1)
   del x_, y_

   return (x_train, y_train, x_cv, y_cv, x_test, y_test)


"""
Input: 
    x: Data to be scaled and use their mean and std deviation
Output:
    Tuple(Scaled data, the linear scaler)
"""
def scale_train_data(x):
    scaler_linear = StandardScaler()
    x_linear = scaler_linear.fit_transform(x)
    return (x_linear, scaler_linear)


"""
Input: 
    x: data to be scaled
    scaler_linear: The linear scaler previoulsy initiated via `scale_train_data(x)`
Output:
   scaled_data: The input data after scaling 
"""
def scale_data(x, scaler_linear):
    scaled_data = scaler_linear.transform(x)
    return scaled_data 


"""
Input:
   yhat: The model output
   y: The real output
Output:
    y_mse: Corresponding mean Squared Error (with 2m as the division, not m)
"""
def calc_mse(yhat, y):
    y_mse = mean_squared_error(y, yhat) / 2
    return y_mse



"""
Calculate the accuracy of the model on the training and test data.
Args:
        model (models.Sequential): The model to evaluate.
        x_data (np.ndarray): The input data to evaluate.
        y_true (np.ndarray): The true labels for the input data.
Returns:
        tuple: The training loss and accuracy respectively.
"""
def calculate_accuracy(model: models.Sequential, x_data: np.ndarray, y_true: np.ndarray) -> tuple[float, float]:
        train_loss, train_accuracy = model.evaluate(x_data, y_true, verbose=2)

        return (train_loss, train_accuracy)


"""
Shows the image given the pixel values.
Args:
    pixels (list[float]): A list of pixel values representing the image.
Returns:
    None: Displays the image using matplotlib.
"""
def show_image(pixels: list[float]):
    img = np.array(pixels).reshape(28, 28)
    plt.figure(figsize=(8, 4))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray_r')
    plt.title('Input to Model')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    

"""
Load a pre-trained model from the specified path.
Args:
    model_path (str): The path to the model file.
Returns:
    models.Sequential: The loaded Keras model.
"""
def load_model(model_path: str) -> models.Sequential: 
    model = models.load_model(model_path)
    print("Model loaded successfully from", model_path)
    return model