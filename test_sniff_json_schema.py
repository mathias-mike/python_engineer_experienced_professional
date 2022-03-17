from sniff_json_schema import process_file, get_type

# Can be tested with pytest

def test_exception_on_incorrect_file_name():
    assert(process_file("name/mike/filejson") == None)

def test_string_identification():
    assert(get_type("Mike") == "STRING")

def test_int_identification():
    assert(get_type(12) == "INTEGER")

def test_neg_int_identification():
    assert(get_type(-23) == "INTEGER")

def test_float_as_int_identification():
    assert(get_type(12.5) == "INTEGER")

def test_obj_identification():
    assert(get_type({"name": "Mike", "age": 25}) == "OBJECT")

def test_boolean_identification():
    assert(get_type(True) == "BOOLEAN")

def test_boolean_identification():
    assert(get_type(False) == "BOOLEAN")

def test_array_empt_identification():
    assert(get_type([]) == "ARRAY")

def test_array_identification():
    assert(get_type([12, 19, 42]) == "ARRAY")

def test_emum_identification():
    assert(get_type(["Mike", "George"]) == "ENUM")


