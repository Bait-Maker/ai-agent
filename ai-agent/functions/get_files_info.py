import os

# ** Treat the directory as a relative path inside working_directory
def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    # Build string representing contents of the directory
    file_string = ""
    try:
        for content in os.listdir(full_path):
            child_path = os.path.join(full_path, content)
            file_string = f"{file_string}- {content}: file_size={os.path.getsize(child_path)} bytes, is_dir={os.path.isdir(child_path)}\n"
    except Exception as e:
        return (f"Error: {e}")
    

    return (file_string)
