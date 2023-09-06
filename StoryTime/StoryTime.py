import random
import os 

class Word():
    
    def __init__(self, text):
        
        self.text = text
        self.afters = []
        
    def add_after(self, text):
        self.afters.append(text)
        
    def get_after(self):
        return self.afters[random.randint(0,len(self.afters)-1)]
    
    def get_text(self):
        return self.text
    
    def after_length(self):
        return len(self.afters)
        
dictionary = {}

# reads file into the dictionary
prev_word = Word('')
dictionary[''] = prev_word

with open(None) as f: # insert file with writing here
    line = f.readline()
    line = line.split()
    for w in line:
        curr_word = Word(w)
        if w not in dictionary.keys():
            dictionary[w] = curr_word
        dictionary[prev_word.get_text()].add_after(w)
        prev_word = curr_word
    f.close()

# writes new text
word = ''
story = ''
while(dictionary[word].after_length() > 0 and len(story) < 1000):
    word = dictionary[word].get_after()
    story += word+' '
print(story)
