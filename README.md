# Peridynamics-Example-Using-HMSolver

> Private usage. The HMSolver is private repo. //
> 仅限个人使用。HMSolver 是一个私有的求解器

## Working Directory

* [`Group-2020-11-17`](https://github.com/polossk/Peridynamics-Example-Using-HMSolver/tree/main/Group-2020-11-17): 数值算例组，于 2020 年 11 月 17 日开始整理
* [`Utilities`](https://github.com/polossk/Peridynamics-Example-Using-HMSolver/tree/main/Utilities): 独立常用组件

## Source lines of code (SLOC)

| SLOC             |   python | powershell | markdown |
| :--------------- | -------: | ---------: | -------: |
| .                |          |            |       26 |
| Chinese-Handbook |       47 |            |      505 |
| Examples         |      197 |            |      498 |
| Group-2020-11-17 |     1496 |         67 |      178 |
| Utilities        |        9 |          1 |       12 |
| **Total**        | **1749** |     **68** | **1219** |

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