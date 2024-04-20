from tkinter import Tk, Toplevel
from datetime import datetime
from lib import SpriteHandler

class Display:
    def __init__(self) -> None:
        self.ConfigureTk()
        self.sprite_controller = SpriteHandler.SpriteController(self.root, self.chat_window)

    def ConfigureTk(self):
        self.root = Tk()
        self.chat_window = Toplevel()

        self.root.geometry(f"100x100+100+500")

        self.root.overrideredirect(True)
        self.root.lift()
        
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "black")

        self.chat_window.overrideredirect(True)
        self.chat_window.lift()
        
        self.chat_window.wm_attributes("-topmost", True)
        self.chat_window.wm_attributes("-disabled", True)
        
        self.chat_window.wm_attributes("-transparentcolor", "white")
        self.chat_window.wm_attributes("-alpha", 0)
        
        self.chat_window.maxsize(height=200)
    
    def Start(self):
        
        while True:
            try:
            
                self.sprite_controller.HandleAnimation()
            
            except Exception as e:
                
                with open("errorlog.txt","a") as f:
                    err_str = f"{datetime.now()}: {e.args}\n"
                    f.write(err_str)
                
                print(e); break;
        exit()

    

def main():
    d = Display()
    d.Start()

if __name__ == "__main__":
    main()