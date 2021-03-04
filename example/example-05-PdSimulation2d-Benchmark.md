# Benchmark

| Problem Scale | 10x10 | 20x20 | 40x40 | 80x80 |
| :------------ | ----: | ----: | ----: | ----: |
| Elements      |   100 |   400 |  1600 |  6400 |
| Nodes         |   121 |   441 |  1681 |  6561 |
| Buckets       |     1 |     4 |    16 |    49 |
| Barrels       |     1 |     1 |     9 |    36 |
| DOF           |   242 |   882 |  3362 |       |


| Sections                    | 10x10 |  10x10* | 20x20 |  20x20* | 40x40 |  40x40* | 80x80 |  80x80* |
| :-------------------------- | ----: | ------: | ----: | ------: | ----: | ------: | ----: | ------: |
| 1 Mesh Preprocessing        |  0.02 |    0.02 |  0.12 |    0.12 |  1.25 |    1.23 |  6.66 |    6.62 |
| 1.1 Bucket Generation       |  0.00 |    0.00 |  0.00 |    0.00 |  0.02 |    0.00 |  0.00 |    0.00 |
| 1.2 Bond Building           |  0.02 |    0.00 |  0.11 |    0.09 |  1.14 |    1.14 |  6.23 |    6.19 |
| 1.3 Bucket Sorting          |  0.00 |    0.00 |  0.00 |    0.00 |  0.00 |    0.00 |  0.03 |    0.03 |
| 2 Problem Solving           |  0.80 |    0.56 |  2.86 |    2.62 | 12.67 |   11.56 | 54.66 |   49.92 |
| 2.1 PD Stiffness Assembling |  0.59 |    0.56 |  2.80 |    2.53 | 12.12 |   11.01 | 49.99 |   45.23 |
| *Time Reduction             |     - |  94.92% |     - |  90.36% |     - |  90.84% |     - |  90.48% |
| *Boosting                   |     - | 105.36% |     - | 110.67% |     - | 110.08% |     - | 110.52% |
| 2.2 Solving Linear System   |  0.00 |    0.00 |  0.06 |    0.06 |  0.55 |    0.55 |  4.67 |    4.69 |


# Logs

## 10x10

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [2.58795512e+20 2.58795512e+20 2.70966629e+20]
Separate into 1 bucket(s).The bucket grid is about 1x1.
It will be handled by 1 barrel(s).
Prepared. Cost 0.00s
handle barrel completed. Cost 0.02s
sorting bond completed. Cost 0.00s
building bond completed. Total 0.02s
## All data completed. Total 0.02s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix processing 21%, working on 227/1058, used 0.11s, eta 0.40s
        assembling PD-stiffness martix processing 39%, working on 416/1058, used 0.22s, eta 0.34s
        assembling PD-stiffness martix processing 58%, working on 610/1058, used 0.33s, eta 0.24s
        assembling PD-stiffness martix processing 77%, working on 810/1058, used 0.44s, eta 0.13s
        assembling PD-stiffness martix processing 93%, working on 979/1058, used 0.55s, eta 0.04s
        assembling PD-stiffness martix processing 100%, working on 1057/1058, used 0.59s, eta 0.00s
        assembling completed. Total 0.59s
Solving Linear System: DOF=242.
Linear System Solved. Time cost= 0.00s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 20x20

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [2.48575695e+20 2.48575695e+20 2.38580104e+20]
Separate into 4 bucket(s).The bucket grid is about 2x2.
It will be handled by 1 barrel(s).
Prepared. Cost 0.00s
handle barrel completed. Cost 0.11s
sorting bond completed. Cost 0.00s
building bond completed. Total 0.11s
## All data completed. Total 0.12s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix processing 18%, working on 864/4898, used 0.47s, eta 2.19s
        assembling PD-stiffness martix processing 35%, working on 1706/4898, used 0.95s, eta 1.78s
        assembling PD-stiffness martix processing 52%, working on 2548/4898, used 1.44s, eta 1.33s
        assembling PD-stiffness martix processing 69%, working on 3389/4898, used 1.92s, eta 0.86s
        assembling PD-stiffness martix processing 86%, working on 4214/4898, used 2.37s, eta 0.39s
        assembling PD-stiffness martix processing 99%, working on 4862/4898, used 2.77s, eta 0.02s
        assembling completed. Total 2.80s
Solving Linear System: DOF=882.
Linear System Solved. Time cost= 0.06s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 40x40

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [6.81584670e+20 6.81584670e+20 5.60024753e+20]
Separate into 16 bucket(s).The bucket grid is about 4x4.
It will be handled by 9 barrel(s).
Prepared. Cost 0.02s
building bonds with buckets processing 22%, working on 2/9, used 0.17s, eta 0.60s
building bonds with buckets processing 33%, working on 3/9, used 0.36s, eta 0.72s
building bonds with buckets processing 44%, working on 4/9, used 0.45s, eta 0.57s
building bonds with buckets processing 56%, working on 5/9, used 0.62s, eta 0.50s
building bonds with buckets processing 67%, working on 6/9, used 0.81s, eta 0.41s
building bonds with buckets processing 78%, working on 7/9, used 0.91s, eta 0.26s
building bonds with buckets processing 89%, working on 8/9, used 1.00s, eta 0.12s
building bonds with buckets processing 100%, working on 9/9, used 1.09s, eta 0.00s
handle barrel completed. Cost 1.14s
sorting bond completed. Cost 0.00s
building bond completed. Total 1.14s
## All data completed. Total 1.25s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix processing 17%, working on 3498/20978, used 2.00s, eta 9.99s
        assembling PD-stiffness martix processing 33%, working on 6974/20978, used 3.98s, eta 8.00s
        assembling PD-stiffness martix processing 50%, working on 10432/20978, used 6.00s, eta 6.06s
        assembling PD-stiffness martix processing 66%, working on 13908/20978, used 7.98s, eta 4.06s
        assembling PD-stiffness martix processing 83%, working on 17366/20978, used 10.00s, eta 2.08s
        assembling PD-stiffness martix processing 99%, working on 20697/20978, used 11.95s, eta 0.16s
        assembling completed. Total 12.12s
Solving Linear System: DOF=3362.
Linear System Solved. Time cost= 0.55s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 80x80

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [6.53783516e+21 6.53783516e+21 4.74309992e+21]
Separate into 49 bucket(s).The bucket grid is about 7x7.
It will be handled by 36 barrel(s).
Prepared. Cost 0.00s
building bonds with buckets processing 6%, working on 2/36, used 0.19s, eta 3.19s
building bonds with buckets processing 8%, working on 3/36, used 0.37s, eta 4.12s
building bonds with buckets processing 11%, working on 4/36, used 0.56s, eta 4.50s
building bonds with buckets processing 14%, working on 5/36, used 0.75s, eta 4.65s
building bonds with buckets processing 17%, working on 6/36, used 0.94s, eta 4.69s
building bonds with buckets processing 19%, working on 7/36, used 1.06s, eta 4.40s
building bonds with buckets processing 22%, working on 8/36, used 1.27s, eta 4.43s
building bonds with buckets processing 25%, working on 9/36, used 1.45s, eta 4.36s
building bonds with buckets processing 28%, working on 10/36, used 1.64s, eta 4.27s
building bonds with buckets processing 31%, working on 11/36, used 1.83s, eta 4.15s
building bonds with buckets processing 33%, working on 12/36, used 2.02s, eta 4.03s
building bonds with buckets processing 36%, working on 13/36, used 2.16s, eta 3.81s
building bonds with buckets processing 39%, working on 14/36, used 2.34s, eta 3.68s
building bonds with buckets processing 42%, working on 15/36, used 2.55s, eta 3.57s
building bonds with buckets processing 44%, working on 16/36, used 2.73s, eta 3.42s
building bonds with buckets processing 47%, working on 17/36, used 2.92s, eta 3.27s
building bonds with buckets processing 50%, working on 18/36, used 3.12s, eta 3.12s
building bonds with buckets processing 53%, working on 19/36, used 3.27s, eta 2.92s
building bonds with buckets processing 56%, working on 20/36, used 3.45s, eta 2.76s
building bonds with buckets processing 58%, working on 21/36, used 3.64s, eta 2.60s
building bonds with buckets processing 61%, working on 22/36, used 3.83s, eta 2.44s
building bonds with buckets processing 64%, working on 23/36, used 4.02s, eta 2.27s
building bonds with buckets processing 67%, working on 24/36, used 4.20s, eta 2.10s
building bonds with buckets processing 69%, working on 25/36, used 4.34s, eta 1.91s
building bonds with buckets processing 72%, working on 26/36, used 4.53s, eta 1.74s
building bonds with buckets processing 75%, working on 27/36, used 4.73s, eta 1.58s
building bonds with buckets processing 78%, working on 28/36, used 4.92s, eta 1.41s
building bonds with buckets processing 81%, working on 29/36, used 5.11s, eta 1.23s
building bonds with buckets processing 83%, working on 30/36, used 5.30s, eta 1.06s
building bonds with buckets processing 86%, working on 31/36, used 5.44s, eta 0.88s
building bonds with buckets processing 89%, working on 32/36, used 5.58s, eta 0.70s
building bonds with buckets processing 92%, working on 33/36, used 5.72s, eta 0.52s
building bonds with buckets processing 94%, working on 34/36, used 5.84s, eta 0.34s
building bonds with buckets processing 97%, working on 35/36, used 5.98s, eta 0.17s
building bonds with buckets processing 100%, working on 36/36, used 6.12s, eta 0.00s
handle barrel completed. Cost 6.23s
sorting bond completed. Cost 0.03s
building bond completed. Total 6.26s
## All data completed. Total 6.66s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix processing 16%, working on 14142/86738, used 8.08s, eta 41.46s
        assembling PD-stiffness martix processing 33%, working on 28244/86738, used 16.19s, eta 33.52s
        assembling PD-stiffness martix processing 49%, working on 42346/86738, used 24.39s, eta 25.57s
        assembling PD-stiffness martix processing 65%, working on 56448/86738, used 32.48s, eta 17.43s
        assembling PD-stiffness martix processing 81%, working on 70550/86738, used 40.61s, eta 9.32s
        assembling PD-stiffness martix processing 98%, working on 84670/86738, used 48.57s, eta 1.19s
        assembling completed. Total 49.99s
Solving Linear System: DOF=13122.
Linear System Solved. Time cost= 4.67s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 10x10 8 Threads

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [2.58795512e+20 2.58795512e+20 2.70966629e+20]
Separate into 1 bucket(s).The bucket grid is about 1x1.
It will be handled by 1 barrel(s).
Prepared. Cost 0.00s
handle barrel completed. Cost 0.00s
sorting bond completed. Cost 0.00s
building bond completed. Total 0.00s
## All data completed. Total 0.02s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix  into parallel
        split worklist into 8 chunk(s).
            Thread 4:  processing 33%, working on 4/12, used 0.16s, eta 0.31s
            Thread 7:  processing 38%, working on 6/16, used 0.16s, eta 0.26s
            Thread 3:  processing 33%, working on 4/12, used 0.17s, eta 0.34s
            Thread 0:  processing 33%, working on 4/12, used 0.20s, eta 0.41s
            Thread 6:  processing 33%, working on 4/12, used 0.20s, eta 0.41s
            Thread 5:  processing 33%, working on 4/12, used 0.20s, eta 0.41s
            Thread 1:  processing 33%, working on 4/12, used 0.22s, eta 0.44s
            Thread 7:  processing 69%, working on 11/16, used 0.22s, eta 0.10s
            Thread 2:  processing 33%, working on 4/12, used 0.25s, eta 0.50s
        Thread 7:  proceed from 84 to 99 completed. Total 0.25s
            Thread 6:  processing 67%, working on 8/12, used 0.34s, eta 0.17s
            Thread 3:  processing 67%, working on 8/12, used 0.36s, eta 0.18s
            Thread 4:  processing 67%, working on 8/12, used 0.36s, eta 0.18s
            Thread 1:  processing 67%, working on 8/12, used 0.37s, eta 0.19s
            Thread 0:  processing 67%, working on 8/12, used 0.39s, eta 0.20s
            Thread 2:  processing 67%, working on 8/12, used 0.39s, eta 0.20s
            Thread 5:  processing 67%, working on 8/12, used 0.41s, eta 0.20s
        Thread 6:  proceed from 72 to 83 completed. Total 0.44s
        Thread 0:  proceed from 0 to 11 completed. Total 0.50s
        Thread 5:  proceed from 60 to 71 completed. Total 0.52s
        Thread 4:  proceed from 48 to 59 completed. Total 0.52s
        Thread 3:  proceed from 36 to 47 completed. Total 0.52s
        Thread 1:  proceed from 12 to 23 completed. Total 0.52s
        Thread 2:  proceed from 24 to 35 completed. Total 0.53s
        Kpd assembling completed (Parallel). Total 0.56s
Solving Linear System: DOF=242.
Linear System Solved. Time cost= 0.00s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```


## 20x20 8 Threads

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [2.48575695e+20 2.48575695e+20 2.38580104e+20]
Separate into 4 bucket(s).The bucket grid is about 2x2.
It will be handled by 1 barrel(s).
Prepared. Cost 0.00s
handle barrel completed. Cost 0.09s
sorting bond completed. Cost 0.00s
building bond completed. Total 0.09s
## All data completed. Total 0.12s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix  into parallel
        split worklist into 8 chunk(s).
            Thread 7:  processing 34%, working on 17/50, used 0.67s, eta 1.30s
            Thread 4:  processing 34%, working on 17/50, used 0.83s, eta 1.61s
            Thread 3:  processing 34%, working on 17/50, used 0.84s, eta 1.64s
            Thread 1:  processing 34%, working on 17/50, used 0.84s, eta 1.64s
            Thread 6:  processing 34%, working on 17/50, used 0.89s, eta 1.73s
            Thread 5:  processing 34%, working on 17/50, used 0.91s, eta 1.76s
            Thread 2:  processing 34%, working on 17/50, used 0.95s, eta 1.85s
            Thread 7:  processing 66%, working on 33/50, used 1.05s, eta 0.54s
            Thread 0:  processing 34%, working on 17/50, used 1.06s, eta 2.06s
            Thread 7:  processing 98%, working on 49/50, used 1.23s, eta 0.03s
        Thread 7:  proceed from 350 to 399 completed. Total 1.23s
            Thread 4:  processing 66%, working on 33/50, used 1.53s, eta 0.79s
            Thread 1:  processing 66%, working on 33/50, used 1.58s, eta 0.81s
            Thread 3:  processing 66%, working on 33/50, used 1.58s, eta 0.81s
            Thread 6:  processing 66%, working on 33/50, used 1.64s, eta 0.85s
            Thread 5:  processing 66%, working on 33/50, used 1.72s, eta 0.89s
            Thread 2:  processing 66%, working on 33/50, used 1.72s, eta 0.89s
            Thread 0:  processing 66%, working on 33/50, used 1.95s, eta 1.01s
            Thread 4:  processing 98%, working on 49/50, used 2.19s, eta 0.04s
        Thread 4:  proceed from 200 to 249 completed. Total 2.23s
            Thread 6:  processing 98%, working on 49/50, used 2.28s, eta 0.05s
            Thread 1:  processing 98%, working on 49/50, used 2.28s, eta 0.05s
        Thread 1:  proceed from 50 to 99 completed. Total 2.30s
        Thread 6:  proceed from 300 to 349 completed. Total 2.31s
            Thread 3:  processing 98%, working on 49/50, used 2.33s, eta 0.05s
        Thread 3:  proceed from 150 to 199 completed. Total 2.33s
            Thread 2:  processing 98%, working on 49/50, used 2.37s, eta 0.05s
            Thread 5:  processing 98%, working on 49/50, used 2.39s, eta 0.05s
        Thread 2:  proceed from 100 to 149 completed. Total 2.41s
        Thread 5:  proceed from 250 to 299 completed. Total 2.41s
            Thread 0:  processing 98%, working on 49/50, used 2.44s, eta 0.05s
        Thread 0:  proceed from 0 to 49 completed. Total 2.45s
        Kpd assembling completed (Parallel). Total 2.53s
Solving Linear System: DOF=882.
Linear System Solved. Time cost= 0.06s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 40x40 8 Threads

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [6.81584670e+20 6.81584670e+20 5.60024753e+20]
Separate into 16 bucket(s).The bucket grid is about 4x4.
It will be handled by 9 barrel(s).
Prepared. Cost 0.00s
building bonds with buckets processing 22%, working on 2/9, used 0.17s, eta 0.60s
building bonds with buckets processing 33%, working on 3/9, used 0.36s, eta 0.72s
building bonds with buckets processing 44%, working on 4/9, used 0.45s, eta 0.57s
building bonds with buckets processing 56%, working on 5/9, used 0.62s, eta 0.50s
building bonds with buckets processing 67%, working on 6/9, used 0.81s, eta 0.41s
building bonds with buckets processing 78%, working on 7/9, used 0.91s, eta 0.26s
building bonds with buckets processing 89%, working on 8/9, used 1.00s, eta 0.12s
building bonds with buckets processing 100%, working on 9/9, used 1.09s, eta 0.00s
handle barrel completed. Cost 1.14s
sorting bond completed. Cost 0.00s
building bond completed. Total 1.14s
## All data completed. Total 1.23s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix  into parallel
        split worklist into 8 chunk(s).
            Thread 1:  processing 32%, working on 65/200, used 3.41s, eta 7.07s
            Thread 0:  processing 32%, working on 65/200, used 3.45s, eta 7.17s
            Thread 6:  processing 32%, working on 65/200, used 3.50s, eta 7.27s
            Thread 7:  processing 32%, working on 65/200, used 3.52s, eta 7.30s
            Thread 2:  processing 32%, working on 65/200, used 3.58s, eta 7.43s
            Thread 3:  processing 32%, working on 65/200, used 3.67s, eta 7.63s
            Thread 5:  processing 32%, working on 65/200, used 3.73s, eta 7.76s
            Thread 4:  processing 32%, working on 65/200, used 3.97s, eta 8.24s
            Thread 7:  processing 64%, working on 129/200, used 6.67s, eta 3.67s
            Thread 1:  processing 64%, working on 129/200, used 6.80s, eta 3.74s
            Thread 0:  processing 64%, working on 129/200, used 6.81s, eta 3.75s
            Thread 6:  processing 64%, working on 129/200, used 6.81s, eta 3.75s
            Thread 2:  processing 64%, working on 129/200, used 7.09s, eta 3.90s
            Thread 3:  processing 64%, working on 129/200, used 7.26s, eta 4.00s
            Thread 5:  processing 64%, working on 129/200, used 7.42s, eta 4.08s
            Thread 4:  processing 64%, working on 129/200, used 7.92s, eta 4.36s
            Thread 7:  processing 96%, working on 193/200, used 8.06s, eta 0.29s
        Thread 7:  proceed from 1400 to 1599 completed. Total 8.14s
            Thread 1:  processing 96%, working on 193/200, used 9.95s, eta 0.36s
            Thread 0:  processing 96%, working on 193/200, used 9.98s, eta 0.36s
            Thread 6:  processing 96%, working on 193/200, used 10.01s, eta 0.36s
        Thread 1:  proceed from 200 to 399 completed. Total 10.25s
        Thread 0:  proceed from 0 to 199 completed. Total 10.30s
        Thread 6:  proceed from 1200 to 1399 completed. Total 10.30s
            Thread 2:  processing 96%, working on 193/200, used 10.33s, eta 0.37s
            Thread 3:  processing 96%, working on 193/200, used 10.45s, eta 0.38s
        Thread 2:  proceed from 400 to 599 completed. Total 10.51s
            Thread 5:  processing 96%, working on 193/200, used 10.53s, eta 0.38s
        Thread 3:  proceed from 600 to 799 completed. Total 10.61s
        Thread 5:  proceed from 1000 to 1199 completed. Total 10.64s
            Thread 4:  processing 96%, working on 193/200, used 10.69s, eta 0.39s
        Thread 4:  proceed from 800 to 999 completed. Total 10.73s
        Kpd assembling completed (Parallel). Total 11.01s
Solving Linear System: DOF=3362.
Linear System Solved. Time cost= 0.55s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```

## 20x20 8 Threads

```plain
Synchronize Complete. Ratio= [1. 1. 1.]
Constitutive: (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic:  (C11, C22, C33)= [3.375e+11 3.375e+11 1.125e+11]
Peridynamic Coefficients= [6.53783516e+21 6.53783516e+21 4.74309992e+21]
Separate into 49 bucket(s).The bucket grid is about 7x7.
It will be handled by 36 barrel(s).
Prepared. Cost 0.00s
building bonds with buckets processing 6%, working on 2/36, used 0.19s, eta 3.19s
building bonds with buckets processing 8%, working on 3/36, used 0.37s, eta 4.12s
building bonds with buckets processing 11%, working on 4/36, used 0.55s, eta 4.37s
building bonds with buckets processing 14%, working on 5/36, used 0.73s, eta 4.55s
building bonds with buckets processing 17%, working on 6/36, used 0.92s, eta 4.61s
building bonds with buckets processing 19%, working on 7/36, used 1.06s, eta 4.40s
building bonds with buckets processing 22%, working on 8/36, used 1.25s, eta 4.37s
building bonds with buckets processing 25%, working on 9/36, used 1.44s, eta 4.31s
building bonds with buckets processing 28%, working on 10/36, used 1.62s, eta 4.22s
building bonds with buckets processing 31%, working on 11/36, used 1.83s, eta 4.15s
building bonds with buckets processing 33%, working on 12/36, used 2.02s, eta 4.03s
building bonds with buckets processing 36%, working on 13/36, used 2.16s, eta 3.81s
building bonds with buckets processing 39%, working on 14/36, used 2.34s, eta 3.68s
building bonds with buckets processing 42%, working on 15/36, used 2.53s, eta 3.54s
building bonds with buckets processing 44%, working on 16/36, used 2.72s, eta 3.40s
building bonds with buckets processing 47%, working on 17/36, used 2.91s, eta 3.25s
building bonds with buckets processing 50%, working on 18/36, used 3.09s, eta 3.09s
building bonds with buckets processing 53%, working on 19/36, used 3.23s, eta 2.89s
building bonds with buckets processing 56%, working on 20/36, used 3.42s, eta 2.74s
building bonds with buckets processing 58%, working on 21/36, used 3.61s, eta 2.58s
building bonds with buckets processing 61%, working on 22/36, used 3.80s, eta 2.42s
building bonds with buckets processing 64%, working on 23/36, used 4.00s, eta 2.26s
building bonds with buckets processing 67%, working on 24/36, used 4.19s, eta 2.09s
building bonds with buckets processing 69%, working on 25/36, used 4.31s, eta 1.90s
building bonds with buckets processing 72%, working on 26/36, used 4.50s, eta 1.73s
building bonds with buckets processing 75%, working on 27/36, used 4.70s, eta 1.57s
building bonds with buckets processing 78%, working on 28/36, used 4.89s, eta 1.40s
building bonds with buckets processing 81%, working on 29/36, used 5.08s, eta 1.23s
building bonds with buckets processing 83%, working on 30/36, used 5.27s, eta 1.05s
building bonds with buckets processing 86%, working on 31/36, used 5.41s, eta 0.87s
building bonds with buckets processing 89%, working on 32/36, used 5.55s, eta 0.69s
building bonds with buckets processing 92%, working on 33/36, used 5.67s, eta 0.52s
building bonds with buckets processing 94%, working on 34/36, used 5.81s, eta 0.34s
building bonds with buckets processing 97%, working on 35/36, used 5.95s, eta 0.17s
building bonds with buckets processing 100%, working on 36/36, used 6.09s, eta 0.00s
handle barrel completed. Cost 6.19s
sorting bond completed. Cost 0.03s
building bond completed. Total 6.22s
## All data completed. Total 6.62s
********************************
Simulation Manual Checking:
Mesh is ready.
Material is ready.
Boundary Conds is ready.
Basis is ready.
OK.
********************************
        assembling PD-stiffness martix  into parallel
        split worklist into 8 chunk(s).
            Thread 1:  processing 32%, working on 257/800, used 13.33s, eta 28.16s
            Thread 0:  processing 32%, working on 257/800, used 13.86s, eta 29.28s
            Thread 5:  processing 32%, working on 257/800, used 13.87s, eta 29.31s
            Thread 6:  processing 32%, working on 257/800, used 14.08s, eta 29.74s
            Thread 2:  processing 32%, working on 257/800, used 14.62s, eta 30.90s
            Thread 7:  processing 32%, working on 257/800, used 14.81s, eta 31.29s
            Thread 4:  processing 32%, working on 257/800, used 15.26s, eta 32.25s
            Thread 3:  processing 32%, working on 257/800, used 15.31s, eta 32.35s
            Thread 1:  processing 64%, working on 513/800, used 26.64s, eta 14.90s
            Thread 5:  processing 64%, working on 513/800, used 27.54s, eta 15.41s
            Thread 0:  processing 64%, working on 513/800, used 27.58s, eta 15.43s
            Thread 6:  processing 64%, working on 513/800, used 28.14s, eta 15.74s
            Thread 2:  processing 64%, working on 513/800, used 29.18s, eta 16.33s
            Thread 7:  processing 64%, working on 513/800, used 29.59s, eta 16.55s
            Thread 4:  processing 64%, working on 513/800, used 30.58s, eta 17.11s
            Thread 3:  processing 64%, working on 513/800, used 30.62s, eta 17.13s
            Thread 7:  processing 96%, working on 769/800, used 39.90s, eta 1.61s
            Thread 1:  processing 96%, working on 769/800, used 39.90s, eta 1.61s
        Thread 7:  proceed from 5600 to 6399 completed. Total 40.26s
            Thread 0:  processing 96%, working on 769/800, used 41.03s, eta 1.65s
            Thread 5:  processing 96%, working on 769/800, used 41.23s, eta 1.66s
        Thread 1:  proceed from 800 to 1599 completed. Total 41.34s
            Thread 6:  processing 96%, working on 769/800, used 41.93s, eta 1.69s
        Thread 0:  proceed from 0 to 799 completed. Total 42.31s
        Thread 5:  proceed from 4000 to 4799 completed. Total 42.50s
            Thread 2:  processing 96%, working on 769/800, used 42.79s, eta 1.73s
        Thread 6:  proceed from 4800 to 5599 completed. Total 43.00s
        Thread 2:  proceed from 1600 to 2399 completed. Total 43.51s
            Thread 4:  processing 96%, working on 769/800, used 43.54s, eta 1.76s
            Thread 3:  processing 96%, working on 769/800, used 43.60s, eta 1.76s
        Thread 4:  proceed from 3200 to 3999 completed. Total 43.98s
        Thread 3:  proceed from 2400 to 3199 completed. Total 44.06s
        Kpd assembling completed (Parallel). Total 45.23s
Solving Linear System: DOF=13122.
Linear System Solved. Time cost= 4.69s
get_absolute_displace done.
get_strain_field done.
get_stress_field done.
get_strain_energy_density done.
get_distortion_energy_density done.
```
