class Mama(object):
    def says(self):
        print("Do your homework")


class Sister(Mama):
    def says(self):
        super(Sister, self).says()
        print(" and clean your bedroom")


manee = Sister()
manee.says()
