python test_of_correction_config_A5.py -t 0 -c const | tee example-A5A0.log
python test_of_correction_config_A5.py -t 1 -c const | tee example-A5A1.log
python test_of_correction_config_A5.py -t 2 -c const | tee example-A5A2.log
python test_of_correction_config_A5.py -t 0 -c exp | tee example-A5B0.log
python test_of_correction_config_A5.py -t 1 -c exp | tee example-A5B1.log
python test_of_correction_config_A5.py -t 2 -c exp | tee example-A5B2.log
echo done