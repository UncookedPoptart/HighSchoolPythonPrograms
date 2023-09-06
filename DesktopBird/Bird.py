from tkinter import *
import time
import random
import math
import pyautogui as gui
import os

class pet():
    def __init__(self):
        # create a window
        self.window = Tk()
        
        # creates dimensions
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.gif_dimx = 114
        self.gif_dimy = 84
        
        # creates objective
        self.objective = None
        self.xdest = 20
        self.ydest = 0
        self.wait_time = 3
        
        # this is his name
        self.name = 'eduardo'
        
        # creates bird stats
        self.facing_right = True
        self.speech_options = ['']
        
        # adds images
        self.walking_right = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(12)] # replace file paths with your own gifs
        self.walking_left = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(12)]
        self.flying_right = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(4)]
        self.flying_left = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(4)]
        self.idle_right = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(18)]
        self.idle_left = [PhotoImage(file=None, format='gif -index %i' % (i)) for i in range(18)]
        self.frame_index = 0
        self.img = None

        # timestamp to check whether to advance frame
        self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='black')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # create a label as a container for our image
        self.label = Label(self.window, bd=0, bg='white', borderwidth=0)
        #self.label.config(bg='systemTransparent')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.y = self.height-(self.gif_dimy+70)
        self.window.geometry(str(self.gif_dimx)+'x'+str(self.gif_dimy)+'+{x}+{y}'.format(x=str(self.x), y=str(self.y)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()

    def update(self):

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.05:
            diftime = time.time()-self.timestamp
            self.timestamp = time.time()
            
            #chooses which goal the pet wants
            if self.objective == None:
                self.frame_index = 0
                # chooses which goal the pet has
                self.frame_index = 0
                option = random.randint(1,8)
                if option < 5:
                    self.objective = 'walking'
                    self.xdest = random.randint(0, self.width-self.gif_dimx)
                elif option == 5:
                    self.objective = 'flying'
                    self.ydest = random.randint(0, self.height/2)
                    self.xdest = random.randint(0, self.width-self.gif_dimx)
                elif 5 < option and option < 8:
                    self.objective = 'idling'
                    self.wait_time = random.randint(1,5)
                elif option == 8:
                    self.objective = 'talking'
                
                    
            #annoys the users mouse
            if self.objective == 'annoying':
                x,y = gui.position()
                self.xdest = x - int(self.gif_dimx/2)
                self.ydest = y - int(self.gif_dimy/2)
                    
            #walks the pet to x position
            if self.objective == 'walking':
                if self.xdest > self.x:
                    self.x += 3
                    self.img = self.walking_right[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 12
                    self.facing_right = True
                if self.xdest < self.x:
                    self.x -= 3
                    self.img = self.walking_left[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 12
                    self.facing_right = False
                if self.xdest <  self.x + 3 and self.xdest > self.x -3:
                    self.objective = None
            
            #flies pet to x,y position
            if self.objective == 'flying' or self.objective == 'annoying':
                dx = self.xdest-self.x
                if dx == 0:
                    dx = 1
                degree = math.atan2(self.ydest-self.y,dx)
                dx = int(12*math.cos(degree))
                dy = int(12*math.sin(degree))
                if dx > 0:
                    self.img = self.flying_right[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 4
                    self.facing_right = True
                else:
                    self.img = self.flying_left[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 4
                    self.facing_right = False
                self.y += dy
                self.x += dx
                if self.xdest <  self.x + 6 and self.xdest > self.x -6 and self.ydest <  self.y + 6 and self.ydest > self.y -6:
                    if self.ydest < int(self.height/2) and self.objective != 'annoying':
                        self.objective = 'flying'
                        self.ydest = self.height-(self.gif_dimy+70)
                        self.xdest = random.randint(0, self.width-self.gif_dimx)
                    elif self.objective != 'annoying':
                        self.objective = None
            
            #plays bird idle animation for specified time
            if self.objective == 'idling':
                if self.facing_right:
                    self.img = self.idle_right[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 18
                else:
                    self.img = self.idle_left[self.frame_index]
                    self.frame_index = (self.frame_index + 1) % 18
                if self.wait_time <= 0:
                    self.objective = None
                self.wait_time -= diftime
                
            #controls the birds speech 
            if self.objective == 'talking':
                os.system('say \"'+str(self.speech_options[random.randint(0,len(self.speech_options)-1)])+'\"')
                self.objective = None
                

        # create the window
        self.window.geometry(str(self.gif_dimx)+'x'+str(self.gif_dimy)+'+{x}+{y}'.format(x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update)
                        
pet()