""" write a program that calls a function, list_descend, that sorts a list in
descending order: for example
['z','d','c','b','a']
print(list_descend(['d','a','c','z','b']))
"""


def list_descend(letters):
    return sorted(letters, reverse = True)






def main():
    print(list_descend(['d', 'a', 'c', 'z', 'b']))
    #['z','d','c','b','a']


if __name__ == '__main__':
    main()