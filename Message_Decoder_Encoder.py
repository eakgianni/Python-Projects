
#Created By Everett Gianni Aug 6th 2020

import os

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '?', ".", ",", "'", "!", "0"]


def encrypt():

    global alphabet 
    
    message = input("enter message: ")
    message = message.lower()
    inputedKey = input("enter key (any integer): ")
    inputedKey = int(inputedKey)
    
    
    
    message = list(message)
    
    

    #cycle through all of the letters in the message and change them based on the key
    cycle = 0
    for i in message:    
        theKey = inputedKey
        
        #set the index if the current letter of the message to the corresponding letter in the alphabet list
        letterIndex = alphabet.index(message[cycle])    
              
        if theKey >= len(alphabet):
            theKey = theKey % len(alphabet)
                
        #if the key and letter index are greater than the alphabet, do some more math stuff idk
        if letterIndex + theKey >= len(alphabet):               
            message[cycle] = alphabet[letterIndex - len(alphabet) + theKey]    
            
            cycle = cycle + 1
                    
        else:
            #set change the current letter by the key based on the alphabet list
            message[cycle] = alphabet[letterIndex + theKey]    
            
            cycle = cycle + 1
            

    os.system("cls")
    print("Done!")
    print("")
    print("".join(message))
    input()    
        
def decrypt():
    global alphabet
    
    message = input("enter message: ")
    
    inputedKey = input("enter key: ")
    inputedKey = int(inputedKey)
    
    
    message = list(message)

    

    #cycle through all of the letters in the message and change them based on the key
    cycle = 0
    for i in message:    
        theKey = inputedKey
        
        #set the index if the current letter of the message to the corresponding letter in the alphabet list
        letterIndex = alphabet.index(message[cycle])           
        
        if theKey >= len(alphabet):
            theKey = theKey % len(alphabet)
            
        
        #if the key and letter index are less than 0, do some more math stuff to get it to a positive number where it should be
        if letterIndex - theKey < 0:               
                       
            message[cycle] = alphabet[letterIndex - theKey + len(alphabet)]    
            
            cycle = cycle + 1
                   
        else:
            #set change the current letter by the key based on the alphabet list
            message[cycle] = alphabet[letterIndex - theKey]    
            
            cycle = cycle + 1
    
    os.system("cls")
    print("Done!")
    print("")
    print("".join(message))
    input()  
            

answer = ""
while answer != "1" and answer != "2":
    os.system("cls")
    print("What do you want to do?")
    print("Encrypt(1)")
    print("Decrypt(2)")
    answer = input(">")

if answer == "1":
    encrypt()
    
elif answer == "2":
    decrypt()





    
    




