from os import listdir
from random import choice
from time import time

from PIL import Image, ImageTk
from tkinter import Label

from lib.WindowHandler import Handler
from lib.CommentGenerator import Commenter


class SpriteController:
    def __init__(self, root, chat_win_root) -> None:
        self.animation_frames: dict[str:list[str]] = self.LoadAnimations()
        
        self.commenter = Commenter()

        self.direction: str = "right"
        self.current_animation = self.animation_frames[f"idle_{self.direction}"]

        self.root = root
        self.chat_window_root = chat_win_root

        self.label = Label(self.root)
        
        self.chat_label = Label(self.chat_window_root)
        self.chat_response = None
        self.chat = False
        
        self.tts_begun = False

        self.moving = False
        
        self.fall    = False
        self.jumping = False

        self.idle_delay     = 0
        self.max_idle_delay = 2000

        self.move_distance     = 0
        self.max_move_distance = 200

        self.move_delay     = 0
        self.max_move_delay = 50

        self.frame_index = 0
        self.max_frame_index = len(self.current_animation) - 1

        self.delay_count = 0

        self.max_delay   = 200
        self.max_delay_0 = 700

        self.fall_frame_delay     = 0
        self.max_fall_frame_delay = 50

        self.pos_x = 20
        self.pos_y = 730

        self.ground_x = 20
        self.ground_y = 730

        self.target_x_max   = 0
        self.target_x       = 0
        self.target_y       = 0

        self.x_border       = 10
        self.x_border_right = 1500
        self.y_border       = 730

        self.jump_init_counter = time()
        self.chat_init_counter = time()

        self.jumped_to_window = False

    def GetScreenshotComment(self):
        self.moving = False
        self.jumping = False

        self.SetAnimation("sitting")

        last_x = self.pos_x
        last_y = self.pos_y

        self.pos_x = -50
        self.pos_y = -50

        self.UpdateRootWindow()
        self.tts_begun = True
    
        self.chat_response = self.commenter.GenerateComment()

        self.pos_x = last_x
        self.pos_y = last_y

        self.commenter.ThreadedSpeaker()
        self.tts_begun = False

    def UpdateChatWindowAlpha(self):
        self.chat_window_root.wm_attributes("-alpha", 1 if self.chat else 0)

    def UpdateChatWindow(self):
        if not self.chat:
            return
        
        self.chat_window_root.geometry(f"+{self.pos_x+100}+{self.pos_y}")

        self.chat_label.configure(text=self.chat_response)
        
        self.chat_label.configure(wraplength=300)
        self.chat_label.configure(anchor="w")
        
        self.chat_label.configure(background="yellow")
        self.chat_label.configure(foreground="red")

        self.chat_label.pack()
        self.chat_label.config(cursor=None)
        
        self.chat_window_root.update_idletasks()
        self.chat_window_root.update()

    def UpdateRootWindow(self):
        wind = "100x100"
        self.root.image = self.current_animation[self.frame_index]
        self.root.geometry(f"{wind}+{self.pos_x}+{self.pos_y}")
        self.label.configure(image=self.root.image, background="black")
        self.label.pack()
        self.label.config(cursor="none")

        self.root.update_idletasks()
        self.root.update()

    def SetAnimation(self, name):
        self.current_animation = self.animation_frames[name]
        self.max_frame_index = len(self.current_animation) - 1
        self.frame_index = 0

    def MakeFall(self):
        if self.pos_y != self.ground_y:
            if self.fall_frame_delay == self.max_fall_frame_delay:
                self.pos_y+=1
                self.fall_frame_delay = 0
                self.UpdateRootWindow()
            else:
                self.fall_frame_delay+=1
        else:
            self.fall = False
            self.jumped_to_window = False

    def CheckFallWindow(self):
        if self.fall:
            return
        if not self.jumped_to_window:
            return
        
        new_fg_window_location = Handler.GetForegroundWindowPosition()

        if new_fg_window_location:
            if self.target_x != new_fg_window_location[0] and self.target_y != new_fg_window_location[1]:
                
                self.fall = True
                
                self.moving = False
                self.chat = False
                self.SetAnimation("fall")

    def SetTargetWindow(self):
        target_window_location = Handler.GetForegroundWindowPosition()
        
        if target_window_location:
            self.target_x     = target_window_location[0]
            self.target_y     = target_window_location[1]
            self.target_x_max = target_window_location[2]
            return True
        else:
            return False

    def MakeJump(self):
        if self.jumping:
            if self.pos_x != self.target_x:
                self.pos_x = self.pos_x+1 if self.pos_x < self.target_x else self.pos_x-1
            if self.pos_y != self.target_y:
                self.pos_y = self.pos_y+1 if self.pos_y < self.target_y else self.pos_y-1
            else:
                self.pos_y-=70
                self.jumping = False
                self.jumped_to_window = True
                self.UpdateMovementBorder()
    
    def CheckJump(self) -> None:
        current = int(time() - self.jump_init_counter)
        if current >= 20:
            if self.SetTargetWindow():

                if self.pos_y != self.target_y-70:
                
                    self.jumping = True
                    self.moving = False
                    if self.pos_x > self.target_x:
                        self.SetAnimation("jump_left")
                    else:
                        self.SetAnimation("jump_right")

            self.jump_init_counter = time()
    
    def UpdateMovementBorder(self):
        self.x_border = self.target_x
        self.x_border_right = self.target_x_max

    def InitChat(self):
        
        current = int(time() - self.chat_init_counter)
        
        if current >= 60:
            self.chat_init_counter = time()
            return True
        
        return False
        
    
    def SetIdleAnim(self, direction=None):
        if direction:
            self.direction = direction
        
        self.moving = False
        self.move_distance = 0

        anim = choice((f"idle_{self.direction}", "sitting", "3_idle", "4_idle"))
        
        self.SetAnimation(anim)

    def HandleAnimation(self):
        if self.fall:
            self.MakeFall()
            return
        
        if not self.fall:
            self.CheckFallWindow()
        
        if not self.jumping:
            self.CheckJump()

        if self.jumping:
            self.MakeJump()

        if self.moving:
            if self.move_distance != self.max_move_distance:
                if self.move_delay != self.max_move_delay:
                    self.move_delay += 1
                else:
                    self.move_delay = 0
                    self.move_distance += 1

                    if self.direction == "right":
                        if not self.pos_x>=self.x_border_right:
                            self.pos_x+=1
                        else:
                            self.SetIdleAnim("left")
                    else:
                        if self.pos_x!=self.x_border:
                            self.pos_x-=1
                        else:
                            self.SetIdleAnim("right")

            else:
                self.move_distance = 0
                self.moving = False

                change_direction = choice([True, False])
                if change_direction:
                    self.direction = "right" if self.direction == "left" else "left"
                
                anim = choice([f"idle_{self.direction}", "sitting", "3_idle", "4_idle"])
                self.SetAnimation(anim)

                if self.InitChat():
                    self.chat = True
                    self.GetScreenshotComment()

        if not self.moving:
            if self.idle_delay == self.max_idle_delay:
                self.moving = True
                self.chat = False
                self.idle_delay = 0
                self.SetAnimation(f"move_{self.direction}")
            else:
                self.idle_delay += 1
        self.UpdateFrame()

    def UpdateFrame(self):
        self.frame_index = (
            0 if self.frame_index >= self.max_frame_index else self.frame_index
        )

        if self.delay_count == self.max_delay:
            self.delay_count = 0
            if not len(self.current_animation) == 1:
                self.frame_index += 1
        else:
            self.delay_count += 1

        self.chat_window_root.wm_attributes("-alpha", 1 if self.chat else 0)

        self.UpdateChatWindow()
        if not self.tts_begun:
            self.UpdateRootWindow()
    
    def LoadAnimations(self):
        anim_dict = {}

        for animation_directory in listdir("sprites"):
            dir_path = f"sprites/{animation_directory}/"

            file_list = listdir(dir_path)

            for image_file in file_list:

                pil_image = Image.open(dir_path + image_file)
                resized_image = pil_image.resize((100,100))
                tk_image = ImageTk.PhotoImage(resized_image)

                if animation_directory in anim_dict:
                    anim_dict[animation_directory].append(tk_image)
                else:
                    anim_dict[animation_directory] = [tk_image]
        return anim_dict

