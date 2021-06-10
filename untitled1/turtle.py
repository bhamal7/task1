import string


def capTitle(line):
    line1=line.split()
    for i in range(len(line1)):
        if i == 0 or line1[i] not in specailWords:
            line1[1]=line1[i].title()
    return ' '.join(line1)
    print("hi")