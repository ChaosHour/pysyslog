# pysyslog



## Description
This was created to help parsing the syslog. Yes, there are some really good shell one-liners out there, but I wanted to be able to use this in a more programmatic way.

## Usage

```python
python3 pysyslog.py -f /path/to/your/file -d 2022-01-01 -s error
python3 pysyslog.py -f /path/to/your/file -s error
python3 pysyslog.py -f /path/to/your/file -d $(date -d "2 days ago" +%Y-%m-%d) -s error
python3 pysyslog.py -f /path/to/your/file -d 2022-01-01 -s error -l 10
```

# requirements for pysyslog.py
- python3



# requirements for pysyslog2.py
- python3
- termcolor

pip install -r requirements.txt

