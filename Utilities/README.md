# Utilities

> Hybrid-Model-Solver 代码版本：
> [**0.4.5a0 (@8fbddad)**](https://github.com/polossk/Hybrid-Model-Solver/commit/8fbddad44c8ff5550a0867ef94cac9ca8bd6a487)

## `convert.py`

* 将 Gmsh 导出的网格文件 (`*.msh` Version 2 ASCII) 转化为 hmsolver 使用的网格文件 (`*.mesh`)
* Usage
   ```shell
   > python convert.py
   ```
* 原始网格中的孤立点将被删除，以保证求解线性方程组时总刚度矩阵不会奇异

## `sloc.sh` 和 `sloc.ps1`

* 统计当前文件目录下所有 `*.py`, `*.ps1`, `*.md` 文件的行数

