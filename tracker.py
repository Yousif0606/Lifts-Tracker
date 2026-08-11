from datetime import date
from storage import save_data as _write_to_disk, load_data as _read_from_disk

excersizes = {"monday": {}, "tuesday": {}, "wednesday":{},
              "thursday":{}, "friday":{}, "saturday":{},
              "sunday":{}}

DAY_ABBREVIATIONS = {
    "mon": "monday", "tue": "tuesday", "wed": "wednesday",
    "thur": "thursday", "fri": "friday", "sat": "saturday", "sun": "sunday"
}

def save_data():
    _write_to_disk(excersizes)

def load_data():
    global excersizes
    loaded = _read_from_disk()
    if loaded is not None:
        excersizes = loaded

def today_str():
    return date.today().isoformat()

def prompt_for_number(prompt_text, cast=float):
    while True:
        raw = input(prompt_text)
        try:
            return cast(raw)
        except ValueError:
            print("That's not a valid number, try again.")

def prompt_for_value(prompt_text, previous_value, cast=float):
    while True:
        raw = input(f"{prompt_text} (current: {previous_value}, type 'same' to keep): ").lower()
        if raw == "same":
            return previous_value
        try:
            return cast(raw)
        except ValueError:
            print("That's not a valid number, try again.")

def calculate_progression(initial, current):
    if initial == 0:
        return None
    return ((current / initial) - 1) * 100
def user_input() -> str:
    while True:
        opening = input("l - log weight | c - change weight | q - quit\n: ").lower()
        if opening == "l":
            log_weight()
        elif opening == "c":
            change_weight()
        elif opening == "q":
            save_data()
            print("Have a good day")
            return 0
        else:
            print("Please input a valid choice (l, c, q) try again: ")

def select_day(action_verb):
    while True:
        chosen_day = input(f"Choose the day you want to {action_verb}\nmon, tue, wed\nthur, fri, sat, sun: \nTo return home type (home)\n:").lower()

        if chosen_day == "home":
            return None

        if chosen_day in DAY_ABBREVIATIONS:
            return DAY_ABBREVIATIONS[chosen_day]

        print("Please input a valid choice (mon, tue, wed, thur, fri, sat, sun, home) try again: ")

def log_weight():
    day = select_day("log to")
    if day is None:
        return

    if len(excersizes[day]) < 1:
        while True:
            second_log = input(f"\n\nNo workouts on {day}\nMust add an excersize/workout split: \ntype (Add) for adding excersize or (back) to return home\n:").lower()
            if second_log == "add":
                add_excersize(day)
                break
            elif second_log == "back":
                return
            else:
                print("Wrong input must type the following:\nadd\nback")
    else:
        print(f"\n{day.capitalize()}'s workout split:")
        for name, ex in excersizes[day].items():
            last = ex["logs"][-1]
            print(f"\n{name} (last: {last['weight']}kg x{last['reps']} reps x{last['sets']} sets)")
            weight = prompt_for_value("Weight (kg)", last["weight"], float)
            reps = prompt_for_value("Reps", last["reps"], int)
            sets = prompt_for_value("Sets", last["sets"], int)

            ex["logs"].append({"date": today_str(), "weight": weight, "reps": reps, "sets": sets})

            initial_weight = ex["logs"][0]["weight"]
            progression = calculate_progression(initial_weight, weight)
            if progression is None:
                print(f"{name}: {weight}kg x{reps}x{sets} (no % - starting weight was 0)")
            else:
                print(f"{name}: {weight}kg x{reps}x{sets} ({progression:+.1f}% from initial)")
            save_data()



def add_excersize(day):
    while True:
        name = input("Enter the excersize name: ").strip()

        is_dupe = name in excersizes[day]
        if is_dupe:
            confirm = input(f"'{name}' is already in {day}'s split. Log a new entry for it? (y/n): ").lower()
            if confirm != "y":
                continue
            last = excersizes[day][name]["logs"][-1]
            weight = prompt_for_value("Weight (kg)", last["weight"], float)
            reps = prompt_for_value("Reps", last["reps"], int)
            sets = prompt_for_value("Sets", last["sets"], int)
            excersizes[day][name]["logs"].append({"date": today_str(), "weight": weight, "reps": reps, "sets": sets})
        else:
            weight = prompt_for_number("Enter the starting weight (kg): ", float)
            reps = prompt_for_number("Enter the reps: ", int)
            sets = prompt_for_number("Enter the sets: ", int)
            excersizes[day][name] = {"logs": [{"date": today_str(), "weight": weight, "reps": reps, "sets": sets}]}

        save_data()

        again = input("Add another excersize? (y/n): ").lower()
        if again != "y":
            break
def change_weight():
    day = select_day("change")
    if day is None:
        return

    if len(excersizes[day]) < 1:
        print(f"\nNo excersizes on {day} to change.")
        return

    print(f"\n{day.capitalize()}'s workout split:")
    for name, ex in excersizes[day].items():
        last = ex["logs"][-1]
        print(f"- {name} (last: {last['weight']}kg x{last['reps']} reps x{last['sets']} sets)")

    while True:
        target = input("\nWhich excersize do you want to change? ").strip()
        if target in excersizes[day]:
            break
        print("That excersize isn't in this split, try again.")

    while True:
        action = input(f"Replace or delete '{target}'? (replace/delete): ").lower()
        if action in ("replace", "delete"):
            break
        print("Please type 'replace' or 'delete'.")

    if action == "delete":
        confirm = input(f"Are you sure you want to delete '{target}' from {day}? (y/n): ").lower()
        if confirm == "y":
            del excersizes[day][target]
            save_data()
            print(f"'{target}' deleted from {day}.")
        else:
            print("Cancelled.")
    else:
        new_name = input("Enter the new excersize name: ").strip()
        weight = prompt_for_number("Enter the starting weight (kg): ", float)
        reps = prompt_for_number("Enter the reps: ", int)
        sets = prompt_for_number("Enter the sets: ", int)

        del excersizes[day][target]
        excersizes[day][new_name] = {"logs": [{"date": today_str(), "weight": weight, "reps": reps, "sets": sets}]}
        save_data()
        print(f"'{target}' replaced with '{new_name}'.")

if __name__ == "__main__":
    load_data()
    user_input()
