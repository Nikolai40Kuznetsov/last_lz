# Take mass, volume and density and return is object floats in the water

# Finding function
def Counting(m, V, po):
    if po > 1:
        print("Объект не является плавучим")
    elif po == 1:
        print("Объект является частично плавучим")
    else:
        print("Объект является плавучим")


# Main function
def main():
    mass = float(input("Введите массу объекта "))
    volume = float(input("Введите объём погружённой части объекта "))
    density = float(input("Введите плотность объекта "))
    Counting(mass, volume, density)

if __name__ == "__main__":
    main()