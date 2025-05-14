# DEPI-project
📘 Overview

This project demonstrates a basic implementation of a feedforward neural network using PyTorch to classify a simple 2D dataset. 
The notebook includes:
- Dataset generation using make_moons
- Neural network model definition
- Training with backpropagation
- Evaluation of accuracy and visualization of decision boundaries

🧠 Project Structure

The notebook covers the following main steps:

1- Data Preparation
 - Synthetic data is generated using make_moons from sklearn.datasets.
 - The data is split into training and test sets.

2- Model Definition
 - A simple neural network is defined using PyTorch's nn.Sequential.

3- Training Loop
 - The model is trained using a standard cross-entropy loss and stochastic gradient descent (SGD).
 - Training accuracy and loss are monitored over epochs.

4- Visualization
 - The decision boundary of the trained model is plotted.
 - Training history (loss and accuracy over epochs) is visualized.

🛠️ Requirements

To run this notebook, install the following dependencies:
( pip install torch matplotlib scikit-learn numpy)

🚀 How to Run

1- Open the notebook in a Jupyter environment.

2- Run all cells in sequence.

3- Observe the model training and decision boundary plots.

📊 Results

The model is expected to achieve high classification accuracy on the simple binary dataset (make_moons), demonstrating the effectiveness of basic neural networks in non-linear classification tasks.

📁 Files

nb2.2.ipynb – Jupyter notebook containing code, training, and visualization.

🧾 License

This project is an open source project made by DEPI Students. Feel free to use and modify it for educational or personal purposes.
