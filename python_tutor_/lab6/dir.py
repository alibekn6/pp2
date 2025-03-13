import os
import shutil


def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)
    
    print("\nAll items (directories and files):")
    for item in os.listdir(path):
        print(item)


def check_path_access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")


def check_path_and_split(path):
    if os.path.exists(path):
        print(f"The path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("The path does not exist.")

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")

def write_list_to_file(file_path, my_list):
    with open(file_path, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")
    print(f"List written to {file_path}")

def generate_alphabet_files():
    for letter in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(letter)}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {chr(letter)}.txt")
    print("26 files generated from A.txt to Z.txt")


def copy_file(source, destination):
    shutil.copyfile(source, destination)
    print(f"Contents of {source} copied to {destination}")

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"{file_path} deleted.")
        else:
            print(f"No write access to {file_path}.")
    else:
        print(f"{file_path} does not exist.")


def main():
    path = input("Enter a path: ")
    
    # Task 1
    print("\n1. Listing directories and files:")
    list_directories_files(path)
    
    # Task 2
    print("\n2. Checking path access:")
    check_path_access(path)
    
    # Task 3
    print("\n3. Checking path and splitting:")
    check_path_and_split(path)
    
    # Task 4
    file_path = input("\n4. Enter file path to count lines: ")
    count_lines_in_file(file_path)
    
    # Task 5
    my_list = ['apple', 'banana', 'cherry']
    write_list_to_file('output.txt', my_list)
    print("\n5. List written to 'output.txt'")
    
    # Task 6
    generate_alphabet_files()
    print("\n6. Generated 26 files A.txt to Z.txt")
    
    # Task 7
    source = input("\n7. Enter source file to copy: ")
    destination = input("Enter destination file: ")
    copy_file(source, destination)
    
    # Task 8
    file_to_delete = input("\n8. Enter file path to delete: ")
    delete_file(file_to_delete)

main()