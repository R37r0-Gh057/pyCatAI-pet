import os
import subprocess


class Handler:
    @classmethod
    def GetForegroundWindowPosition(cls):
        #detects if your on kde if not it trys a universal method
        if cls.is_kde():
            pos = cls.try_kde_dbus()
            if pos is not None and cls._safe(pos):
                return pos
    
        pos = cls.try_xdotool()
        if pos is not None and cls._safe(pos):
            return pos
        
        return None

    @staticmethod
    def is_kde():
        desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
        if "kde" in desktop:
            return True
        try:
            subprocess.check_output(["pgrep", "-x", "kwin_x11"])
            return True
        except:
            return False

    @staticmethod   
    def _safe(pos):
        left, top, right, bottom = pos
        width  = right  - left
        height = bottom - top

        if left < 0 or top < 0:
            return False

        # Reject windows too small to stand on
        if width < 100 or height < 100:
            return False
        if top < 50:  
            return False
        
        if left == 0 and top == 0:
            return False

        return True

    @classmethod
    def try_xdotool(cls):
        try:
            win_id_dec = int(
                subprocess.check_output(["xdotool", "getactivewindow"])
                .decode().strip()
            )
            win_id_hex = f"0x{win_id_dec:08x}"

            lines = subprocess.check_output(["wmctrl", "-lG"]).decode().splitlines()

            for line in lines:
                parts = line.split()
                if parts[0].lower() == win_id_hex:
                    left = int(parts[2])
                    top = int(parts[3])
                    width = int(parts[4])
                    height = int(parts[5])
                    return (left, top, left + width, top + height)


            return None
        except:
            return None

    @classmethod
    def try_kde_dbus(cls):
        try:
            win_path = subprocess.check_output([
                "qdbus", "org.kde.KWin", "/KWin", "org.kde.KWin.activeWindow"
            ]).decode().strip()

            if not win_path:
                return None

            window_id = win_path.split("/")[-1]

            info_raw = subprocess.check_output([
                "qdbus", "org.kde.KWin", "/KWin", "getWindowInfo", window_id
            ]).decode()

            info = {}
            for line in info_raw.splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    info[k.strip()] = v.strip()

            x = int(info.get("x", 0))
            y = int(info.get("y", 0))
            width = int(info.get("width", 0))
            height = int(info.get("height", 0))
            return (x, y, x + width, y + height)

        except:
            return None


if __name__ == "__main__":
    print(Handler.GetForegroundWindowPosition())
