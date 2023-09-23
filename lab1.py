# Task 1.1
def task1():
    sequence = [4, 8, 15, 16, 23, 42]

    for number in sequence:
        print(number, end=' ')

task1()

# Task 1.2
def task2():
    sequence = [4, 8, 15, 16, 23, 42]

    for number in sequence:
        print(number)

task2()

# Task 1.3
def task3():
    first_number = int(input("enter number: "))
    for i in range(3):
        print(first_number + i)

task3()

# Task 1.4
def task4():
    first_number = int(input("enter first number: "))
    second_number = int(input("enter second number: "))
    third_number = int(input("enter third number: "))

    var = first_number + second_number + third_number
    print (var)

task4()

# Task 1.5
def task5():
    edge_length = float(input("Enter the edge length of the cube: "))

    # Calculate the volume of the cube
    volume = edge_length ** 3

    # Calculate the total surface area of the cube
    surface_area = 6 * edge_length ** 2

    print("Volume =", int(volume))
    print("Total surface area =", int(surface_area))

    task5()