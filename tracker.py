excersizes = {"monday": {}, "tuesday": {}, "wednesday":{},
              "thursday":{}, "friday":{}, "saturday":{},
              "sunday":{}}

DAY_ABBREVIATIONS = {
    "mon": "monday", "tue": "tuesday", "wed": "wednesday",
    "thur": "thursday", "fri": "friday", "sat": "saturday", "sun": "sunday"
}
def user_input() -> str:
    opening = input()
    if opening.lower() == "l":
        log_weight()
    elif opening.lower() == "c":
        change_weight()
    elif opening.lower() == "q":
        print("Have a good day")
        return 0
    else:
        print("Please input a valid choice (l, c, q) try again: ")
        user_input()

def log_weight():
    logging_day = input("Choose the day you want to log to\nmon, tue, wed\nthur, fri, sat, sun: \nTo return home type (home)\n:").lower()

    if logging_day == "home":
        user_input()
        return

    if logging_day not in DAY_ABBREVIATIONS:
        print("Please input a valid choice (mon, tue, wed, thur, fri, sat, sun, home) try again: ")
        log_weight()
        return

    day = DAY_ABBREVIATIONS[logging_day]

    if len(excersizes[day]) < 1:
        second_log = input(f"\n\nNo workouts on {day}\nMust add an excersize/workout split: \ntype (Add) for adding excersize or (back) to return home\n:").lower()
        if second_log == "add":
            add_excersize(day)
        elif second_log == "back":
            user_input()
        else:
            raise ValueError("Wrong input must type the following:\nadd\nback")
    else:
        # TODO: day already has exercises logged — need to log a weight to one of them
        pass



def add_excersize(day):
    while True:
        name = input("Enter the excersize name: ").strip()

        is_dupe = name in excersizes[day]
        if is_dupe:
            confirm = input(f"'{name}' is already in {day}'s split. Update its current weight? (y/n): ").lower()
            if confirm != "y":
                continue

        while True:
            prompt_label = "current" if is_dupe else "starting"
            weight_input = input(f"Enter the {prompt_label} weight for {name}: ")
            try:
                weight = float(weight_input)
                break
            except ValueError:
                print("That's not a valid number, try again.")

        if is_dupe:
            excersizes[day][name]["current"] = weight
        else:
            excersizes[day][name] = {"initial": weight, "current": weight}

        again = input("Add another excersize? (y/n): ").lower()
        if again != "y":
            break
def change_weight():
    pass
