from conversiones import unidades

def main():
    print("--- CONVERSOR DE UNIDADES ---")
    
    # 1. Conversión de Kilómetros a Metros
    km_ingresados = float(input("Ingresa la cantidad en kilómetros: "))
    resultado_metros = unidades.km_a_metros(km_ingresados)
    print(f"{km_ingresados} km equivalen a {resultado_metros} metros.\n")
    
    # 2. Conversión de Celsius a Fahrenheit
    celsius_ingresados = float(input("Ingresa la temperatura en grados Celsius: "))
    resultado_fahrenheit = unidades.celsius_a_fahrenheit(celsius_ingresados)
    print(f"{celsius_ingresados}°C equivalen a {resultado_fahrenheit}°F.")

if __name__ == "__main__":
    main()