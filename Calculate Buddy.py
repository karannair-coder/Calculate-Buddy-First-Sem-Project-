import math


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
    a = int(input("Choose Your Operation: "))
  except:
    print("Error! Please Select the Operation")
    a = 0

  
  if a == 8:
    print("Have a Good Day!")
    break
  
  if a == 1:
    print("1:- Square")
    print("2:- Rectangle")
    print("3:- Circle")
    print("4:- Triangle")
    print("5:- Ellipse")
    print("6:- Parallelogram")
    b = int(input("Choose Your Shape: "))
    if b == 1:
      x = float(input("Side Of Square(in cm): "))
      print("Area of Square is: ",x*x,"cm²")
    if b == 2:
      x = float(input("Enter the length of rectangle: "))
      y = float(input("Enter the breadth of reactangle: "))
      print("Area of rectangle is: ",x*y,"cm²")
    if b == 3:
      x = float(input("Radius of circle: "))
      print("Area of circle is: ",(math.pi*x*x),"cm²")
    if b == 4:
      x = float(input("Enter Base of the Triangle: "))
      y = float(input("Enter Height of the Triangle: "))
      print("Area of Triangle is :",1/2*x*y,"cm²")
    if b == 5:
      x = float(input("Enter Value of Major Axis: "))
      y = float(input("Enter Value of Minor Axis: "))
      print("Area of Ellipse: ",(math.pi*x*y))
    if b == 6:
      x = float(input("Enter base of  Parallelogram: "))
      y = float(input("Enter height of parallelogram: "))
      print("Area of Parallelogram: ",(x*y))
  if a == 2:
    print("Shapes")
    print("1:- Cube")
    print("2:- Cuboid")
    print("3:- Sphere")
    print("4:- Cylinder")
    print("5:- Cone")
    print("6:- Hemisphere")
    b = int(input("Select Operation: "))
    if b == 1:
      x = float(input("Enter the Edge Length: "))
      print("Surface Area of Cube: ",6*x*x)
    if b == 2:
      x = float(input("Enter Length: "))
      y = float(input("Enter Breadth: "))
      z = float(input("Enter Height: "))
      print("Surface Area of Cuboid: ",(2*((x*y)+(y*z)+(z*x))))
    if b == 3:
      x = float(input("Enter the Radius: "))
      print("Surface Area of Sphere: ",(4*math.pi*x*x))
    if b == 4:
     x = float(input("Enter The Radius: "))
     y = float(input("Enter the Height: "))
     print("Curved Surface Area: ",(2*math.pi*x*y)) 
     print("Total Surface Area: ",(2*math.pi*x*(y+x)))
    if b == 5:
      x = float(input("Enter Radius: "))
      y = float(input("Enter Height: "))
      print("Area of Cone: ",(math.pi*x*(x+math.sqrt((y*y)+(x*x)))))
    if b == 6:
      x = float(input("Enter the Radius: "))
      print("Curved Surface Area: ",(2*math.pi*x*x))
      print("Total Surface Area: ",(3*math.pi*x*x))
  if a == 3:
    print("Select Shapes: ")
    print("1:- Cube")
    print("2:- Cuboid")
    print("3:- Sphere")
    print("4:- Cylinder")
    print("5:- Cone")
    print("6:- Hemisphere")
    b = int(input("Select Shape: "))
    if b == 1:
      x = float(input("Enter the Edge Length: "))
      print("Volume of Cube: ",(x*x*x))
    if b == 2:
      x = float(input("Enter Length: "))
      y = float(input("Enter Breadth: "))
      z = float(input("Enter Height: "))
      print("Volume Of Cuboid: ",(x*y*z))
    if b == 3:
      x = float(input("Enter Radius: "))
      print("Volume of Sphere: ",(4/3*(math.pi*(x*x*x))))
    if b == 4:
      x = float(input("Enter Radius: "))
      y = float(input("Enter Height: "))
      print("Volume of Cylinder: ",(math.pi*(x*x)*y)) 
    if b == 5:
     x = float(input("Enter Radius: "))
     y = float(input("Enter Height: "))
     print("Volume of Cube: ",(1/3*(math.pi*x**2*y)))
    if b == 6:
      x = float(input("Enter Radius: ")) 
      print("Volume of Hemispshere: ",(2/3*(math.pi*x**3)))  

  if a == 4:
    print("Shapes")
    print("1:- Square")
    print("2:- Rectangle")
    print("3:- Circle")
    print("4:- Triangle")
    b = int(input("Choose Your Shape: "))
    if b == 1:
      x = float(input("Enter side of Sqaure: "))
      print("Perimeter of Square: ",4*x,"cm")
    if b == 2:
      x = float(input("Enter the Length: "))
      y = float(input("Enter the Breadth: "))
      print("Perimetr of Rectangle: ",2*(x+y),"cm")
    if b == 3:
      x = float(input("Enter the Radius: "))
      print("Perimter of Circle: ",2*math.pi*x,"cm")
    if b == 4:
      x = float(input("Side 1 of the Triangle: "))
      y = float(input("Side 2 of the Triangle: "))
      z = float(input("Side 3 of the Triangle: "))
      print("Perimeter of Triangle: ",x+y+z,"cm")
  if a == 5:
    print("Select Operation:")
    print("1:- Square")
    print("2:- Cube")
    print("3:- Square Root")
    x = float(input("Select Operation: "))
    if x == 1:
      a = int(input("Enter The Number: "))
      print("Square of Number: ",a*a)
    if x == 2:
      a = float(input("Enter Number: "))
      print("Cube: ",a**3)
    if x == 3:
      a = float(input("Enter Number: "))
      print("Square Root: ",math.sqrt(a))
  
  if a == 6:
    x = float(input("Enter The Loan Amount: "))
    y = float(input("Enter Monthly Intrest Rate (%): "))
    z = float(input("Enter Number of Months: "))
    y = y/100
    emi = (x*y*(1+y)**z)/((1+y)**z -1)
    print("Your EMI is: ₹",round(emi))

  if a == 7:
    print("Select Operation:")
    print("1:- Addition")
    print("2:- Subtraction")
    print("3:- Multiplication")
    print("4:- Division")
    b = int(input("Select Operation: "))
    if b == 1:
      x = int(input("Enter 1st No.: "))
      y = int(input("Enter 2nd No.: "))
      print("Addition: ",x+y)
    if b == 2:
      x = int(input("Enter 1st No.: "))
      y = int(input("Enter 2nd No.: "))
      print("Subtraction",x-y)
    if b == 3:
      x = int(input("Enter 1st No.: "))
      y = int(input("Enter 2nd No.: "))
      print("Multiplication: ",x*y)
    if b == 4:
      x = int(input("Enter 1st No.: "))
      y = int(input("Enter 2nd No.: "))
      if y == 0:
        print("Not Defined!")
      else:
        print("Division: ",x/y)
      

    
  input("Press Enter To Continue...")

