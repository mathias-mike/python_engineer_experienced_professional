import os
import sys
import json
import datatypes as dt

def process_file(file):
    """ Function reads content of a json file and converts it to python dictionary.

    Args:
        file (str): The full path of json file to read.

    Returns:
        data (dict): Python dictionary of content of json file.
    """
    # Confirm file passed is a json file
    if file[-5:] != ".json":
        # Not raising an exception here incase you want to batch process a ton of json files
        # raise Exception("Please check: {}\nProgram only processes 'JSON' files!".format(file))
        print("\nProgram only processes 'JSON' files! Please check: {}".format(file))
        return

    with open(file, "r") as f:
        data = f.read()
    
    try:
        data = json.loads(data)
    except Exception as e:
        print("\nError parsing file:: {}".format(e))
        return

    return data



def get_type(value):
    """ Function gets the defined json data type of a given variable. Data types are from the datatypes file.

    Args:
        value: The variable to detect its data type.

    Returns:
        dtype (str): Data type of the given variable in string.
    """
    dtype = None

    if isinstance(value, dict):
        dtype = dt.obj
    elif isinstance(value, bool):
        dtype = dt.bool
    elif isinstance(value, int) or isinstance(value, float):
        dtype = dt.int
    elif isinstance(value, str):
        dtype = dt.str
    elif isinstance(value, list):
        if len(value) == 0:
            dtype = dt.arr
        elif isinstance(value[0], str):
            dtype = dt.enum
        else:
            dtype = dt.arr

    return dtype



def save_schema(root, schema_name, schema):
    """ Function saves detected json schema in the root/schema_name.json file

    Args:
        root (str): Root path for directory to save the schema in
        schema_name (str): Name for file to save the schema in. A ".json" would be appended to this.
        schema (dict): Dictionary object defining the schema of the json file.
    """

    # Defining the output file for the detected schema. Using os.path to append the schema_name to root because different
    # os has different ways of referencing directories (window uses the backslash "\" while linux uses the forward slash "/")
    schema_name = schema_name + ".json"
    output_file = os.path.join(root, schema_name)

    # Ensuring that root path exist and if not, we create the path including all it's parent.
    if not os.path.exists(root):
        os.makedirs(root)

    # Finally dumping detected schema
    with open(output_file, "w") as f:
        f.write(json.dumps(schema, indent=4))



def generate_schema(root, schema_name, data):
    """ Function generates schema for attributes of the given json object (data.

    Args:
        root (str): Root path for directory to save the schema in.
        schema_name (str): Name for file to save the schema in. A ".json" would be appended to this.
        data (dict): Python dictionary to parse and generate schema for its attributes.
    """

    schema = {}
    for key, value in data.items():
        schema[key] = {}

        dtype = get_type(value)
        if dtype == dt.obj:
            new_root = os.path.join(root, key)
            generate_schema(new_root, key, value)

        schema[key]["type"] = dtype
        schema[key]["tag"] = ""
        schema[key]["description"] = ""
        schema[key]["required"] = False

    save_schema(root, schema_name, schema)


def run(file):
    """ Sniff json schema of json file.

    Args:
        file (str): Relative or full path of json file.
    """
    data = process_file(file)

    if data is not None:
        # Creatin the directory for the schema
        filename = os.path.basename(file)[:-5]
        root = os.path.join("schema", filename)

        data = data.get("message", {})
        generate_schema(root, filename, data)

        print("{} processed and schema saved at {}".format(file, root))
    else:
        print("-----------------------{} skiped------------------------------\n".format(file))


def main():
    # Make sure file is passed in as arguement 
    if len(sys.argv) < 2:
        raise Exception("Not enough arguement for the task!")

    json_file = sys.argv[1]

    run(json_file)


if __name__ == "__main__":
    main()