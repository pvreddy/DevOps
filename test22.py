class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        print "second"

class Third(Second):
    def __init__(self):
        super(Third, self).__init__()
        print "that's it"



O = Third()
