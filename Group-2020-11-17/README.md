# Usage of Group-2020-11-17

## `test_of_correction_config_A1.py`

* Usage
   ```shell
   > python test_of_correction_config_A1.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |             Description |         Values |
   | :----- | :-------- | ----------------------: | -------------: |
   | `-t`   | `--mtype` | mesh type of simulation |  0, 1, 2, 3, 4 |
   | `-c`   | `--ctype` |       constitutive type | "const", "exp" |
* `Example_A1.ps1`
   ```shell
   python test_of_correction_config_A1.py -t 0 -c const | tee example-A1A0.log
   python test_of_correction_config_A1.py -t 1 -c const | tee example-A1A1.log
   python test_of_correction_config_A1.py -t 2 -c const | tee example-A1A2.log
   python test_of_correction_config_A1.py -t 3 -c const | tee example-A1A3.log
   python test_of_correction_config_A1.py -t 4 -c const | tee example-A1A4.log
   python test_of_correction_config_A1.py -t 0 -c exp | tee example-A1B0.log
   python test_of_correction_config_A1.py -t 1 -c exp | tee example-A1B1.log
   python test_of_correction_config_A1.py -t 2 -c exp | tee example-A1B2.log
   python test_of_correction_config_A1.py -t 3 -c exp | tee example-A1B3.log
   python test_of_correction_config_A1.py -t 4 -c exp | tee example-A1B4.log
   echo done
   ```