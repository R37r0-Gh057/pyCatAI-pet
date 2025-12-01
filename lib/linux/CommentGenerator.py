import google.generativeai as genai
import subprocess
from threading import Thread
import tempfile
import os

from PIL import ImageGrab
import edge_tts

from lib.linux.Window_handler import Handler


BLOCKED_WINDOW_NAMES = [
    "chrome", "firefox", "brave", "edge",
    "login", "password", "auth", "settings",
    "obsidian", "uivicore", "vscode"
]


def is_secure_to_capture():
    pos = Handler.GetForegroundWindowPosition()
    if not pos:
        return False

    try:
        win_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode().strip()
        title = subprocess.check_output(["xdotool", "getwindowname", win_id]).decode().lower()

        for bad in BLOCKED_WINDOW_NAMES:
            if bad in title:
                return False

        return True

    except:
        return False



class Commenter:
    def __init__(self):
        self.API_KEY = ""
        self.MODEL = self.Configure()
        self.latest_response = None
    
    def Configure(self):
        genai.configure(api_key=self.API_KEY)
        return genai.GenerativeModel("gemini-2.5-flash")
    
    def TakeScreenshot(self):
        if not is_secure_to_capture():
            return None
        return ImageGrab.grab()
    
    def GenerateComment(self):
        prompt = (
            "This is a screenshot of my desktop. "
            "Pretend you are a cat and make a funny, sassy comment about what you see."
        )

        screenshot = self.TakeScreenshot()

        if screenshot is None:
            self.latest_response = "I can't see anything… your screen is private! 😼"
            return self.latest_response

        self.latest_response = self.MODEL.generate_content(
            [prompt, screenshot]
        ).text

        return self.latest_response
    
    def ThreadedSpeaker(self):
        Thread(target=self.SpeakComment, daemon=True).start()


    async def GenerateVoice(self, text, output_file):
        # Change voice here if you want
        voice = "en-US-JessaNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)


    def SpeakComment(self):
        if not self.latest_response:
            return
        
        #Edge-TTS requires an async
        import asyncio

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            temp_path = tmp.name

        #Run
        asyncio.run(self.GenerateVoice(self.latest_response, temp_path))

        #ffplay
        try:
            subprocess.run(
                ["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", temp_path]
            )
        finally:
            os.remove(temp_path)

