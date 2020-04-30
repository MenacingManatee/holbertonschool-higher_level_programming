#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    d = dir(hidden_4)
    for i in range(len(d)):
        if d[i][0] != '_':
            print("{}".format(d[i]))
