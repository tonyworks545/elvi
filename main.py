import sys

initialWeight = int(sys.argv[1])

# # print "hello world"

weight = initialWeight
def elvis_is_dead(message):
    if weight <= 0:
        print message + " Elvis is dead!"
        quit() 
    print message
    print weight
# TODO: Elvis eats a lot of food and gains 20 pounds

# +  addition operator
# -  subtraction operator
# *  multiplication operator
# /  divison operator
# =  assignment operator (sets a variable equal to something)

# BOOLEAN Operators
# Boolean operators return either true or false and can be used
# to make sure some condition is true for example:

if weight == 0:
    quit()

# the code above quits the program if elvis weights 0 pounds.
# add code that checks if Evlis has negative weight. 
# If he does print elvis is dead and quit

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


# gains weight
weight = weight + 20 
elvis_is_dead("Ate 50 ice cream sundaes")


# diet
weight = weight - 10
elvis_is_dead("Ate to much brockle")
 


# falls in dryer
weight = weight / 2
elvis_is_dead('supid and more supid')

# Elvis clone 
weight = weight *13
elvis_is_dead('ate a lot of brugers')

# thoson Elvis clone tower
weight = weight - 1001
elvis_is_dead('played just dance bad')



# Elvis kills with music
weight = weight * 1000
elvis_is_dead('ate to many chips')


# People love Elvis 
weight = weight / 5
elvis_is_dead('punch someone in the face')
 

# Elvis dead because of being ugly
    # inside ifs you have to indent like this or it doesn't know you are inside the if
if weight <= 0:
    print "Elvis is dead!"
    quit()

# Okay put it all the places the weight can be less than 0. You haven't found the all yet.
# so is a way to make a game by using this
