# Dress Color Matcher Web App

A Flask-based web application that allows users to upload an existing dress and new dresses they like, and finds the best matching new dress based on color similarity. The app uses KMeans clustering to extract the main color of each dress and compares the main color of the existing dress with the new ones.

## Features
- Upload an existing dress image.
- Upload multiple new dress images.
- Automatically extracts the main color of each image.
- Uses KMeans clustering to analyze color patterns.
- Matches the best new dress based on color similarity.
- Displays the best-matched dress.

## Technologies Used
- **Backend**: Python, Flask
- **Image Processing**: OpenCV, KMeans (from scikit-learn)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: KMeans clustering for color matching
- **Web Framework**: Flask

##  Steps to Run the Application
1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/KishoreBharathiB/Dress-Color-Matcher.git
   cd Dress Color Matcher
   ```
2. Run the project
  ```bash
  python app.py
  ```

## How to Use the Application
Upload your Existing Dress: Click on the "Choose File" button to upload your existing dress image. This image will be used as the reference for matching.
Upload New Dresses: Click on the "Choose Files" button to upload multiple images of new dresses that you like.
Find the Best Match: After uploading the images, click the "Find Best Match" button to find the best-matched dress based on color similarity.
View the Best Match: If a matching dress is found, the image of the best-matched dress will be displayed below the button.

## Image Processing Details 
KMeans Clustering: The KMeans algorithm is used to perform color clustering in the image. It divides the image into k clusters (4 by default) and selects the dominant color.
Euclidean Distance for Matching: Once the main colors are extracted, the app calculates the Euclidean distance between the existing dress color and the new dress colors. The smallest distance indicates the best match.

## Future Enhancements
Color Sensitivity Tuning: Allow users to adjust the sensitivity of the color matching to get a wider or more specific range of matches.
User Authentication: Add user authentication to allow users to save their preferences and upload history.
Advanced Color Matching Algorithm: Use more advanced techniques like perceptual color difference metrics for better matching


This `README.md` provides a comprehensive guide for setting up, running, and understanding the functionality of your "Dress Color Matcher" web application.


