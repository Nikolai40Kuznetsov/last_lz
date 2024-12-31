# Main file of the project
# All rights are reserved

# Import all nesessary libs and modules
import pyramid as p
import Archimed as A

# The main function of the project
def main():
    user_choise = int(input("Выберите функцию, которую хотите использовать: "))
    if user_choise == 1:
        base_1 = float(input("Введите площадь нижнего основания "))
        base_2 = float(input("Введите площадь верхнего основания "))
        height = float(input("Введите высоту усечённой пирамиды "))
        print(f"ОбЪём усечённой пирамиды составляет {p.Value(base_1, base_2, height)} кубических единиц")
    if user_choise == 2:
        mass = float(input("Введите массу объекта "))
        volume = float(input("Введите объём погружённой части объекта "))
        density = float(input("Введите плотность объекта "))
        A.Counting(mass, volume, density)

if __name__ == "__main__":
    main()