python test_of_correction_config_B.py -r 1 -t 1 -c const | tee example-B1A1.log
python test_of_correction_config_B.py -r 1 -t 2 -c const | tee example-B1A2.log
python test_of_correction_config_B.py -r 2 -t 1 -c const | tee example-B2A1.log
python test_of_correction_config_B.py -r 2 -t 2 -c const | tee example-B2A2.log
python test_of_correction_config_B.py -r 3 -t 1 -c const | tee example-B3A1.log
python test_of_correction_config_B.py -r 3 -t 2 -c const | tee example-B3A2.log
python test_of_correction_config_B.py -r 1 -t 1 -c exp | tee example-B1B1.log
python test_of_correction_config_B.py -r 1 -t 2 -c exp | tee example-B1B2.log
python test_of_correction_config_B.py -r 2 -t 1 -c exp | tee example-B2B1.log
python test_of_correction_config_B.py -r 2 -t 2 -c exp | tee example-B2B2.log
python test_of_correction_config_B.py -r 3 -t 1 -c exp | tee example-B3B1.log
python test_of_correction_config_B.py -r 3 -t 2 -c exp | tee example-B3B2.log
echo done
