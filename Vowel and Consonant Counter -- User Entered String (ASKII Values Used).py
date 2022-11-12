


def vowels(word):
    word = word.lower()
    wword = []
    wword[:] = word
    #print(wword)

    vowels= ["a", "e","i","o","u"] 
   
    vowelcount = 0
    consonants  = 0
    spaces = 0 
    for i in range (0,len(wword)):
        for z in range(0, 5): 
        
            if wword[i] == vowels[z]:
                vowelcount +=1

        if word[i] == " ":
            spaces +=1
            
    
    print("The string you entered includes", end = " ")
    print(vowelcount, end= "")
    print(" vowels and ", end = "")
    print(str((len(word) - spaces - vowelcount)), end = " ")
    print ("consonants")


def main():
    word = str(input("Enter a string: "))
    vowels(word) 
    


main() 
