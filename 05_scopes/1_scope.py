username = "Chai and Code"

def func():
    #usename = "chai"
    print(username)

print(username)
func()


x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)



def func3():
    global x 
    x = 96
    
func3()
print(x)



def f1():
    x = 88  
    def f2():
        print(x)
    return f2
my_result = f1()
my_result()



def chaiaurcode(num):
    def actual(x):
        return x ** num
    return actual

f = chaiaurcode(2)
g = chaiaurcode(3)

print(f(3))
print(g(3))
