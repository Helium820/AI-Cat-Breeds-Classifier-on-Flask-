# AI Cat Breeds Classifier on Flask Apps  

  
<br/>

## Introduction

**We all love cats.**  
The Cat Breeds Classifier allows us to upload a cat image and obtain the possible breeds for that cat, along with confidence percentages. These user-firendly apps offer accessible and intuitive platform for leveraging the ability of computer vision to analyze the categories of cat you may want to know.

<br/>

## Demo
You can click the button and upload the image, then the result will show below.  
Video Demo:  [YouTube](https://youtu.be/Ouw5TsYeAEA)

https://github.com/user-attachments/assets/a565ec1c-5514-4437-bd56-51dcebbf1750




<br/>

## Dataset

The Cat Breeds Classifier performs classification on different cat breeds, including the six common cat breeds: **american shorthair, bengal, maine coon, ragdoll, scottish fold, sphinx**, based on the dataset from [Kaggle](https://www.kaggle.com/datasets/solothok/cat-breed/data). However, more than 40 cat breeds we can identify in the World, it is possible for us to expand more categories and improve robustness of the applications in the future.

<br/>

## Motivation

As my final project for [Harvard CS0x course](https://pll.harvard.edu/course/cs50-introduction-computer-science), and my background in computer vision, I combined website development and image classification into application. Learning new technologies and hone my software development skills, while tackling interesting problem with AI solutions.

<br/>

## Repository Structure

The repository has the following structure:

```
AI-Cat-Breeds-Classifier-on-Flask/
├── app.py
├── Cat_Classification.ipynb
├── templates/
│   ├── temp.html
│   └── index.html
├── static/
│   ├── styles.css
│   ├── uploads/
│   │   ├── demo_image.jpg
│   │   ├── static_uploaded.jpg
│   │   └── ...
├── weights/
│   ├── save_at_{epochs}.h5.keras
│   └── ...
├── cat_breed/
│   │   ├── TEST/ ...
│   │   └── TRAIN/ ...
└── README.md
```

<br/>

## Usage

### Clone the repository

- ``git clone``
- ``unzip folder``
- ``cd AI-Cat-Breeds-Classifier-on-Flask/``

### Modify the classification model
Simplest model ran record is saved in ``Cat_Classification.ipynb``. AlexNet and more advanced pretrained models can be obtain from [Keras](https://keras.io/api/applications/) for computer vision tasks.  
Model selection done by ``app.py``.

### Run the App
- ``flask run``
- or ``python -m app.py``
- or ``http-server``

<br/>

## TODO

- Consider more cat categories 
- Improve data quality
- Image preprocessing to improve model robustness
- Improve model performance by testing other available open source model architectures
- From image classification to cat detection (of cat position)
- From image to video
- Features and tools on website to provide a better user-interface


