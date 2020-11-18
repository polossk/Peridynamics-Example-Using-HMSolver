python elas_C.py
python crack_shear_C.py -t 2 -c const -p 200 | tee C12A-200.log
python crack_shear_C.py -t 2 -c exp -p 200 | tee C12C-200.log
echo done
