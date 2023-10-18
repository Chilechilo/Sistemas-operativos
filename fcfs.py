
processes = [
    {"id": "P1", "arrivalTime": 4, "burstTime": 5},
    {"id": "P2", "arrivalTime": 6, "burstTime": 4},
    {"id": "P3", "arrivalTime": 0, "burstTime": 3},
    {"id": "P4", "arrivalTime": 6, "burstTime": 2},
    {"id": "P5", "arrivalTime": 5, "burstTime": 4}
]

processes.sort(key=lambda x: x["arrivalTime"])

current_time = 0
waiting_time = []
turnaround_time = []

for process in processes:
    arrival_time = process["arrivalTime"]
    burst_time = process["burstTime"]

    process_waiting_time = max(0, current_time - arrival_time)
    waiting_time.append(process_waiting_time)

    completion_time = max(current_time, arrival_time) + burst_time
    current_time = completion_time

    process_turnaround_time = completion_time - arrival_time
    turnaround_time.append(process_turnaround_time)

average_waiting_time = sum(waiting_time) / len(waiting_time)
average_turnaround_time = sum(turnaround_time) / len(turnaround_time)

print("Promedio de Waiting Time:", average_waiting_time)
print("Promedio de Turn Around Time:", average_turnaround_time)
