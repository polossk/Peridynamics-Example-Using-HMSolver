python elas.py
python crack_shear.py -t 2 -p 200 | tee C12A-200.log
python crack_shear_only_exp.py -t 2 -p 200 | tee C12C-200.log
echo done
