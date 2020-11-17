# Usage of Example-A1

```shell
> python test_of_correction_config_A1A.py -t 0 | tee example-A1A0.log
> python test_of_correction_config_A1A.py -t 1 | tee example-A1A1.log
> python test_of_correction_config_A1A.py -t 2 | tee example-A1A2.log
> python test_of_correction_config_A1A.py -t 3 | tee example-A1A3.log
> python test_of_correction_config_A1A.py -t 4 | tee example-A1A4.log
> python test_of_correction_config_A1B.py -t 0 | tee example-A1B0.log
> python test_of_correction_config_A1B.py -t 1 | tee example-A1B1.log
> python test_of_correction_config_A1B.py -t 2 | tee example-A1B2.log
> python test_of_correction_config_A1B.py -t 3 | tee example-A1B3.log
> python test_of_correction_config_A1B.py -t 4 | tee example-A1B4.log
> echo done
```

## `test_of_correction_config_A1A.py`

```shell
> python test_of_correction_config_A1A.py [option] | tee <logfile>
```

* options are
  * `-t`, `--mtype`: mesh type of simulation

## `test_of_correction_config_A1B.py`

```shell
> python test_of_correction_config_A1B.py [option] | tee <logfile>
```

* options are
  * `-t`, `--mtype`: mesh type of simulation
