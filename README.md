# JSON schema sniffer
This program is designed to read the data of a json file, sniff the schema and dump the schema in another json file.

## Dependencies
To run the program, all you need is;
* Python (>=3.0)

## How to run
To run the program, you need the following in one folder;
* `datatypes.py`
* `main.py`
* `sniff_json_schema.py` 
* and a folder called `data` containing all your json files.

Once you have all this, open your terminal (cmd or powershell for windows) and navigate to the folder containing the above files

    cd /path/to/folder/

Next enter;

    python main.py

And the schemas of all json files in the data folder would be dumped into a new folder called `schema` in the same working directory. 


## Testing
To run the tests, you need to have `pytest` (>= 7.0.0) installed. You also need the `test_sniff_json_schema.py` in your folder.

With your terminal opened to your directory with all the necessary files, enter;

    pytest

and all unit tests would be run.