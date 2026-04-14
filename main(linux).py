from tkinter import Tk, Toplevel
from datetime import datetime
import lib.linux.SpriteHandler

class Display:
    def __init__(self) -> None:
        self.ConfigureTk()
        self.sprite_controller = lib.linux.SpriteHandler.SpriteController(
            self.root, 
            self.chat_window
        )

    def ConfigureTk(self):
        self.root = Tk()
        self.chat_window = Toplevel()

        # base position
        self.root.geometry("100x100+100+500")

        # remove window borders
        self.root.overrideredirect(True)
        self.root.lift()

        # always on top
        self.root.wm_attributes("-topmost", True)

        self.root.configure(bg="black")

        self.chat_window.overrideredirect(True)
        self.chat_window.lift()
        self.chat_window.wm_attributes("-topmost", True)

        self.chat_window.configure(bg="white")

        self.chat_window.wm_attributes("-alpha", 0)

        self.chat_window.maxsize(width=500, height=200)

    def Start(self):
        while True:
            try:
                self.sprite_controller.HandleAnimation()

            except Exception as e:
                with open("errorlog.txt", "a") as f:
                    err_str = f"{datetime.now()}: {e.args}\n"
                    f.write(err_str)

                print(e)
                break

        exit()


def main():
    d = Display()
    d.Start()


if __name__ == "__main__":
    main()
