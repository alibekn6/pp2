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
    
    print("\n1. List directories, files, and all items:")
    list_directories_files(path)
    
    print("\n2. Check access to the path:")
    check_path_access(path)
    
    print("\n3. Check if the path exists and split into directory and filename:")
    check_path_and_split(path)
    
    print("\n4. Count lines in a text file:")
    file_path = input("Enter the file path: ")
    count_lines_in_file(file_path)
    
    print("\n5. Write a list to a file:")
    my_list = ['apple', 'banana', 'cherry']
    write_list_to_file('output.txt', my_list)
    
    print("\n6. Generate 26 text files (A.txt to Z.txt):")
    generate_alphabet_files()
    
    print("\n7. Copy contents of a file to another file:")
    source = input("Enter source file path: ")
    destination = input("Enter destination file path: ")
    copy_file(source, destination)
    
    print("\n8. Delete a file by specified path:")
    file_to_delete = input("Enter the file path to delete: ")
    delete_file(file_to_delete)

# Run the program
if __name__ == "__main__":
    main()