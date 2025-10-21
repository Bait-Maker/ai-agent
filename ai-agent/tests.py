from functions import get_files_info, get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
# Test file for functions.py

def test():
    # ** get_file_info tests
    # print("Result for current directory:")
    # print(get_files_info("calculator", "."))


    # print("Result for 'pkg' directory:")
    # print(get_files_info("calculator", "pkg"))


    # print("Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"))


    # print("Result for '../' directory:")
    # print(get_files_info("calculator", "../"))

    # ** Lorem ipsum test for MAX_CHARS limit
    # print(get_file_content("calculator", "lorem.txt"))

    # ** get_file_content tests
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))

    # ** write_file tests
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem upsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum folor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))
    


if __name__ == "__main__":
    test()