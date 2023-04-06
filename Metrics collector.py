import psutil

def collect_metrics():
    cpu_percent = psutil.cpu_percent()
    mem_stats = psutil.virtual_memory()
    mem_percent = mem_stats.percent

    print(f"Porcentaje de uso de CPU: {cpu_percent}%")
    print(f"Porcentaje de uso de memoria: {mem_percent}%")
collect_metrics()
