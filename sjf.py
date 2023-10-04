class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion

def sjf(planificacion):
    tiempo_actual = 0
    tiempo_espera_total = 0
    procesos_terminados = []

    while planificacion:
        procesos_disponibles = [proceso for proceso in planificacion if proceso.tiempo_llegada <= tiempo_actual]

        if not procesos_disponibles:
            tiempo_actual += 1
            continue

        proceso_actual = min(procesos_disponibles, key=lambda x: x.tiempo_ejecucion)
        planificacion.remove(proceso_actual)

        tiempo_espera = tiempo_actual - proceso_actual.tiempo_llegada
        tiempo_espera_total += tiempo_espera
        tiempo_actual += proceso_actual.tiempo_ejecucion

        print(f"Proceso {proceso_actual.nombre}: Tiempo de espera = {tiempo_espera}")

        procesos_terminados.append(proceso_actual)

    promedio_tiempo_espera = tiempo_espera_total / len(procesos_terminados)
    print(f"Tiempo promedio de espera = {promedio_tiempo_espera}")

if __name__ == "__main__":
    proceso1 = Proceso("P1", 0, 6)
    proceso2 = Proceso("P2", 2, 8)
    proceso3 = Proceso("P3", 4, 7)
    proceso4 = Proceso("P4", 5, 3)

    lista_procesos = [proceso1, proceso2, proceso3, proceso4]

    print("Planificación SJF:")
    sjf(lista_procesos)
