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
            "total": bytes,    # 总内存
            "used": memroy.used,      # 已使用内存
            "free": memory.available, # 客用内存
            "percent": memory.percent # 内存使用百分比
        }

        
        """
        memory = psutil.virtual_memory()
        return {
            "total": memory.total,    # 
            "used": memory.used,      # 已使用内存
            "free": memory.available, # 客用内存
            "percent": memory.percent # 内存使用百分比
        }

def my_function():
    return "Hello from my_function!"