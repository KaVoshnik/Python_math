from math import *

def inp(a: int, argsname: list) -> list:
    out = []
    for i in range(0, a):
        out.append(input("Input " + str(argsname[i]) + " arg: "))
    return out


if __name__ == '__main__':

    print("Select formule:")
    print("1: s = b * sin(a * t^2 * cos(2 * t))")
    print("2: z = m * cos(b * t * sin(t)) + c")
    print("3: f = x * sin(x^3) * cos(x)^2")
    print("4: r = x^2 * (x + 1)/b - sin(x + a)^2")

    a = input("Choise: ")
    print()

    if a == '1':
        print("s = b * sin(a * t^2 * cos(2 * t))")
        arr = inp(3, ['a', 'b', 't'])
        s = int(arr[1]) * sin(int(arr[0]) * int(arr[2]) * int(arr[2]) * cos(2 * int(arr[2])))
        print("s = " + str(s) + "\n")

    elif a == '2':
        print("z = m * cos(b * t * sin(t)) + c")
        arr = inp(4, ['m', 'b', 't', 'c'])
        z = int(arr[0]) * cos(int(arr[1]) * int(arr[2]) * sin(int(arr[2]))) + int(arr[3])
        print("z = " + str(z) + "\n")

    elif a == '3':
        print("f = x * sin(x^3) * cos(x)^2")
        arr = inp(2, ['x', 'y'])
        f = int(arr[0]) * sin(int(arr[0]) ** 3) * cos(int(arr[0])) ** 2
        print("f = " + str(f) + "\n")

    elif a == '4':
        print("r = x^2 * (x + 1)/b - sin(x + a)^2")
        arr = inp(3, ['x', 'b', 'a'])
        r = int(arr[0]) ** 2 * (int(arr[0]) + 1) / int(arr[1]) - sin(int(arr[0]) + int(arr[2])) ** 2
        print("r = " + str(r) + "\n")

    else:
        print("Incorrect input! Please, try again")
