def word_counting():
    print("****This is a word counter****")
    print(" ")
    x = str(input("Enter a sentence or paragraph: "))
    if x == "":
        print("User Input is empty!!!!")
        exit()

    word_list = x.split()  #This method splits the string into list of words
    count = len(word_list)
    print("The total number of words are: ", count)

word_counting()