# Yusupov
# Take height and two bases of pyramid and count it's value

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