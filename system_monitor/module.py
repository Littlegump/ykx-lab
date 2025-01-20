import psutil

class SystemMonitor:
    def __init__(self):
        self.cpu_count = psutil.cpu_count(logical=True)
    
    def get_cpu_usage(self):
        ''' get cpu usage'''
        return psutil.cpu_percent(interval=1) ## sample interval equals 1 second
    
    def get_mem_usage(self):
        """
        get mem usage
        return {
            "total": float GB .2f
            "used": float GB .2f
            "free": float GB .2f
            "percent": Str eg 88.2%
        }
        """
        memory = psutil.virtual_memory()
        return {
            "total": float(f"{memory.total/(1024**3):.2f}"),
            "used": float(f"{memory.used/(1024**3):.2f}") ,      # 已使用内存
            "free": float(f"{memory.available/(1024**3):.2f}"), # 客用内存
            "percent": str(memory.percent)+"%" # 内存使用百分比
        }

def my_function():
    return "Hello from my_function!"