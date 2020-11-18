python test_of_correction_config_A2.py -t 1 -c const | tee example-A2A1.log
python test_of_correction_config_A2.py -t 2 -c const | tee example-A2A2.log
python test_of_correction_config_A2.py -t 3 -c const | tee example-A2A3.log
python test_of_correction_config_A2.py -t 1 -c exp | tee example-A2B1.log
python test_of_correction_config_A2.py -t 2 -c exp | tee example-A2B2.log
python test_of_correction_config_A2.py -t 3 -c exp | tee example-A2B3.log
echo done
