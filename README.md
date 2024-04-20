# pyCatAI-pet
A Windows based AI powered desktop pet written in [Python](https://python.org/). It can move around on your screen and jump on top of active program windows. And with the help of [Google's Gemini Vision model](https://blog.google/technology/ai/google-gemini-ai/#sundar-note), it can generate funny comments on current on-screen activity by taking screenshots of your screen every minute.

[Watch video demo here](https://youtu.be/Ep7Un8vAwbI)
<p align="center">
  <a href="https://github.com/R37r0-Gh057/pyCatAI-pet">
    <img alt="logo" src="logo.gif" height=400 width=700>
  </a>
</p>

![Python](https://img.shields.io/badge/python-3.11-green.svg) ![](https://shields.io/badge/python-tkinter-blue) ![](https://shields.io/badge/win32-api-blue) ![](https://shields.io/badge/google-gemini_vision-blue)

# About
> [!NOTE]
> All of the cat sprites used in this project are not mine. They have been taken from [here](https://luizmelo.itch.io/pet-cat-pack).

Current Features:
* Uses [tkinter](https://docs.python.org/3/library/tkinter.html) to display sprite images and text on screen.
* Uses [win32gui](https://pypi.org/project/win32gui/) library to access and utitlize the [Windows API](https://learn.microsoft.com/en-us/windows/win32/api/) to get the active program windows and their X, Y positions.
* Uses [pyttsx3](https://pypi.org/project/pyttsx3/) library for Text-to-speech.
* Uses [Google's Gemini Vision](https://blog.google/technology/ai/google-gemini-ai/#sundar-note) model for generating comments.

# Getting started

> [!IMPORTANT]  
> Make sure to [generate your own Gemini API key](https://aistudio.google.com/app/apikey) and place it in this file here:
https://github.com/R37r0-Gh057/pyCatAI-pet/blob/fa142662c4cc735ebe82a3d457dc0b3b78f78752/lib/CommentGenerator.py#L10

Now download and extract this repository manually or run the following commands if you have git installed:

`git clone https://github.com/R37r0-Gh057/pyCatAI-pet`

`cd pyCatAI-pet`

Once you're inside the directory, run the following command in your terminal:

`pip install -r requirements.txt`

# Usage
Run the `main.py` file to start the pet.
``python main.py``
