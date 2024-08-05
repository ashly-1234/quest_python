# Checking a letter is Vowel or Consonant

Letter = input("Enter the letter to check if it is a Vowel: ")

if Letter == 'a' or Letter == "A" or Letter == 'e' or Letter == "E" or Letter == 'i' or Letter == "I" or Letter == 'o' or Letter == "O" or Letter == 'u' or Letter == "U":                                        #'or' is a relational operator and it needs to satisfy any one of the conditions given
    print(Letter, "is a Vowel")
else:
    print(Letter, "is a Consonant")