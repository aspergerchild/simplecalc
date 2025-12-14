def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def main():
    print("=== Простой Калькулятор ===")
    
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        
        choice = input("Введите номер операции (1-4): ")
        
        if choice == '1':
            result = add(a, b)
            print(f"\n{a} + {b} = {result}")
        elif choice == '2':
            result = subtract(a, b)
            print(f"\n{a} - {b} = {result}")
        elif choice == '3':
            result = multiply(a, b)
            print(f"\n{a} * {b} = {result}")
        elif choice == '4':
            result = divide(a, b)
            print(f"\n{a} / {b} = {result}")
        else:
            print("Ошибка: выберите операцию от 1 до 4")
            
    except ValueError:
        print("Ошибка! Введите числа корректно.")

if __name__ == "__main__":
    main() 
