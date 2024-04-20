from win32gui import GetForegroundWindow, GetWindowRect

class Handler:
    @classmethod
    def GetForegroundWindowPosition(cls):
        window = GetForegroundWindow()
        
        if window:
            window_rect = GetWindowRect(window)
            return (window_rect[0], window_rect[1], window_rect[2]) \
                if window_rect[0] >= 40 and window_rect[1] >= 50 else None
        
        return None

if __name__ == "__main__":
    print(Handler.GetForegroundWindowPosition())