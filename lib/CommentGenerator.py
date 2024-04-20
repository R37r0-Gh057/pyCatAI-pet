import google.generativeai as genai
import pyttsx3
from threading import Thread

from PIL import ImageGrab

class Commenter:
    def __init__(self):
        # update your API key
        self.API_KEY = ""
        self.MODEL = self.Configure()

        self.latest_response = None
    
    def Configure(self):
        genai.configure(api_key=self.API_KEY)
        model = genai.GenerativeModel("gemini-pro-vision")

        return model
    
    def TakeScreenshot(self):
        screenshot = ImageGrab.grab()
        return screenshot
    
    def GenerateComment(self):
        prompt = "this is a screnshot of my computer screen. Pretend that you are a cat and do your best to generate a funny comment based on what you see."
        screenshot = self.TakeScreenshot()

        self.latest_response = self.MODEL.generate_content([prompt, screenshot]).text

        return self.latest_response
    
    def ThreadedSpeaker(self):
        _ = Thread(target=self.SpeakComment)
        _.run()

    def SpeakComment(self):
        tts = pyttsx3.init()
        tts.say(f'<pitch middle="10">{self.latest_response}</pitch>')
        tts.runAndWait()