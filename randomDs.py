# Random Module in Python => For Generating random data using different sub methods

import random 

# Prinitng any random Numbers using random.random method
for i in range(3):
    print(random.random())

print("Uniform method is used to generate random values in range as passed parameters ",random.uniform(5,8))

print("randint is used to generate random integer values in the given range and avoids floating values : " , random.randint(5,30))

# Now we are going to Select randomly from a list using choice.
names = ["sekhar", "s2e", "data science", "ndskj", "jknsdk"]
# Selecting from a list using choice method and getting the values randomly from a method
for i in range(2):
    print(random.choice(names))


names = ["sekhar", "s2e", "data science", "ndskj", "jknsdk"]
# Now we are going to explore something related to choices. This is the next version of the choice method and now we don't have to use for loop any more 
# Since choices is going to accept two parameters one is the list and other is the number of times we need to generate the random values.
# The second parameter should be passed as k and we will be getting list of values as return from choices method

# The choices method return duplicates from the list where this can be avoided by using sample method
print(random.choices(names, k =10))
# The sample method doesn't accept k value greater than the length of the list that we are passing.
# You know why because we are generating unique values here LMAO.
print(random.sample(names, k = 4))