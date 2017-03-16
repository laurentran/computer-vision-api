# computer-vision

The project includes an Azure Function to ping the Cognitive Services Computer Vision API for tagging images with image content.  **tagImages** is blob-triggered when an image is added to a blob, and then writes the results to Azure Table Storage.

For logo recognition, this project also uses Azure Functions to call a custom trained IRIS endpoint.  **recognizeLogos** is also blob-triggered and sends the image to IRIS to recognize the logo present in the image.

In addition to using IRIS, this project leverages Azure Machine Learning for custom trained logo classifiers.  Inside the custom-classifiers folder, `extractKeypoints.py` uses scikit-image to extract daisy features from the training set.  The resulting output file (`keypoints.csv`) file is uploaded to Azure ML to then cluster the keypoints into visual words, quantize the images, and train a classifier.  This shows a proof-of-concept for 2 different logo classes and can extend to multiple.  The code in `createHistograms.py` was integrated in the Azure ML workflow inside the "Execute Python Script" module to quantize the images into feature vectors.

# License
Licensed using the MIT License (MIT); Copyright (c) Microsoft Corporation. For more information, please see [LICENSE](https://github.com/laurentran/computer-vision/blob/master/LICENSE)
