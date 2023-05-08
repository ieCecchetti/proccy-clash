from const import MENU
from services.general import print_helper


def print_banner():
    with open(f"res/banner.txt", 'r') as file:
        banner = file.read()
        # update version num
        banner = banner.replace("<version_num>", "1.0.0")
        print(banner)


if __name__ == '__main__':
    print_banner()
    choice = None
    while choice != 'C':
        print(f"Welcome in proccy-clash menu. Please select the operation you want to perform: ")
        print_helper(MENU)
        ans = input("Please select what you want to do: ")
    print("Finished")


