#parameters of function can given a default values


def function(x,y,food="spam"):
    print(food)

function(1,2)
function(3,4,"egg")

#in case the argument is passed in,the defaut value is ignored


# **kwargs - standing for keyword arguments

def my_func(x,y=7, *args, **kwargs):
    print(kwargs)

my_func(2,3,4,5,6, a=7,b=8)

# a and b are the names of the arguments  that we passed
# arguments returned by **kwargs are not included in *args
