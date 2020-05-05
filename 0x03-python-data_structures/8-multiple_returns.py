#!/usr/bin/python3
def multiple_returns(sentence):
    res_list = []
    res_list.append(len(sentence))
    if (sentence):
        res_list.append(sentence[0])
    else:
        res_list.append("None")
    return(tuple(res_list))
