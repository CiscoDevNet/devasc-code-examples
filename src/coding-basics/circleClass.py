# Fill in this file with the code from the Coding Basics - Classes exercise

# Print the circumference for circles with a radius of 2, 5, and 7

# Circle class.
# When a Circle object is instantiated,
# a data element is created and is a member of that object.
# Methods:
# __init()__
# circumference()
# printCircumference()

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
      # Formula for a circumference is c = pi * 2 * radius
      pi = 3.14 #
      circumferenceValue = pi * self.radius * 2
      return circumferenceValue

    def printCircumference(self):
      myCircumference = self.circumference()
      print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))


# Create the first class Circle defined object:  'circle1'
circle1 = Circle(1)

# Since printCircumference is a method, it is called using
# [class instance].[method name] syntax.
circle1.printCircumference()

# The Circle class can be instantiated multiple times
circle2 = Circle(2)
circle2.printCircumference()

circle3 = Circle(3)
circle3.printCircumference()
