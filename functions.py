def hello():
    print('Hello, class ***!')
hello()

# Pass single argument to a function
def hello(name):
    print('Hello,', name)
hello('Maria')
hello('Kim')
hello('Olya')

# Pass multiple arguments
def some_function(name, job):
    print(name, 'is a', job)
some_function('fiona', 'chef')

def some_function(name, job, skill):
    print(name, 'is a',skill,job)
some_function(job='developer', name='Fiona',skill="python")
some_function('Fiona', job='developer',skill='python')

def AreaOfCircle(radius):
    return(radius*3.14**2)
print(AreaOfCircle(5))
