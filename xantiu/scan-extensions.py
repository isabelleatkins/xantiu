import os
import click
import pandas as pd

@click.command()
@click.argument("path", type=click.Path(exists=True))
def scan_extensions(path):
    '''
    Scans a directory and returns the number of files, the largest file, and the total size of all files for each file extension. \n
    PATH is the path to the directory to scan. eg /home/user/Documents.
    '''
    file_extension_stats = {}
    #Traverse the directory top-down. This visits all files in the directory and its subdirectories.
    for root, _, filenames in os.walk(path):
        for file in filenames:
            #Split the file into its name and extension eg "file.txt" becomes "file" and ".txt"
            _, file_extension = os.path.splitext(file)
            #Obtain the size of the file
            file_size = os.path.getsize(os.path.join(root, file))
            #If the file extension is already in the dictionary, update the stats for that file extension. Otherwise, add the file extension to the dictionary.
            if file_extension_stats.get(file_extension) != None:
                file_extension_stats[file_extension][0] += 1
                if file_size > file_extension_stats[file_extension][1]:
                    file_extension_stats[file_extension][1] = file_size
                file_extension_stats[file_extension][2] += file_size
            else:
                file_extension_stats[file_extension] = [1, file_size, file_size]

    #Convert the dictionary to a pandas DataFrame and print it to the console.
    df = pd.DataFrame(file_extension_stats)
    print(df.transpose())