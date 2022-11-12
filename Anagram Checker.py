
def isAnagram(string1,string2):
    isAnagram = False
    if len(string1) == len(string2):
        isAnagram = True
        for letter1 in string1:
            count1 = 0
            count2 = 0
            for letter2 in string1:
                if letter1 == letter2:
                    count1 += 1
            for letter2 in string2:
                if letter1 == letter2:
                    count2 += 1
            if count1 != count2:
                isAnagram = False
        return isAnagram


def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    x = isAnagram(string1,string2)
    if x == True:
        print(string1, "and", string2, "are anagrams")
    else:
        print(string1, "and", string2, "are not anagrams")

main()
