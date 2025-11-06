# AI-Powered Image Classification using Deep Learning

A web application that uses a deep learning model trained on the CIFAR-10 dataset to classify images into 10 different categories. The application provides a clean, user-friendly interface for uploading images and getting real-time predictions.

## Features

- **Easy-to-use Interface**: Simple drag-and-drop or click-to-upload functionality
- **Real-time Preview**: See your uploaded image before classification
- **Fast Predictions**: Quick classification using a pre-trained CNN model
- **Supported Formats**: Handles PNG, JPG, and GIF image formats
- **Responsive Design**: Works well on both desktop and mobile devices

## CIFAR-10 Classes

The model can classify images into these 10 categories:
- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

## Technical Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Deep Learning**: TensorFlow/Keras CNN model
- **Model Architecture**: Custom CNN trained on CIFAR-10 dataset

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/shubham-guptaaa/AI-Powered-Image-Classification-using-Deep-Learning.git
cd AI-Powered-Image-Classification-using-Deep-Learning
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your web browser and visit:
```
http://127.0.0.1:5000
```

## Usage

1. Click the "Choose File" button or drag and drop an image
2. Preview your image in the interface
3. Click "Upload and Predict" to get the classification result
4. View the prediction result displayed below the image


## Model Information

The classifier uses a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. The model achieves good accuracy on the standard CIFAR-10 test set and can handle real-world images through appropriate preprocessing.

## Limitations

- Best results with images similar to CIFAR-10 style
- Maximum file size: 5MB
- Supported formats: PNG, JPG, GIF
- Images are preprocessed to match CIFAR-10 dimensions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Shubham Gupta
- GitHub: [@shubham-guptaaa](https://github.com/shubham-guptaaa)