import os

def check_and_rename_file(folder_path):
    # Traverse all subfolders and files in the folder
    for root_directory, directories, file_name_list in os.walk(folder_path):
        for file_name in file_name_list:
            # Get the full path of the file
            full_path = os.path.join(root_directory, file_name)
            
            try:
                # Read the file content
                with open(full_path, 'r', encoding='latin-1') as file:
                    content = file.read()
                
                # Determine the new file suffix based on the file content
                if '/Script/Engine' in content:
                    new_suffix = '.uasset'
                elif 'LuaS' in content:
                    new_suffix = '.lua'
                elif 'BKHD' in content:
                    new_suffix = '.bnk'
                elif 'if ... then' in content:
                    new_suffix = '.lua'
                elif 'function' in content:
                    new_suffix = '.lua'
                else:
                    new_suffix = '.uexp'
                
                # Split filename and current suffix
                basename, extension = os.path.splitext(file_name)
                new_name = basename + new_suffix
                new_full_path = os.path.join(root_directory, new_name)
                
                # If new name is different from current name, rename file and print modified file
                if new_full_path != full_path:
                    os.rename(full_path, new_full_path)
                    print(f"SET_FILE UNPACK {new_name}")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

# Get folder path entered by user
input_path = "/storage/emulated/0/Download/output_folder"
check_and_rename_file(input_path)
