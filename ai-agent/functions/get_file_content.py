import os
from configparser import ConfigParser

def get_file_content(working_directory, file_path):
    config = ConfigParser()
    config.read("file_config.ini")

    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not target_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_config = config["FILE"]
    max_chars = int(file_config["MAX_CHARS"])

    try:
        with open(target_path, "r") as file:
            file_contenent_string = file.read(max_chars)
            if os.path.getsize(target_path) > max_chars:
                file_contenent_string += (
                    f'[...File "{file_path}" truncated at {max_chars} characters]'
                )
        return file_contenent_string
    except Exception as e:
        return (f'Error reading file: "{file_path}": {e}')