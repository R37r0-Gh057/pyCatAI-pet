# pyCatAI-pet (v0.9)
A Windows based AI powered desktop pet written in [Python](https://python.org/). It can move around on your screen and jump on top of active program windows. And with the help of [Google's Gemini Vision model](https://blog.google/technology/ai/google-gemini-ai/#sundar-note), it can generate funny comments on current on-screen activity by taking screenshots of your screen every minute.

[Watch video demo here](https://youtu.be/Ep7Un8vAwbI)
<p align="center">
  <a href="https://github.com/R37r0-Gh057/pyCatAI-pet">
    <img alt="logo" src="logo.gif" height=400 width=700>
  </a>
</p>

![Python](https://img.shields.io/badge/python-3.11-green.svg) ![](https://shields.io/badge/python-tkinter-blue) ![](https://shields.io/badge/win32-api-blue) ![](https://shields.io/badge/google-gemini_vision-blue)

> [!NOTE]
> All of the cat sprites used in this project are not mine. They have been taken from [here](https://luizmelo.itch.io/pet-cat-pack).

## Current Features:
* Uses [tkinter](https://docs.python.org/3/library/tkinter.html) to display sprite images and text on screen.
* Uses [win32gui](https://pypi.org/project/win32gui/) library to access and utitlize the [Windows API](https://learn.microsoft.com/en-us/windows/win32/api/) to get the active program windows and their X, Y positions.
* Uses [pyttsx3](https://pypi.org/project/pyttsx3/) library for Text-to-speech.
* Uses [Google's Gemini Vision](https://blog.google/technology/ai/google-gemini-ai/#sundar-note) model for generating comments.
### To do:
- [ ] Add support for linux.
- [ ] Add better TTS.
- [ ] Add & use more idle animations.
- [ ] Make the sprite draggable using mouse.
- [ ] Make the sprite stick on other program window borders.

## Getting started

Install [Python](https://python.org/) on your machine if you haven't already.

Download this repository manually, or if you have [git](https://git-scm.com/) installed::

```
git clone https://github.com/R37r0-Gh057/pyCatAI-pet

```
Once inside the directory, open your terminal enter the following commands to install the necessary libraries:
```
pip install -r requirements.txt
```

## Usage

> [!IMPORTANT]  
> Make sure that you have generated your own [Gemini API key](https://aistudio.google.com/app/apikey) and placed it in the script:
https://github.com/R37r0-Gh057/pyCatAI-pet/blob/fa142662c4cc735ebe82a3d457dc0b3b78f78752/lib/CommentGenerator.py#L10

Run the `main.py` file from terminal:
```
python main.py
```

## Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)

If you want to suggest a new feature or functionality then you can open a new issue with the `"enhancement"` title.

If you want to add features or enhance existing code by yourself then feel free to open a **Pull Request**:

1. Fork this repository
2. Create a separate branch
3. Make your changes
5. Open pull request

You can get started by checking the [currently open issues](https://github.com/R37r0-Gh057/pyCatAI-pet/issues), or create new ones.

## Contact

Feel free to reach out to me on discord: @retr0_gh0st
