words = ["cat", "dog", "animal", "goat", "sheep", "monkey", "turtle"]

with open("word.txt", "w") as file:
    for word in words:
        file.write(word +" \n")