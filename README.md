# Fake News Detection ML Model and Web App

## Overview

This project aims to detect fake news using machine learning techniques and provide a web application interface for users to interact with the model. The model achieves an accuracy of 94.7% using logistic regression and lemmatization.

## Dataset

The dataset used for training the model is called WELFake. It consists of 72,134 news articles, with 35,028 labeled as real and 37,106 labeled as fake. The dataset is a combination of four popular news datasets (Kaggle, McIntire, Reuters, BuzzFeed Political) to prevent overfitting and improve model generalization. Each entry in the dataset contains a serial number, title, text, and label (0 for fake news and 1 for real news). It is published in IEEE Transactions on Computational Social Systems (doi: 10.1109/TCSS.2021.3068519).

## Backend

The backend of the project is implemented using Django. Here's an overview of the directory structure:
```
fake_news_detection_project/
│
├── fake_news_detection_project/
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
└── news_detection/
├── migrations/
├── models.py
├── urls.py
├── views.py
└── ...
```

- `dataset/News_dataset.csv`: The dataset used for training the machine learning model.
- `ML Model/`: The trained machine learning model.
- `README.md`: The file you are currently reading.
- `requirements.txt`: The list of dependencies required to run the web application.

## Prerequisites

To run this web application locally, you need to have the following dependencies installed:

- Django==3.2.10
- joblib==1.1.0
- scikit-learn==0.24.2

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt
```

The `fake_news_detection_project` directory contains the Django project settings and configurations. Inside this directory, a Django app named `news_detection` is created to handle the functionalities related to fake news detection.

To save the model, it should be placed inside the `news_detection` folder. You can modify the settings of the model in `news_detection/models.py`.

## Instructions

1. Ensure you have Python and Django installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the Django development server.
   ```bash
   python manage.py runserver
   ```
Access the web application through the provided URL.
##Credits:-
- Dataset: WELFake (IEEE Transactions on Computational Social Systems, doi: 10.1109/TCSS.2021.3068519)
- Framework: Django

Feel free to explore the code and contribute to improving the project!
