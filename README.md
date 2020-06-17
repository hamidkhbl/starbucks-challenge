# Starbucks Recommendation System


## Table of Contents

1. [Installation](#installation)
2. [Project Definition](#def)
3. [File Description](#file-description)
4. [Analysis](#Analysis)
5. [Methodology](#Methodology)
6. [Results](#results)
7. [Conclusion](#Conclusion)
8. [Web-app Guide](#web-app)
9. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
1. Install the requirments:
>`pip install -r requirements.txt`

2. Run the Extract, Transform, Load (ETL) pipeline:<br>
> `python ..\data\process_data.py` <br>

3. Run ML pipeline: <br>
>`python ..\model\train_classifier.py` <br>
this command trains a Random Forest Classifier on the clean data and exports the model to a pickle file.
4. Run the Flask application <br>
> `Flask run` <br>
Go to http://localhost:5000/

## Project Definition <a name="def"></a>
* ### Project Overview
> In this project, we analyze Starbucks data to see how users are using offers. Also, we predict which offers should be sent to a user and if they will complete it or not.
* ### Problem Statement
>The person who is responsible for sending offers needs assistance to send targetted offers to people. This application can help him/her to send better offers.

## File Descriptions <a name="file-description"></a>
> There are 3 main folders in this project:
* app: contains files for the web application
* data: contains data cleaning python file and also JSON and SQL files
* Model: Contains classifier and model files

## Analysis <a name="Analysis"></a>
* ### Data Exploration and Visualization
> There is a menu in the web app for exploritory data visualization.

## Results <a name="results"></a>
> The person whi is responsible of sending offers can use this web app to send targetted offers to group of users.



## Web-app Guide <a name="web-app"></a>
There are five menu in the app:
* Find best offer for a user
* Predict offer complition
* Data Visualization
* Data sample
* About


## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
>


