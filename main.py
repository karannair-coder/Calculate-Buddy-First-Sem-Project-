while True:

    print("Welcome To Calculate Buddy!")
    print("Operations")
    print("1:- Area (2D)")
    print("2:- Area (3D)")
    print("3:- Volume (3D)")
    print("4:- Perimeter")
    print("5:- Power Menu")
    print("6:- Loan Calculator")
    print("7:- Basic Calci")
    print("8:- Exit")

    try:
        a = int(input("Choose Operation: "))
    except:
        print("Error! please select an operation")

    if a == 8:
        print("Have a Good Day!")
        break

    if a == 1:
        print("Area 2d menu: ")

    if a == 2:
        print("Area 3d Menu: ")
    
    if a == 3:
        print("Volume Menu: ")
    
    if a == 4:
        print("Perimeter Menu: ")
    
    if a == 5:
        print("Power Menu: ")

    if a == 6:
        print("Loan Menu: ")

    if a == 7:
        print("Basic Calci Menu: ")

    input("Press Enter to continue: ")
