def myMax(*args):
    maxVal=args[0];
    for i in args:
        if(i>maxVal):
            maxVal=i
    return maxVal
def myEnumerate(collection):
    return [(x.__index__(),x) for x in collection]
a=[1,2,3,4,5]
#for i in myEnumerate(a):
#    print(i)
class cls:
    bar=10
cls.var=20
def robBank():
    return 1;
cls.robBank=robBank
print(cls.robBank())
