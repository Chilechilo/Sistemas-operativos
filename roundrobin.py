class Proceso:
    def __init__(self, nombre, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_ejecucion = tiempo_ejecucion

def round_robin(procesos, quantum):
    tiempo_total = 0
    while procesos:
        proceso_actual = procesos.pop(0)
        if proceso_actual.tiempo_ejecucion <= quantum:
            tiempo_total += proceso_actual.tiempo_ejecucion
            print(f"Ejecutando {proceso_actual.nombre} por {proceso_actual.tiempo_ejecucion} unidades de tiempo")
        else:
            tiempo_total += quantum
            print(f"Ejecutando {proceso_actual.nombre} por {quantum} unidades de tiempo")
            proceso_actual.tiempo_ejecucion -= quantum
            procesos.append(proceso_actual)
    
    print(f"Tiempo total de ejecución: {tiempo_total}")

if __name__ == "__main__":
    proceso1 = Proceso("P1", 10)
    proceso2 = Proceso("P2", 5)
    proceso3 = Proceso("P3", 8)
    proceso4 = Proceso("P4", 4)
    proceso5 = Proceso("P5", 7)

    lista_procesos = [proceso1, proceso2, proceso3, proceso4, proceso5]
    quantum = 3  

    print("Simulación del algoritmo Round Robin")
    round_robin(lista_procesos, quantum)
