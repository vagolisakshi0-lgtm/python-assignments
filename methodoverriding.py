class square:
    def area(self,side):
        y=self.side*self.side;
        print(y)
class rec(square):
    def area(self,l,b):
        x=self.l*self.b;
        print(x)
r=rec(4,4)
r.area(4)
