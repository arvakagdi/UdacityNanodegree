
#program is correct but i am struck in getting output.Please see my print statement.
#i want a output like this
#                  abcd
 #                 ==^
 #                 abef


def singleline_diff_format(line1,line2,idx):
    sum=""
    length1=len(line1)
    length2=len(line2)
    if length1>length2:
        longer_length=length1
    else:
        longer_length=length2
    for i in range(longer_length):
        if i <idx:
            sum=sum+"="
        else:
            sum=sum+"^"
            break
    try1=line1
    try2=sum
    try3=line2
    return try1,try2,try3

join=list(singleline_diff_format("abcde","ab",2))
print("{0}\n{1}\n{2}".format(join[0],join[1],join[2]))


