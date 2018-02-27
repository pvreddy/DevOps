def sum_int(x):
    print "given value is %s" %x
    y = 0
    while x:
        y = y + x%10
        x = x//10
    print y



sum_int(33248826)
