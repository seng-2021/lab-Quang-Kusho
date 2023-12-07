from datetime import datetime as dt
import menu_function as mf

# take input from user
def read_int(s):
    try:
        return int(s)
    except ValueError:
        return 0

# create a menu
def menu():
    print("What do you want to do:\n" +
          "1) Identify the components of a time object\n"+
          "2) Calculate age in days\n"+
          "3) Print the days of the week\n"+
          "4) Print the months\n"+
          "0) Stop")
    choice = read_int(input("Your choice:\n"))
    return choice

def main():
    print("This program uses the datatime library to deal with time.")
    choice = 1
    while choice != 0:
        choice = menu()
        if choice == 1:
            mf.get_time()
        elif choice == 2:
            mf.cal_age()
        elif choice == 3:
            mf.get_weekday()
        elif choice == 4:
            mf.get_month()


if __name__ == "__main__":
    main()