# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def jains(val1, val2):
    sum1 = (val1 + val2)**2
    sum2 = 2 * (val1**2 + val2**2)
    jfi = sum1 / sum2
    return jfi


def jainsall(list):
    sum1 = 0
    sum2 = 0
    for x in list:
        sum1 = (x + sum1)
        sum2 = (x**2 + sum2)
    jfi = sum1**2 / (len(list) * sum2)
    return jfi


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    list = [1, 4, 5]
    list2 = [1, 2, 5]
    val1 = 2
    val2 = 4
    print(jains(val1, val2))
    print(jainsall(list))
    print(jainsall(list2))


if __name__ == '__main__':
    print_hi('PyCharm')

liste = []

with open("fil.txt") as fil:
    for x in fil:
        split = x.split()
        liste.append(float(split[0]))
    print(jainsall(liste))

liste2 = []
with open("fil2.txt") as fil2:
    for x in fil2:
        line = x.split()
        if line[1] == "Kbps":
            line = int(line[0]) / 1000
            liste2.append(line)
        elif line[1] == "Mbps":
            line = int(line[0])
            liste2.append(line)
    print(jainsall(liste2))
