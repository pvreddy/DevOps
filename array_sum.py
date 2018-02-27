def sum1(number):
    sum1 = 0
    print number
    print len(number)
    for i in number:
        sum1 = sum1 + int(i)
    print sum1


number = list(raw_input('enter n value : '))
sum1(number)
