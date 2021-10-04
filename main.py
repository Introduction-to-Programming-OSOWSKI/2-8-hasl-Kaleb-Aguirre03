#Define the function hasL()
def hasL(w):

#Create a for loop to check every letter in a word
    for i in range (0, len(w)):
        if w[i] == "l":
            return True

    #else statement is not needed because it is not on the same indentation as the if statement        
    return False

#Print the function to test the code
print (hasL("wool"))
