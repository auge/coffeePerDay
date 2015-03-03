coffeePerDay
============

Parsing and analyzing collected data files from the measurement campaign of http://www.monergy-project.eu/

Usage
=====

Integration
-----------

A set of scripts is provided to integrate the power consumption to obtain the total energy usage.

run this script with:
```
./integrate.sh /path/to/dataset/directory/ [integrate.py|integrateFile.py]
```

- integrate.py will analyze a single column
- integrateFile.py will analyze the whole file

Coffees per Day
---------------

Put your *.csv files in this directory and run ./coffeePerDay.sh

Alternatively, you may call 
```
find path/to/csv-files -type f -name "*.csv" | while IFS= read -r; do echo $REPLY `./analyze.py "$@" < $REPLY`; done
```

Options given to coffeePerDay.sh will be passed to analyze.py

You may run ./analyze.py -h to see all options:
```
usage: analyze.py [-h] [-v] [-f FILENAME] [-s SEPARATOR] [-c DATACOL] [-t PTIME]
                  [-p PLIMIT]

Scan through STDIN for periods where more than given amount of power has been
consumed.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Print debug info.
  -f FILENAME, --file FILENAME
                        Path to file to read. Defaults to STDIN.
  -s SEPARATOR, --separator SEPARATOR
                        Specify the separation character. Defaults to comma (,).
  -c DATACOL, --column DATACOL
                        Specify the column of the input data that contains the
                        data. Defaults to column 8.
  -t PTIME, --time PTIME
                        Specify the time limit for counter in seconds. Defaults to
                        20 seconds.
  -p PLIMIT, --power PLIMIT
                        Specify the power limit for the counter to be triggered.
                        Defaults to 500 W.
```
