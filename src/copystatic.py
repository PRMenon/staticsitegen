import os
import shutil

def copy_files_recursive(source, destination):
    #cleanup
    if os.path.exists(destination):
        print(f"Deleting {destination} directory")
        shutil.rmtree(destination)
    os.mkdir(destination)
    #start copying
    items = os.listdir(source)
    for item in items:
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            print(f"Copying {source_path} to {destination_path}")
            shutil.copy(source_path, destination_path)
        else:
            copy_files_recursive(source_path, destination_path)
