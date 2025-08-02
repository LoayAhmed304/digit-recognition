import numpy as np

from tensorflow.keras import models, layers
from tensorflow.keras.datasets import mnist
from utils import calculate_accuracy

"""
Load data and serialize it from MNIST dataset.
Returns:
        tuple: Training and test data as numpy 1-D arrays.
"""
def load_data() -> tuple:
        # Load data
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        
        # Serialize it
        X_train = X_train.reshape(-1, 28*28).astype("float32") / 255.0
        X_test  = X_test.reshape(-1, 28*28).astype("float32") / 255.0
        
        # Check whether the data is scaled
        assert X_train.min() >= 0.0 and X_train.max() <= 1.0, "Data is not scaled"
        
        return (X_train, y_train), (X_test, y_test)

"""
Check whether the data is scalked.
Args:
        X (np.ndarray): Data to check.

"""
def test_data(X: np.ndarray) -> None:
        assert X.min() >= 0.0 and X.max() <= 1.0, "Data is not scaled"

"""
Build the model NN architecture: 2 hidden relu layers with 256 neurons each.
Dropout layer with 0.45 dropout rate.
Output:
        models.Sequential: The built model.
""" 
def build_model() -> models.Sequential:
        model = models.Sequential([
        layers.Input(shape=(784,)),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.45),
        layers.Dense(256, activation='relu'),
        layers.Dense(10, activation='softmax')

        ], name=('digits_model'))
        
        return model

"""
Compile the model with Adam optimizer and sparse categorical crossentropy loss.
Args:
        model (models.Sequential): The model to compile.
"""
def compile_model(model: models.Sequential) -> None:
        model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

"""
Fit the model with the training data. Epochs is set to 20 by default.
"""
def fit_model(model:models.Sequential, X_train: np.ndarray, y_train: np.ndarray) -> None:
        model.fit(X_train, y_train, epochs=20, verbose=2)


if __name__ == "__main__":
        # 1) Load data
        print("\nLoading MNIST dataset...")
        (X_train, y_train), (X_test, y_test) = load_data()
        
        # 2) Check whether the data is scaled
        test_data(X_train)
        test_data(X_test)
        print("\nData loaded successfully and is well scaled.")

        # 3) Build build the model
        model = build_model()
        
        # 4) Compile the model
        compile_model(model)
        print("\nModel built and compiled successfully.")

        # 5) Fit the model
        fit_model(model, X_train, y_train)
        print("Model training completed.\n")
        
        print("\nModel evaluation:")
        (train_loss, train_accuracy) = calculate_accuracy(model, X_train, y_train)
        (test_loss, test_accuracy) = calculate_accuracy(model, X_test, y_test)
        print(f"Training accuracy: {train_accuracy:.4f}\t Training loss: {train_loss:.4f}")
        print(f"Test accuracy: {test_accuracy:.4f}\t Test loss: {test_loss:.4f}")

        print("\nSaving Model.....")
        model.save('../models/mnist_model.h5')
