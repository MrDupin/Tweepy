def Build():
    f = open("names.txt", 'r')
    lines = f.readlines()
    f.close()

    d = {"807332651782774785": "paleshadow7"}
    for line in lines:
        ID, name = line.strip().split(',')
        d[ID] = name

    return d
