def is_even():
    x = int(input('your number here'))
    if x % 2 == 0:
        print("the number x is even")
    else:
        print("the number x is odd")


def main():
    print(is_even())


if __name__ == '__main__':
    main()

