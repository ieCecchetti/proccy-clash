import os
import sys
import json

from const.visualizer import HELPER, COMMAND_EXAMPLE
from handlers.processes import format_processes
from services.files import zip_file
from services.general import args_extractor, helper_check
from services.mail import send_mail


def extract_procs(filename):
    """ get the processes file json and parse it """
    data = json.load(open(f"res/in/{filename}.json", 'r'))
    return data


def write_procs(filename, data):
    """ get the processes file json and parse it """
    # print in tree structure the json
    json_array = list(data.values())
    with open(f"res/out/{filename}_result.json", "w") as f:
        json.dump(json_array, f, indent=4)


def print_table(filename, data):
    with open(f'res/visualizer_template.html', 'r') as f:
        # Read the content of the template file
        html_content = f.read()
        # Replace table with the new one
        html_content = html_content.replace('<here_the_table>', format_processes(data))
    with open(f"res/out/{filename}_result.html", 'w') as f:
        # Scrivi il contenuto modificato nel nuovo file HTML
        f.write(html_content)


if __name__ == '__main__':
    args = args_extractor(sys.argv)
    helper_check(args, HELPER)

    # get the filename. its mandatory
    if len(sys.argv) > 1:
        file_name = str(sys.argv[1])
    else:
        print(f"Impossible to extract file. No input filename found. {COMMAND_EXAMPLE}")
        sys.exit()
    data = extract_procs(file_name)
    layered_data = {p['pid']: p for p in data}

    for p_key in reversed(list(layered_data.keys())):
        p_value = layered_data[p_key]
        # if exist the father in the unlayered
        if p_value['ppid'] in layered_data.keys():
            if 'children' not in layered_data[p_value['ppid']].keys():
                layered_data[p_value['ppid']]['children'] = []
            layered_data[p_value['ppid']]['children'].append(p_value)
        else:
            print(f"Root process at {p_value['ppid']}")
            continue
        del layered_data[p_key]

    write_procs(file_name, layered_data)

    # view part
    if "--json" in args:
        print(json.dumps(data, indent=4))
    elif "--table" in args:
        print_table(file_name, data)
    # store part
    if "--no-store" in args:
        print(f"Cleaning the created file (--no-store required)")
        file_path = f'res/out/{file_name}_result.json'
        abs_file_path = os.path.abspath(file_path)
        os.remove(abs_file_path)
    elif "--mail" in args:
        file_path = f'res/out/{file_name}_result.json'
        zip_path = f'res/out/{file_name}_result.zip'
        message = "here is the process list. Have fun with it.... ?"
        m_from = input(f"Please add your mail address: ")
        m_to = input(f"Please add the address designed to receive the mail: ")
        psw = None
        if "--mail-protected" in args:
            psw = input("Enter the psw to decript the file: ")
        file = zip_file([file_path], zip_path, password=psw)
        send_mail(m_from, m_to, "process list result", message, zip_url=zip_path)
    else:
        print(f"Extracted file stored in the directory: res/out/{file_name}_result.json")

    print("Finished")
