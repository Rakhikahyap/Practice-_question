# i=0
# while i<=10:
#     print(i)

# while  True:
#     print("hello word")

name="rakhi"
print(len(name))

def sum(a,b):
  c=a+b
  return c
def multi():
  e=sum(3,4)
  return e
print(multi())

def sum(a,b):
  return(a+b)
def sub(a,b):
  return(a-b)
def multi(a,b):
  a=sum(4,5)+a
  b=sub(6,4)+b
  return a,b
print(multi(2,3))


def recursive_fibonacci(n):
  if n<=1:
    return n
  else:
    return(recursive_fibonacci(n-1))+recursive_fibonacci(n-2)
n_terms=10
for i in range(n_terms):
  print(recursive_fibonacci(i))


def sum(a,b):
    return(a+b)
def sub(a,b):
    return (a-b)
def fun(a,b):
    print(sum(3,1))
    print(sub(2,1))
fun(2,4)