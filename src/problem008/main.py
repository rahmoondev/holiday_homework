#​8. Simple Vowel/Consonant Counter
# ​Goal: Write a program that takes a string and reports the total number of vowels and consonants found.
# Concepts: Loops, string checking (in keyword).
# 📂 File Handling and Data Processing
# File handling is crucial for reading configuration files, processing logs, and handling data dumps.
def Vowel_Consonant_Counter(words:str):
    vowels="aeiouAEIOU"
    vowel_count=0
    Consonant_count=0

    for word in words:
        if word.isalpha():
            if word in vowels:
                vowel_count+=1
            else:
                Consonant_count+=1
    return vowel_count, Consonant_count

if __name__=="__main__":
    string= input("enter a sentance or word: ")
    counter=Vowel_Consonant_Counter(string)
    print(f"the number of vowels are {counter[0]} and the number of consonants are {counter[1]}")