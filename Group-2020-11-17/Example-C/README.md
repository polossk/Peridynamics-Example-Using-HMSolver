# Usage of Example-C

```shell
> python elas.py
> python crack_shear.py -t 2 -p 200 | tee C12A-200.log
> python crack_shear_only_exp.py -t 2 -p 200 | tee C12C-200.log
```

## `elas.py`

```shell
> python elas.py
```

## `crack_shear.py`

```shell
> python crack_shear.py [option] | tee <logfile>
```

* options are
  * `-n`, `--name`: name of simulation
  * `-r`, `--runid`: sub number(runid) of simulation
  * `-t`, `--mtype`: mesh type of simulation
  * `-p`, `--phase`: total phase of simulation

## `crack_shear_only_exp.py`

```shell
> python crack_shear_only_exp.py [option] | tee <logfile>
```

* options are
  * `-n`, `--name`: name of simulation
  * `-r`, `--runid`: sub number(runid) of simulation
  * `-t`, `--mtype`: mesh type of simulation
  * `-p`, `--phase`: total phase of simulation
