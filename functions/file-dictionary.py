import os  # Import the os module for operating system related functionalities

def get_dir_dict(dir_path=''):  # Define a function to get details of files within a directory
    dir_dict = {}  # Initialize an empty dictionary to store directory information

    if dir_path == '':  # Check if the directory path is not provided
        dir_path = input('Provide a directory\'s path to get details of the files within (leave blank to use working directory): ')  # Prompt the user to input a directory path
        if dir_path == '':  # If the user leaves the input blank
            dir_path = os.getcwd()  # Get the current working directory

    files = os.listdir(dir_path)  # List all files and directories in the specified directory

    for file in files:  # Iterate through each file and directory in the directory
        file_path = os.path.join(dir_path, file)  # Create the absolute path for the file or directory
        if os.path.isfile(file_path):  # Check if it is a file
            file_details = {  # If it is a file, create a dictionary to store its details
                'path': file_path,  # Store the file path
                'file_size': os.path.getsize(file_path),  # Store the file size
            }
            dir_dict[file] = file_details  # Add the file details to the directory dictionary
        elif os.path.isdir(file_path):  # Check if it is a directory
            subdir_dict = get_dir_dict(file_path)  # If it is a directory, recursively call the function to get its details
            dir_dict[file] = subdir_dict  # Add the directory details to the directory dictionary
        else:  # If it is neither a file nor a directory
            print('No files here')  # Print a message indicating that there are no files in this location

    return dir_dict  # Return the directory dictionary containing file and subdirectory details

# ===== The print funtion is here to make the dictionary easily readable, e.g. it's passed the dictionary created by get_dir_dict =====
def print_dir_dict(dir_dict, indent=0): # Define a function to print directory details
    for key, value in dir_dict.items(): # Iterate through each key-value pair in the directory dictionary
        if isinstance(value, dict): # If the value is a dictionary (subdirectory)
            print(' ' * indent + f'{key}/') # Print the subdirectory name with appropriate indentation
            print_dir_dict(value, indent + 1) # Recursively call the function to print the subdirectory contents
        else: # If value is a file
            print(' ' * indent + f'{key}: {value}') # Print the file name and its details with appropriate indentation



dir_dict = (get_dir_dict(''))  # Call the function to get details of files within the specified directory
print_dir_dict(dir_dict) # Print the resulting dictionary in an easily readable format