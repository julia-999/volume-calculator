"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: October 16th 2019
Program Description: Uses "volume.py" module to calculate volumes and summarize results
"""

# import statements
from Assign2.volume import c_volume_calc, p_volume_calc, e_volume_calc
from Assign2.summarize import summarize

# lists for each shape
cubes = []
pyramids = []
ellipsoids = []

# test number for summary
testNumber = input("Enter test number: ")

# while loop for counting total volumes, continues until user quits
while True:

    # prompts for shape choice input and formats it
    shape = input("\nEnter shape (q or quit to terminate): cube or c, pyramid or p, ellipsoid or e: ").lower().strip().replace(" ", "")

    # ends session if q is entered
    if shape == "q" or shape == "quit":
        break

    # calculates volume based on shape and adds to list
    if shape == "cube" or shape == "c":
        side = int(input("Enter the side length: "))
        cubes.append(c_volume_calc(side))
    elif shape == "pyramid" or shape == "p":
        base = int(input("Enter the base length: "))
        height = int(input("Enter the height: "))
        pyramids.append(p_volume_calc(base, height))
    elif shape == "ellipsoid" or shape == "e":
        radius1 = int(input("Enter the first radius: "))
        radius2 = int(input("Enter the second radius: "))
        radius3 = int(input("Enter the third radius: "))
        ellipsoids.append(e_volume_calc(radius1, radius2, radius3))

    # tells user if input is invalid
    else:
        print("Invalid input. Try again.")

# sorts the volumes from lowest to highest
cubes.sort()
pyramids.sort()
ellipsoids.sort()

# tells user their session is done
print("\nYou have reached the end of your session.")

# tells user if they did not perform any volume calculations
if len(cubes) == 0 and len(pyramids) == 0 and len(ellipsoids) == 0:
    print("You did not perform any volume calculations.")

# prints lists of volumes or tells user if no volumes were entered for that shape
else:
    print("Cube: ", end="")
    if len(cubes) == 0:
        print("No shapes entered.")
    else:
        print(*cubes, sep=", ")
    print("Pyramid: ", end="")
    if len(pyramids) == 0:
        print("No shapes entered.")
    else:
        print(*pyramids, sep=", ")
    print("Ellipsoids: ", end="")
    if len(ellipsoids) == 0:
        print("No shapes entered.")
    else:
        print(*ellipsoids, sep=", ")

# summarizes results in a file
summarize(cubes, pyramids, ellipsoids, testNumber)
