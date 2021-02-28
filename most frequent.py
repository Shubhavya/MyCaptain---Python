import operator

def most_frequent(x):
    d = {}
    for i in x:
        d[i] = x.count(i)
    d1 = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    for i in d1:
        print(i,'=', d1[i])

x = input("Enter the input string: ")
most_frequent(x)