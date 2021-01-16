"*.py", "*.ps1", "*.md" | ForEach-Object { Get-ChildItem -Path .\ -Recurse $_ | Get-Content | Measure-Object -Line }
