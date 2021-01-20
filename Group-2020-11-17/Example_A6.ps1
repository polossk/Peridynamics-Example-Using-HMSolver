python test_of_correction_config_A6.py -t 1 -c const | tee example-A6A1.log
python test_of_correction_config_A6.py -t 2 -c const | tee example-A6A2.log
python test_of_correction_config_A6.py -t 3 -c const | tee example-A6A3.log
python test_of_correction_config_A6.py -t 1 -c exp | tee example-A6B1.log
python test_of_correction_config_A6.py -t 2 -c exp | tee example-A6B2.log
python test_of_correction_config_A6.py -t 3 -c exp | tee example-A6B3.log
echo done