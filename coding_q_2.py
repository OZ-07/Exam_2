from coding_q_1 import list_descend

"""
given the following Word.txt, create a Word.txt.txt file and then:
Word.txt: cat, dog, animal, goat, sheep, monkey, turtle
"""
# 1 write a python function to read the Word.txt out of the file and return them
# in a python list

word_list = []
for line in open('Words/Word.txt'):
    word = line.strip()
    word_list.append(word)

def sort_alpha(word_list):
    #list_descend(word_list)
    """word = list(word_list)
    min('animal'),
    max('turtle')
    print(word)"""


def main():
    print(word_list)
    print(sort_alpha(word_list))


if __name__ == '__main__':
    main()