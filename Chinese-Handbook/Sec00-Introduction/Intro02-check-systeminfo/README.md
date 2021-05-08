# 系统环境检验

## 获取 CPU 信息


```python
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
```


```python
import psutil

n_logical = psutil.cpu_count()
n_physical = psutil.cpu_count(logical=False)
n_usable = len(psutil.Process().cpu_affinity())

print("=" * 64, "CPU info:", sep="\n")
print(f"    Name:       {get_processor_name()}")
print(f"    Logical:    {n_logical}")
print(f"    Physical:   {n_physical}")
print(f"    Usable:     {n_usable}")
```

    ================================================================
    CPU info:
        Name:       Intel(R) Xeon(R) Gold 5218R CPU @ 2.10GHz
        Logical:    40
        Physical:   20
        Usable:     40
    

## 获取内存信息


```python
import psutil

mem = psutil.virtual_memory()
unit_GB = 1024**3
mem_total = mem.total / unit_GB
mem_free = mem.free / unit_GB
mem_available = mem.available / unit_GB

print("=" * 64, "Memory info:", sep="\n")
print(f"    Total:      {mem_total:.2f} GB")
print(f"    Free:       {mem_free:.2f} GB")
print(f"    Available:  {mem_available:.2f} GB")
```

    ================================================================
    Memory info:
        Total:      31.63 GB
        Free:       24.16 GB
        Available:  24.16 GB
    

## 获取依赖库信息


```python
print("=" * 64, "Package requirements info:", sep="\n")
for module_name in ["numpy", "scipy", "numba", "joblib"]:
    try:
        module = __import__(module_name)
        version = module.__version__
        print(f"    {module_name + ':':12s}{version}")
    except:
        print(f"    Module {module_name} not found.")
```

    ================================================================
    Package requirements info:
        numpy:      1.19.2
        scipy:      1.5.2
        numba:      0.51.2
        joblib:     1.0.0
    

## 获取当前求解器版本信息


```python
import hmsolver

print("=" * 64, "HMSolver info:", sep="\n")
print(f"    Author:     {hmsolver.__author__}")
print(f"    Email:      {hmsolver.__email__}")
print(f"    Version:    {hmsolver.__version__}")
print(f"    License:    {hmsolver.__license__}")
print("=" * 64)
```

    ================================================================
    HMSolver info:
        Author:     Shangkun Shen(polossk)
        Email:      poloshensk@gmail.com
        Version:    0.5.0
        License:    GNU General Public License v3.0
    ================================================================
    

## 附录

### A. `check-systeminfo.py` 文件内容

```python
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
```

### B. `hmsolver-info.py` 文件内容

```python
import hmsolver

if __name__ == '__main__':
    print("=" * 64, "HMSolver info:", sep="\n")
    print(f"    Author:     {hmsolver.__author__}")
    print(f"    Email:      {hmsolver.__email__}")
    print(f"    Version:    {hmsolver.__version__}")
    print(f"    License:    {hmsolver.__license__}")
    print("=" * 64)
```
