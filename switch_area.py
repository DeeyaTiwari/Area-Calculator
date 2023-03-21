print("\t\t\t_______________________________________________________________")
print("\t\t\t\t\t\t\t\tAREA CALCULATOR")
print("\t\t\t_______________________________________________________________")
print("1. Area of circle\t\t\t\t\t\t2. Area of Triangle\t\t\t\t\t\t3. Area of Square\n4. Area of Rectangle\t\t\t\t\t5. Area of Parellelogram\t\t\t\t\t6. Area of Rhombus\n7. Area of Cube\t\t\t\t\t\t8. Area of Cuboid\t\t\t\t\t\t9. Area of Cone\n10. Area of Cylinder\t\t\t\t\t\t11. Area of Sphere\t\t\t\t\t\t12. Area of Hemisphere")
print("\nFor Choice, either type the name of the shape or the number associated with it.")
#while True:
choice="Y"
while choice.upper()=="Y":
    ch=(input("\nEnter your choice : ")).lower()
    count=0
    pi=3.14
    match ch:
        case "circle"|"1":
            print("\nAREA OF CIRCLE"
                  )
            radius=eval(input("Enter radius of circle : "))
            area_c=pi*radius*radius
            print("Area of circle = ", area_c)
            choice= input("Do you want to continue? (Y/N): ")
        case "triangle"|"2":
            print("\nAREA OF TRIANGLE")
            base=eval(input("Enter the value for base : "))
            height=eval(input("Enter the value for height : "))
            area_tr=1/2*base*height
            print("Area of Triangle = ", area_tr)
            choice= input("Do you want to continue? (Y/N): ")
        case "square"|"3":
            print("\nAREA OF SQUARE")
            side=eval(input("Enter side : "))
            area_sq=s*s
            print("Area of Square = ", area_sq)
            choice= input("Do you want to continue? (Y/N): ")
        case "recatngle"|"4":
            print("\nAREA OF RECTANGLE")
            length=eval(input("Enter length of Rectangle : "))
            breadth=eval(input("Enter breadth of Rectangle : "))
            area_rect=length*breadth
            print("Area of Recatangle = ", area_rect)
            choice= input("Do you want to continue? (Y/N): ")
        case "parallelogram"|"5":
            print("\nAREA OF PARALLELOGRAM")
            base=eval(input("Enter base of the Parallelogram : "))
            height=eval (input("Enter height of the Parallelogram : "))
            area_pl=base*height
            print("Area of Parallelogram = ", area_pl)
            choice= input("Do you want to continue? (Y/N): ")
        case "rhombus"|"6":
            print("\nAREA OF RHOMBUS")
            diag1=eval(input("Enter the value for first diagonal : "))
            diag2=eval(input("Enter the value for second diagonal : "))
            area_rh=(diag1*diag2)/2
            print("Area of Rhombus = ", area_rh)
            choice= input("Do you want to continue? (Y/N): ")
        case "cube"|"7":
            print("\nAREA OF CUBE")
            a=eval(input("Enter the value for side : "))
            area_cube=6*a*a
            print("Area of Cube = ", area_cube)
            choice= input("Do you want to continue? (Y/N): ")
        case "cuboid"|"8":
            print("\nAREA OF CUBOID")
            l=eval(input("Enter the value for length : "))
            b=eval(input("Enter the value for breadth : "))
            h=eval(input("Enter the value for height : "))
            area_cuboid=2*(l*b+b*h+h*l)
            print("Area of Cuboid = ", area_cuboid)
            choice= input("Do you want to continue? (Y/N): ")
        case "Cone"|"9":
            print("\nAREA OF CONE")
            r=eval(input("Enter the value for radius : "))
            l=eval(input("Enter the length of slant height : "))
            area_cone=(pi*r*r)+ (pi*r*l)
            print("Area of Cone = ", area_cone)
            choice= input("Do you want to continue? (Y/N): ")
        case "cylinder"|"10":
            print("\nAREA OF CYLINDER")
            r=eval(input("Enter the value for radius : "))
            h=eval(input("Enter the value for height : "))
            area_cylinder=2*pi*r(r+h)
            print("Area of Cylinder = ", area_cylinder)
            choice= input("Do you want to continue? (Y/N): ")
        case "sphere"|"11":
            print("\nAREA OF SPHERE")
            r=eval(input("Enter the value for radius : "))
            area_sph=4*pi*r*r
            print("Area of Sphere = ", area_sph)
            choice= input("Do you want to continue? (Y/N): ")
        case "hemisphere"|"12":
            print("\nAREA OF HEMISPHERE")
            r=eval(input("Enter the value for radius : "))
            area_hemis=2*pi*r*r
            print("Area of Hemiphere = ", area_hemis)
            choice= input("Do you want to continue? (Y/N): ")
print("\n\t\t\t\t\t\t\tThank-you for using the Calculator, have a nice day!!")
exit
            
