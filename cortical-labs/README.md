# Cortical Labs API Installation & Simulation Steps

### Prerequisites
* Ensure you have **Python 3.12 or later** installed on your system.

---

### Complete Setup & Execution Instructions for windows, slightly different in places for max or linux

To install the SDK, set up the environment, and run the local simulation all in one sequence, run the following commands in your terminal or command prompt:


open a DOS terminal or powershell terminal (If one does not work try the other)

check which folder you are in and perhaps use the windows to find a better starting point such as make a new folder called cortical-labs in documents and open the terminal there.


Check if python is working and installed, if not install it.
```bash
python3 -V
pip3 -V
```

For me python3 did not work but python -V worked, so I adapted the commands


```bash
python3 -m venv .venv
```



```bash
source .venv/bin/activate
```



```bash
pip3 install cl-sdk jupyterlab
```


```bash
git clone [https://github.com/Cortical-Labs/cl-api-doc.git](https://github.com/Cortical-Labs/cl-api-doc.git)
cd cl-api-doc
```




```bash
jupyter lab

```

A webpage of a jupyter lab should pop up.

## After a full reboot to restart

Get to the same folder


```bash
source .venv/bin/activate
cd cl-api-doc
jupyter lab
```

You could probably put those into a bash file called "start-cl1.bat"

```bash
@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
cd cl-api-doc
jupyter lab
pause

```












<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>


To delete everything you installed 
```bash
rmdir /s /q .venv
rmdir /s /q cl-api-doc
```

Or just remember the folder you started in and find .venv  which may be a hidden file

