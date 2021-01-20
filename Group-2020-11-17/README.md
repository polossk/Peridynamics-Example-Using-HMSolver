# Usage of Group-2020-11-17

> Hybrid-Model-Solver 代码版本：
> [**0.4.5a0 (@8fbddad)**](https://github.com/polossk/Hybrid-Model-Solver/commit/8fbddad44c8ff5550a0867ef94cac9ca8bd6a487)

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

## `test_of_correction_config_A2.py`

* Usage
   ```shell
   > python test_of_correction_config_A2.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |             Description |         Values |
   | :----- | :-------- | ----------------------: | -------------: |
   | `-t`   | `--mtype` | mesh type of simulation |  1, 2, 3, 4, 5 |
   | `-c`   | `--ctype` |       constitutive type | "const", "exp" |
* `Example_A2.ps1`
   ```shell
   python test_of_correction_config_A2.py -t 1 -c const | tee example-A2A1.log
   python test_of_correction_config_A2.py -t 2 -c const | tee example-A2A2.log
   python test_of_correction_config_A2.py -t 3 -c const | tee example-A2A3.log
   python test_of_correction_config_A2.py -t 4 -c const | tee example-A2A4.log
   python test_of_correction_config_A2.py -t 5 -c const | tee example-A2A5.log
   python test_of_correction_config_A2.py -t 1 -c exp | tee example-A2B1.log
   python test_of_correction_config_A2.py -t 2 -c exp | tee example-A2B2.log
   python test_of_correction_config_A2.py -t 3 -c exp | tee example-A2B3.log
   python test_of_correction_config_A2.py -t 4 -c exp | tee example-A2B4.log
   python test_of_correction_config_A2.py -t 5 -c exp | tee example-A2B5.log
   echo done
   ```

## `test_of_correction_config_A3.py`

* Usage
   ```shell
   > python test_of_correction_config_A3.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |             Description |         Values |
   | :----- | :-------- | ----------------------: | -------------: |
   | `-t`   | `--mtype` | mesh type of simulation |        1, 2, 3 |
   | `-c`   | `--ctype` |       constitutive type | "const", "exp" |
* `Example_A3.ps1`
   ```shell
   python test_of_correction_config_A3.py -t 1 -c const | tee example-A3A1.log
   python test_of_correction_config_A3.py -t 2 -c const | tee example-A3A2.log
   python test_of_correction_config_A3.py -t 3 -c const | tee example-A3A3.log
   python test_of_correction_config_A3.py -t 1 -c exp | tee example-A3B1.log
   python test_of_correction_config_A3.py -t 2 -c exp | tee example-A3B2.log
   python test_of_correction_config_A3.py -t 3 -c exp | tee example-A3B3.log
   echo done
   ```

## `test_of_correction_config_A4.py`

* Usage
   ```shell
   > python test_of_correction_config_A4.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |             Description |         Values |
   | :----- | :-------- | ----------------------: | -------------: |
   | `-t`   | `--mtype` | mesh type of simulation |        1, 2, 3 |
   | `-c`   | `--ctype` |       constitutive type | "const", "exp" |
* `Example_A4.ps1`
   ```shell
   python test_of_correction_config_A4.py -t 1 -c const | tee example-A4A1.log
   python test_of_correction_config_A4.py -t 2 -c const | tee example-A4A2.log
   python test_of_correction_config_A4.py -t 3 -c const | tee example-A4A3.log
   python test_of_correction_config_A4.py -t 1 -c exp | tee example-A4B1.log
   python test_of_correction_config_A4.py -t 2 -c exp | tee example-A4B2.log
   python test_of_correction_config_A4.py -t 3 -c exp | tee example-A4B3.log
   echo done
   ```

## `test_of_correction_config_A5.py`

* Usage
   ```shell
   > python test_of_correction_config_A5.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |             Description |         Values |
   | :----- | :-------- | ----------------------: | -------------: |
   | `-t`   | `--mtype` | mesh type of simulation |        0, 1, 2 |
   | `-c`   | `--ctype` |       constitutive type | "const", "exp" |
* `Example_A5.ps1`
   ```shell
   python test_of_correction_config_A5.py -t 0 -c const | tee example-A5A0.log
   python test_of_correction_config_A5.py -t 1 -c const | tee example-A5A1.log
   python test_of_correction_config_A5.py -t 2 -c const | tee example-A5A2.log
   python test_of_correction_config_A5.py -t 0 -c exp | tee example-A5B0.log
   python test_of_correction_config_A5.py -t 1 -c exp | tee example-A5B1.log
   python test_of_correction_config_A5.py -t 2 -c exp | tee example-A5B2.log
   echo done
   ```

## `test_of_correction_config_B.py`

* Usage
   ```shell
   > python test_of_correction_config_B.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |                     Description |         Values |
   | :----- | :-------- | ------------------------------: | -------------: |
   | `-r`   | `--runid` | sub number(runid) of simulation |        1, 2, 3 |
   | `-t`   | `--mtype` |         mesh type of simulation |           1, 2 |
   | `-c`   | `--ctype` |               constitutive type | "const", "exp" |
* `Example_B.ps1`
   ```shell
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
   ```

## `crack_shear_C.py` & `elas_C.py`

* Usage
   ```shell
   > python crack_shear_C.py [option] | tee <logfile>
   ```
* Options
   | Option | Full name |                     Description |                             Values |
   | :----- | :-------- | ------------------------------: | ---------------------------------: |
   | `-n`   | `--name`  |              name of simulation |                                'C' |
   | `-r`   | `--runid` | sub number(runid) of simulation |                                  1 |
   | `-t`   | `--mtype` |         mesh type of simulation |                               1, 2 |
   | `-c`   | `--ctype` |               constitutive type |                     "const", "exp" |
   | `-p`   | `--phase` |       total phase of simulation | positive intergers ($\mathbb Z^+$) |
* `Example_C.ps1`
   ```shell
   python elas_C.py
   python crack_shear_C.py -t 2 -c const -p 200 | tee C12A-200.log
   python crack_shear_C.py -t 2 -c exp -p 200 | tee C12B-200.log
   echo done
   ```
