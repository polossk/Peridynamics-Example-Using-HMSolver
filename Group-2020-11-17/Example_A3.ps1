python test_of_correction_config_A3.py -t 1 -c const | tee example-A3A1.log
python test_of_correction_config_A3.py -t 2 -c const | tee example-A3A2.log
python test_of_correction_config_A3.py -t 3 -c const | tee example-A3A3.log
python test_of_correction_config_A3.py -t 1 -c exp | tee example-A3B1.log
python test_of_correction_config_A3.py -t 2 -c exp | tee example-A3B2.log
python test_of_correction_config_A3.py -t 3 -c exp | tee example-A3B3.log
echo done