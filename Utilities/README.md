# Utilities

> Hybrid-Model-Solver 代码版本：
> [**@1e0a3b2**](https://github.com/polossk/Hybrid-Model-Solver/commit/1e0a3b2ca42645f0b15f6a879c67585da665d33a)

## `convert.py`

* 将 Gmsh 导出的网格文件 (`*.msh` Version 2 ASCII) 转化为 hmsolver 使用的网格文件 (`*.mesh`)
* Usage
   ```shell
   > python convert.py
   ```
* 原始网格中的孤立点将被删除，以保证求解线性方程组时总刚度矩阵不会奇异