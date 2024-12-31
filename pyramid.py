# Take height and two bases of pyramid and count it's value
# Import all nesessary libs and modules
import math as m

# Finding lambda function
Value = lambda base_1, base_2, height: height / 3 * (base_1 + base_2 + m.sqrt(base_1 * base_2))


# Main function
def main():
    base_1 = float(input("Введите площадь нижнего основания "))
    base_2 = float(input("Введите площадь верхнего основания "))
    height = float(input("Введите высоту усечённой пирамиды "))
    print(f"ОбЪём усечённой пирамиды составляет {Value(base_1, base_2, height)} кубических единиц")

if __name__ == "__main__":
    main()