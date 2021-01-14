for ext in "*.py" "*.ps1" "*.md"
do
    wc $(find . -name $ext) -l
done