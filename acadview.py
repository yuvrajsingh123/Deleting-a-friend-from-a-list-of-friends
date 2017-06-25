p=-1
list=['mayank','yuvraj','sanjeet']

for friends in list:

    print 'Your current friend is:=',friends

    text=raw_input("Enter the text")

    splitt = text.split()

    qw = len(splitt)

    print "length is ", qw
    p=p+1
    if qw>5:
        del list[p]
        print 'Final friends are:-',list
        exit()
    else:
        print 'none of your friends are deleted'




