python test_of_correction_config_A4.py -t 1 -c const | tee example-A4A1.log
python test_of_correction_config_A4.py -t 2 -c const | tee example-A4A2.log
python test_of_correction_config_A4.py -t 3 -c const | tee example-A4A3.log
python test_of_correction_config_A4.py -t 1 -c exp | tee example-A4B1.log
python test_of_correction_config_A4.py -t 2 -c exp | tee example-A4B2.log
python test_of_correction_config_A4.py -t 3 -c exp | tee example-A4B3.log
echo done