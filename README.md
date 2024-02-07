# Chinese Handwritten Character Recognition Web App

The main purpose of the project was to build an web app where users can test their Chinese knowledge by translating an English sentence into Chinese by writing out every character by hand. Sadly, most study apps require only characters written on the keyboard which trains digital writing skills by neglects the handwritten aspect of Chinese. As a result, a neural network architecture was built ontop of the Convolutonal Neural Netowork architecture to recognize handwritten Chinese characters from the HSK-1 vocabulary list. Then, a Vue.js frontend and a Flask backend were created to provide an easy-to-use interface for the user to perform translation tasks by handwritting each character. 

![Demo](/figs/demo.png)

## Installing and Executing

To install packages and libraries, please refer to the specific part of the project. Each folder in the project contains a separate function and has its own environment that you can install.

## Description of Project Folders

### Chinese Handwriting Recognizer

A convolutional neural network that recognizes a hantwritten chinese character out of the 178 characters of the HSK 1 exam with a high accuracy. You do not need to train this model yourself for the chinese handwriting recognizer webapp to work. Download only the [UI](chinese_handwriting_interface) and the [Server](chinese_handwriting_server) which contains an already pretrained chinese handwriting recognizer model shown in this repository.

#### Data
The model was trained on a subset of the [CASIA Online and Offline Chinese Handwriting Database](https://nlpr.ia.ac.cn/databases/handwriting/Download.html) which only includes characters present in the HSK 1 (Hanyu Shuiping Kaoshi) exam. The 178 characters were extracted in equal numbers and uploaded to kaggle for public access and reproducibility of results.

### Chinese Handwriting Server

This is the backend for the [Chinese Handwriting UI](chinese_handwriting_interface).

It takes the handwritten character submitted by user and uses the [machine learning model](chinese_handwriting_recognizer) trained beforehand to recognize that character. Then, the server sends it digitally to the frontend. Thus, activing as a brigde between the model and the user interface.

### Chinese Handwritting UI

The UI for a chinse testing app asks the user to solve translation questions and provides an interefact to handwrite each characters in the sentence.

This directory is linked to the [Chinese Handwriting Server](chinese_handwriting_server) which processes the characters written, and recognizes them using the custom [machine learning model](chinese_handwriting_recognizer).

