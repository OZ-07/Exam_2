#print("high") if 5 > 3 else print("low")

#def test():
 #   return 10, 20

#a, b = test()
#print(a + b)

#print(len([1,2,3]))

#for i in range(5,1,-1):
 #   print("hello")

#arr = [1, 2, 3, 4]
#for num in arr:
#    if num == 3:
#        break
#    print(num)
def add(*args):
    return sum(args)


print(add(1, 2, 3))

x = 4
if x > 5:
    print("greater")
elif x < 5:
    print("less")
else:
    print("equal")


    def print_hello():print("hello")

    def add(x, y): return x + y

    print(type(print_hello()))
    print(type(add(x + y)))
    def unsure(n):
        if n == 1:
            return 1
        else:
            return n * unsure(n-1)

    print(unsure(5))

def main():
    my_list= [10,20,30,40,50]
    print(my_list[1:4])




if __name__ == '__main__':
    main()