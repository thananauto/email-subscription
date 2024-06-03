
import csv, os
from dotenv import dotenv_values

def conf():
    #loaded env files
    props = {
         # load env variables
        **dotenv_values('.env') # Load environment variables
    }

    return props


def get_file_data():
    output =[]
    file_name = conf()['input_filename']
    with open(f'files/{file_name}', mode ='r')as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            output.append(row[0])
    return output

def writing_file(output: object, filename: str):
    #deletet the old file
    if os.path.exists(filename):
        os.remove(filename)
    
    # create the new file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output)

