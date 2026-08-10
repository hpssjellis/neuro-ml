# Cortical Labs API Installation & Simulation Steps

### Prerequisites
* Ensure you have **Python 3.12 or later** installed on your system.

---

### Complete Setup & Execution Instructions

To install the SDK, set up the environment, and run the local simulation all in one sequence, run the following commands in your terminal or command prompt:


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
