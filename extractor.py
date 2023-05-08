import sys
import json
import psutil
import hashlib
import datetime


def extract_procs():
    """Get list of running process"""
    proc_list = []
    # Iterate over the list
    print("Exctracting processses from you local machine")
    for proc in psutil.process_iter():
        try:
            # Fetch process details as dict
            pinfo = proc.as_dict(attrs=['pid', 'ppid', 'memory_percent', 'name', 'cpu_times',
                                        'create_time', 'memory_info'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            # Append dict to list
            proc_list.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error trying to extract current processes. Caused by: {repr(e)}")
            return None
    # Sort list of dict by key vms i.e. memory usage
    proc_list = sorted(proc_list, key=lambda proc_obj: proc_obj['pid'])
    return proc_list


def write_procs(proc_list, filename=None):
    """ get the processes file json and parse it """
    # print in tree structure the json
    if not filename:
        now = datetime.datetime.now()
        date = now.strftime('%Y%m%d%H%M%S%f')
        sha256 = hashlib.sha256(date.encode()).hexdigest()
        filename = f"p_temp_{sha256[:6]}"
    try:
        with open(f"res/in/{filename}.json", "w") as f:
            json.dump(proc_list, f)
    except FileNotFoundError:
        print("Impossible store the the list of processes. Cause by: File path not found")
    except Exception as e:
        print(f"Unknown error while storing the the list of processes. Cause by: {repr(e)}")
    print(f"Stored into file at: res/in/{filename}.json")

if __name__ == '__main__':
    file_name = None
    if len(sys.argv) == 2:
        # filename specified case
        file_name = str(sys.argv[1])
    processes = extract_procs()
    if processes:
        write_procs(processes, filename=file_name)
    else:
        print("No process found. Maybe an error occured?")

    print("Finished")
