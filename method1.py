def word_counting():
    print("****This is a word counter****")
    print(" ")
    count = 1  #This ensures first word is also counted
    x = str(input("Enter a sentence or paragraph: "))
    if x == "":
        print("User Input is empty!!!!")
        exit()
    s = len(x)
    for i in range(0, s):
        if x[i] == " " and x[i + 1].isalnum():  #This condition checks if a new word is beginning
            count = count + 1
    print("The total number of words are: ", count)


word_counting()

