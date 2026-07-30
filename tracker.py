excersizes = {"monday": {}, "tuesday": {}, "wednesday":{},
              "thursday":{}, "friday":{}, "saturday":{},
              "sunday":{}}
def log_weight():
    logging_day = input("Choose the day you want to log to\nmon, tue, wed\nthur, fri, sat, sun: ").lower()
def change_weight():
    something = 1
def user_input() -> str:
    opening = input()
    while True:
        if opening.lower() == "l":
            log_weight()
        elif opening.lower() == "c":
            change_weight()
        elif opening.lower() == "q":
            print("Have a good day")
            break 
        else:
            print("Please input a valid choice (l, c, q) try again: ")
            user_input()

