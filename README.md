# Python logging Example

## Directory
```
.
├── README.md
├── logging_config.py
├── main.py 
└── someloop.py
```
## How To
The ```logging``` module comes with python so no need for additional installation.

### Steps

1. Create virtual environment for Python3 and activate it.  
2. Execute `main.py`.
3. Check the created `testlog.log` file and get used to the flow. 

## Explanations

- `logging_config.py`  
This sets the basic configuration for all loggers. You can customize the format of the log text and choose whether you would like to log it in a seperate file. In this example it will search for a file named `testlog.log` and log it there. The file will be created if not detected. 
- `main.py`  
This is the main script that will be executed. It has it's own logger object and calls the `foo` function from `someloop.py`.
- `someloop.py`  
This is a script that contains a looping function that will break on the second iteration. It also has it's own logger object. 
