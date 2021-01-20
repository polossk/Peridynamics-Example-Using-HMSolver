# Peridynamics-Example-Using-HMSolver

> Private usage. The HMSolver is private repo. //
> 仅限个人使用。HMSolver 是一个私有的求解器

## Working Directory

* [`Group-2020-11-17`](https://github.com/polossk/Peridynamics-Example-Using-HMSolver/tree/main/Group-2020-11-17): 数值算例组，于 2020 年 11 月 17 日开始整理
* [`Utilities`](https://github.com/polossk/Peridynamics-Example-Using-HMSolver/tree/main/Utilities): 独立常用组件

## Source lines of code (SLOC)

| SLOC             |   python | powershell | markdown |
| :--------------- | -------: | ---------: | -------: |
| .                |          |            |       24 |
| Group-2020-11-17 |     1280 |         60 |      158 |
| Utilities        |        9 |          1 |       12 |
| **Total**        | **1289** |     **61** |  **194** |

* Linux: Shell
   ```shell
   for ext in "*.py" "*.ps1" "*.md"
   do
       wc $(find . -name $ext) -l
   done
   ```
* Windows: PowerShell
   ```powershell
   "*.py", "*.ps1", "*.md" | ForEach-Object { Get-ChildItem -Path .\ -Recurse $_ | Get-Content | Measure-Object -Line }
   ```