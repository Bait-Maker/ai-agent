import os
from google.genai import types


# ** Treat the directory as a relative path inside working_directory
def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    # Build string representing contents of the directory
    file_string = ""
    try:
        for content in os.listdir(target_dir):
            child_path = os.path.join(target_dir, content)
            file_string = f"{file_string}- {content}: file_size={os.path.getsize(child_path)} bytes, is_dir={os.path.isdir(child_path)}\n"
    except Exception as e:
        return f"Error: {e}"

    return file_string


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
