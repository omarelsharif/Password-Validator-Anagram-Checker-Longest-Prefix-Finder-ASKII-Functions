
# Enforces the following conditions
# A password must have at least eight characters.
# A password must consist of only letters and digits.
# A password must contain at least two digits.



def check(word):
    x = len(word)
    word = word.lower()
    wword = []
    wword[:] = word
    #print(wword)
    nums = 0
    corrects  = 0 
    
    #if x > 9:
     #   print("Valid password") 
    #else:
    #    print("Invalid password")

    for i in range(0,len(word)):
        wword[i] = ord(word[i])

    for i in range(0,len(word)):

        if (wword[i] > 47 and wword[i] < 60):
            nums += 1
            corrects+= 1
        elif (wword[i] > 96 and wword[i] < 123) or (wword[i] > 47 and wword[i] < 60):
            
            corrects += 1
     
        
    if corrects == x and nums >= 2 and x>=8:
        print("Valid password")
    else:
        print("Invalid password")
        
  
def main():
    word = str(input("Enter a string for password: "))
    check(word) 

main() 
