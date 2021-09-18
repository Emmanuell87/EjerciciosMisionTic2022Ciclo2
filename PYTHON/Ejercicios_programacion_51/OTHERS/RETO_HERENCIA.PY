total_ganado= int(input("Ingrese la cantidad total de ganado que heredaran\n"))

def calcular_herencia(total_ganado):
    
    
    ganado_heredado_hermano_menor = int(total_ganado*(1/6))

    ganado_heredado_hermano_medio = int(ganado_heredado_hermano_menor*2)
    ganado_heredado_hermano_mayor = int(ganado_heredado_hermano_menor*3)

    ganado_heredado = int(ganado_heredado_hermano_mayor+ganado_heredado_hermano_medio+ganado_heredado_hermano_menor)

    return (f"Total: {ganado_heredado}\n"
    f"hijo_mayor: {ganado_heredado_hermano_mayor}\n"
    f"hijo_medio: {ganado_heredado_hermano_medio}\n"
    f"hijo_menor: {ganado_heredado_hermano_menor}\n")

print(calcular_herencia(total_ganado))