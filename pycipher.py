### A library of functions for cryptographic encoding and decoding
############## TEST CHANGE LINE ##################
import random
import string
import numpy

def caeser(text=str, keyval=int, direction='e'):
    outputText = ''
    keyVal = keyval

    if direction == 'e':
        inputText = text.strip()
        for c in inputText:
            outputText += chr((ord(c) + keyVal) % 255)
    elif direction == 'd':
        for c in inputText:
            outputText += chr((ord(c) - keyVal) % 255)
    else:
        #if the direction arg is not one of the valid options,
        #spit back the input text
        return text 
        
    
    return outputText
    
    
    
    
def vigenere(text=str, key=str, direction='e'):
    outputText = ''
    inputText = text.strip()
    key = key.strip()
    
    d = 0
    for c in inputText:
        if d >= len(key):
            d = 0
        outputText += chr((ord(c) + ord(key[d])))
    
    return outputText    
    
    
    
#THESE TWO FUNCTIONS ARE V DUMB. DO NOT USE    
def oneTimePadEncode(text=str):
    outputText = ''
    key = ''
    inputText = text.strip()
    for c in inputText:
        shift = random.randrange(0, 256)
        outputText += chr((ord(c) + shift) % 255)
        key += str(shift).zfill(3)
    return (outputText, key)
    
def oneTimePadDecode(text=str, key=int):
    outputText = ''
    key = str(key)
    inputText = text
    for c in inputText:
        outputText += chr((ord(c) - int(key[:3])) % 255)
        key = key[3:]
    return outputText
