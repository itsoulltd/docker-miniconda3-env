## Project Documentation:
    Description: *

### What is _______________?
    Description: *

### Architecture of Synapse Pipeline:
    -> [Upload Using XYZ App] 
    -> [ADLStorage(../Bronze/.../Input-Data-Files.csv)] 
    -> [ETL: Stage_01(Cleaning,Transforming,LoadingInto(Silver))]
    -> [VM: Start with ADLStorage(../Silver/.../stage_01_fact_xyz.csv)]
       Stage-02: ....
       Stage-03: ....
    -> [VM: Stop]
    -> [ETL: Read from Silver and Transform into Gold]
    -> [Execute SQL-View Scripts]
    -> [Reporting: Create workspace in powerbi-app with Semantic-Model(Star-Schema) & Report.

### Code infrastructure:
    Description: *

### What is Docker?
    Description: docker and it's basic *

### Why Docker?
    Description: *

### What is Anaconda(aka Conda) for python?
    Description: *

### How to start docker:
    ~>$ open -a Docker
    ~>$ docker-compose up -d

### Open any browser and paste:
    http://localhost:8888

### How to add python SDK in IntelliJ Project:
#### [Click To Follow jetbrains.com/tutorial](https://www.jetbrains.com/help/idea/configuring-python-sdk.html#4817ac47)
#### [Main function in Python](https://realpython.com/python-main-function/)