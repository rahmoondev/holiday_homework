#​6. Word Counter
# ​Goal: Write a script that takes a sentence from the user and counts how many times each word appears.
# Concepts: Strings, splitting strings, dictionaries (to store word counts).
def word_counter(sentance):
    words= sentance.split()
    word_count= {}
    for word in words:
        word=word.lower().strip('.,!?:":')
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] =1
    return word_count
    
if __name__=="__main__":
    input=input("enter a sentance: ")

    counter= word_counter(input)
    print(counter)