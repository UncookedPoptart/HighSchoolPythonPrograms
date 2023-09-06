import openai
import time
import pyautogui as gui
from tkinter import *
from pynput import *
import random

"""personalized variables"""

openai.api_key = None # enter openai api key as a string
ALLOWED_PRESIDENTS = ['trump', 'obama'] # trump, obama
TEMPERATURE = 0.95
SCREEN_HEIGHT_ADJUSTMENT = 110 # will need modification to fit screen (measured in pixels)
WAIT_TIME = 30 # time between messages

"""main variables"""

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

on = False
gui.PAUSE = 0.001

"""classes"""

class president():
    
    def __init__(self, qualities, x, y):
        
        self.qualities = qualities
        self.x = x
        self.y = y

"""definitions"""

def chat_gpt(prompt):
    
    # Set the model and prompt
    model_engine = 'text-davinci-003'

    # Set the maximum number of tokens to generate in the response
    max_tokens = 64

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=TEMPERATURE,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].text

def respond(prompt, person, enemy):
    
    return check_message(chat_gpt('respond as if '+enemy+' is saying \"'+prompt+'\"'+get_line(person)+' in under 48 words and without hashtags'))

def get_line(qualities):
    
    line = ''
    for word in qualities:
        line += ' and ' + word
        
    return line

def check_message(message):
    
    nonos = ['\"', 'Trump:', 'Obama:', 'My Response:','My response would be']
    x = 0
    while x < len(message):
        if message[x] in nonos:
            message = message[:x] + message[x+1:]
            x -= 1
        x += 1
        
    return message

def write_message(message, x, y):
    
    gui.click(x,y)
    gui.typewrite(message)
    gui.hotkey('enter')
    
def on_release(key):
    global on
    if key == keyboard.Key.esc:
        on = not on
        
def get_pres(current):
    
    while True:
        pres = random.choice(ALLOWED_PRESIDENTS)
        if pres != current:
            return pres
        
"""top level"""

keyboard_listener = keyboard.Listener(on_release = on_release).start()

# personalities

trump = [
    'you are former us republican president donald trump',
    'you are not very nice',
    'you like to trash talk barack obama'
]

obama = [
    'you are former us democratic president barack obama',
    'you sometimes bring up random videogame conversation topics',
    'you like to trash talk donald trump'
]

speakers = {'trump': president(trump, width/4, height-SCREEN_HEIGHT_ADJUSTMENT), 'obama': president(obama, 3*width/4, height-SCREEN_HEIGHT_ADJUSTMENT)}

# starting variables

spoken = 'obama'
speaker = 'trump'
message = 'whats up'

# main loop

timestamp = time.time() - WAIT_TIME
while True:
    
    if time.time() > timestamp + WAIT_TIME and on:
         
        print(speaker)
        print(message := respond(message, speakers[speaker].qualities, spoken))
        write_message(message, speakers[speaker].x, speakers[speaker].y)
        spoken = speaker
        speaker = get_pres(speaker)
        timestamp = time.time()