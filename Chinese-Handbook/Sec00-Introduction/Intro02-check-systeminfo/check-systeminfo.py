import psutil

def get_processor_name():
    import os, platform, subprocess
    
    if platform.system() == "Windows":
        command = "wmic cpu get Name | more +1"
        return subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + "/usr/sbin"
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip().decode()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq"
        return subprocess.check_output(command, shell=True).strip().decode()
    return ""

if __name__ == "__main__":
    # cpu info
    n_logical = psutil.cpu_count()
    n_physical = psutil.cpu_count(logical=False)
    n_usable = len(psutil.Process().cpu_affinity())
    print("=" * 64, "CPU info:", sep="\n")
    print(f"    Name:       {get_processor_name()}")
    print(f"    Logical:    {n_logical}")
    print(f"    Physical:   {n_physical}")
    print(f"    Usable:     {n_usable}")
    # memory info
    mem = psutil.virtual_memory()
    unit_GB = 1024**3
    mem_total = mem.total / unit_GB
    mem_free = mem.free / unit_GB
    mem_available = mem.available / unit_GB
    print("=" * 64, "Memory info:", sep="\n")
    print(f"    Total:      {mem_total:.2f} GB")
    print(f"    Free:       {mem_free:.2f} GB")
    print(f"    Available:  {mem_available:.2f} GB")
    # package requirements info
    print("=" * 64, "Package requirements info:", sep="\n")
    for module_name in ["numpy", "scipy", "numba", "joblib"]:
        try:
            module = __import__(module_name)
            version = module.__version__
            print(f"    {module_name + ':':12s}{version}")
        except:
            print(f"    Module {module_name} not found.")
    print("=" * 64)
