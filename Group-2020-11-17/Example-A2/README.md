# Usage of Example-A2

```shell
python test_of_correction_config_A2A.py -t 1 | tee example-A2A1.log
python test_of_correction_config_A2A.py -t 2 | tee example-A2A2.log
python test_of_correction_config_A2A.py -t 3 | tee example-A2A3.log
python test_of_correction_config_A2B.py -t 1 | tee example-A2B1.log
python test_of_correction_config_A2B.py -t 2 | tee example-A2B2.log
python test_of_correction_config_A2B.py -t 3 | tee example-A2B3.log
echo done
```

## `test_of_correction_config_A2A.py`

```shell
> python test_of_correction_config_A2A.py [option] | tee <logfile>
```

* options are
  * `-t`, `--mtype`: mesh type of simulation

## `test_of_correction_config_A2B.py`

```shell
> python test_of_correction_config_A2B.py [option] | tee <logfile>
```

* options are
  * `-t`, `--mtype`: mesh type of simulation
