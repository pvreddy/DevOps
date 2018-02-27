def linear(a, b):
    def result(x):
        return a * x + b
    return result


y = linear(10,20)
print y
print y(3)



d = {}
list1 = ("what", "I'm", "sorting", "by")
list2 = ("something", "else", "to", "sort")
d.update(zip(list1,list2))
print d
