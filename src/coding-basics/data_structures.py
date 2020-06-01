# Fill in this file with the code for Python practice with data structures

def legalAges():
    lifeEvent = (
        16, #driving,
        18, #voting
        21, #drinking
        65  #retirement
    )
    print("The legal driving age is "
      + str(lifeEvent[0]) + ".")
    print("The legal voting age is "
      + str(lifeEvent[1]) + ".")
    print("The legal drinking age is "
      + str(lifeEvent[2]) + ".")
    print("The legal retirement age is "
      + str(lifeEvent[3]) + ".")
legalAges()
