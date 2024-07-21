from math import pi
def main():
    print("Hello! Welcome to the Shape Area Calculator!")

    while True:
        print("Choose a shape:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            result = calculate_rectangle(length, width)
            print(f"The area of the rectangle is: {result}")

        elif choice == '2':
            radius = float(input("Enter the radius of the circle: "))
            result = calculate_circle(radius)
            print(f"The area of the circle is: {result}")

        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            result = calculate_triangle(base, height)
            print(f"The area of the triangle is: {result}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def calculate_rectangle(length, width):
    return length * width

def calculate_circle(radius):
    return pi * radius * radius

def calculate_triangle(base, height):
    return 0.5 * base * height

if __name__ == "__main__":
    main()
