str = input("Enter a word: ")

def countSyllable(str):

    vowels = "aeiou"
    isVowel = False

    numSyllables = 0

    for i in str:
        if(i in vowels):
            if(not isVowel):
                isVowel = True
                numSyllables+=1
        else:
            isVowel = False


    print(numSyllables)

        
countSyllable(str)

