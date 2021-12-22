from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import math

def main():
    r = Rectangle("Синего", 11, 10)
    c = Circle("Зеленого", 11)
    s = Square("Красного", 11)
    print(r)
    print(c)
    print(s)
    print(math.factorial(12))

if __name__ == "__main__":
    main()