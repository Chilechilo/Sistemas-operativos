class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion

def fcfs(planificacion):
    tiempo_actual = 0
    tiempo_espera_total = 0

    for proceso in planificacion:
        if tiempo_actual < proceso.tiempo_llegada:
            tiempo_actual = proceso.tiempo_llegada
        tiempo_espera = tiempo_actual - proceso.tiempo_llegada
        tiempo_espera_total += tiempo_espera
        tiempo_actual += proceso.tiempo_ejecucion

        print(f"Proceso {proceso.nombre}: Tiempo de espera = {tiempo_espera}")
    
    promedio_tiempo_espera = tiempo_espera_total / len(planificacion)
    print(f"Tiempo promedio de espera = {promedio_tiempo_espera}")

if __name__ == "__main__":
    proceso1 = Proceso("P1", 0, 10)
    proceso2 = Proceso("P2", 3, 5)
    proceso3 = Proceso("P3", 5, 8)
    proceso4 = Proceso("P4", 9, 2)

    lista_procesos = [proceso1, proceso2, proceso3, proceso4]

    print("Planificación FCFS:")
    fcfs(lista_procesos)
