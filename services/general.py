import sys


def args_extractor(argv):
    """ Return a list of args extracted from the system.argv"""
    # at first get all the --args
    fnc_extra = []
    for i, arg in enumerate(argv):
        if "--" in arg:
            fnc_extra.append(arg)
            del argv[i]
    # print(f"Found {len(fnc_extra)} args to apply to the function {fnc_extra}")
    return fnc_extra


def print_helper(data_dict, value_title=None):
    for key, item in data_dict.items():
        if not value_title:
            print(f"{key} - {item}")
        else:
            print(f"{key} - {item[value_title]}")


def helper_check(args, helper, title, code_example):
    if "--help" in args:
        print(title)
        print(code_example)
    elif not all(val in helper.keys() for val in args):
        print(f"Commands not existing check the syntax and restart: {args}")
    print_helper(helper)
    sys.exit()

