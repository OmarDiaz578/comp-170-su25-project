from Friend import Person
from Birthday import Birthday
#3from datetime import date

BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
# Used these string to wrap console outpit in color or bold, then reset them back to normal
friends_file = "/workspaces/comp-170-su25-project/friends_database.csv"
# Use this to load and save to when the user exits the program
filename = friends_file 
def load_friends(filename):
    filename = friends_file 
    friends = []
    # creates an empty list to collect Person objects as they are read from the CSV 
    try:
        f = open(filename, encoding='utf-8')
        lines = f.read().splitlines()
        # opens the CSV file in text mode using UTF-8 encoding
    except FileNotFoundError:
        return friends
    for row in lines[1:]:
    # loops thorugh every line except the first one(header)
        cols = [c.strip() for c in row.split(',')]
        # results is a list of column strings
        if not cols or not cols[0]:
        # skips row if empty
            continue
        p = Person(cols[0], cols[1] if len(cols) > 1 else "")
        # create a new Person, passing teh first column as first name and the second as last name, or "" if missing
        if len(cols) > 3 and cols[2].isdigit() and cols[3].isdigit():
            p.set_birthday(int(cols[2]), int(cols[3]))
            # if there are at least 4 columns and columns 2 and 3 are numeric
            # converts them to integers and sets this person's birthday
        field_names = ('email_address','nickname','street_address', 'city','state','zip','phone')
        for i, attr in enumerate(field_names, start=4):
            if len(cols) > 1 and cols[i]:
                getattr(p, f"set_{attr}")(cols[i])
        # adds other data 
        friends.append(p)
        # add full date of Person object to friends list
    return friends
    

#friends_file = "/workspaces/comp-170-su25-project/friends_database.csv"
#filename = friends_file 
def save_friends(filename, friends):
    filename = friends_file  
    header = ['first_name', 'last_name','birth_month','birth_day','email_address','nickname','street_address','city','state','zip','phone']
    f = open(filename, 'w', encoding='utf-8')
    f.write(','.join(header) + '\n')
    for p in friends:
        bm = ''
        bd= ''
        if p is not None:
            bm = str(p.birthday.get_month())
            bd = str(p.get_date())
        row = [p.get_first_name(), p.get_last_name(), bm, bd,
               getattr(p, 'email_address', ''), getattr(p, 'nickname', ''),
               getattr(p, 'street_address', ''), getattr(p, 'city', ''),
               getattr(p, 'state', ''), getattr(p, 'zip', ''), getattr(p, 'phone', '')]
        f.write(','.join(row) + '\n')
    

def prompt_int(prompt, low, high):
    while True:
    # starts an infinite loop until teh user enters a valid input
        try:
            n = int(input(f"{prompt} ").strip())
            if low <= n <= high:
                return n
        except ValueError:
            pass
        print(f"Please enter a number between {low} and {high}.")
        # if value inputted is'nt within the valid range it prints this until a valid integer is returned
    

def create_friend():
    # this function asks you for info on your new friend and if you would liek to add anything else
    # returns a new Person
    print(GREEN + 'Enter new friend details:' + RESET)
    first = input('First name: ').strip()
    last = input('Last name: ').strip()
    friend = Person(first, last)
    if input('Add birthday? (y/N): ').lower().startswith('y'):
        m = prompt_int('Month (1-12):', 1, 12)
        d = prompt_int('Day:', 1, Birthday.days_in_month[m-1])
        friend.set_birthday(m, d)
    if input('Add email? (y/N): ').lower().startswith('y'):
        friend.set_email_address(input('Email: ').strip())
    if input('Add nickname? (y/N): ').lower().startswith('y'):
        friend.set_nickname(input('Nickname: ').strip())
    if input('Add street? (y/N): ').lower().startswith('y'):
        friend.set_street_address(input('Street: ').strip())
    if input('Add city? (y/N): ').lower().startswith('y'):
        friend.set_city(input('City: ').strip())
    if input('Add stete? (y/N): ').lower().startswith('y'):
        friend.set_state(input('State: ').strip())
    if input('Add zip? (y/N): ').lower().startswith('y'):
        friend.set_zip(input('Zip: ').strip())
    if input('Add phone number? (y/N): ').lower().startswith('y'):
        friend.set_phone(input('Phone #: ').strip())
    
    return friend 

def search_friends(friends):
    key = input('Search name: ').lower().strip()
    matches = []
    # collects any Person who match the inserted key
    for p in friends:
        fn = p.get_first_name().lower()
        ln = p.get_last_name().lower()
        if fn.find(key) != -1 or ln.find(key) != -1:
            matches.append(p)
        # checks over each friend and if they match it is added to the matches list
    if len(matches) == 0:
        print('No matches found.')
        result = None
    else:
        print('Found ' + str(len(matches)) + ' match(es):')
        for i in range(len(matches)):
            p = matches[i]
            print(str(i+1) + '. ' + p.get_first_name() + ' ' + p.get_last_name())
            # assigns each match a number
        sel = prompt_int('Select desired number to edit or (0 to Exit):', 0, len(matches))
        # allows user to edit person or return
        if sel == 0:
            result = None
        else:
            result = matches[sel-1]
    return result

def edit_friend(p: Person):
    # modifies desired Person
    print(YELLOW + f"Editing {p.get_first_name()} {p.get_last_name()}" + RESET)
    if input("Change first name? (y/N): ").lower().startswith('y'):
        p.set_first_name(input("New first name: ").strip())
    if input("Change last name? (y/N): ").lower().startswith('y'):
        p.set_last_name(input("New last name: ").strip())
    if input("Change birthday? (y/N): ").lower().startswith('y'):
        m = prompt_int("Month (1-12):", 1, 12)
        d = prompt_int(f"Day (1-{Birthday.days_in_month[m-1]}):", 1, Birthday.days_in_month[m-1])
        p.set_birthday(m, d)
    if input("Change email? (y/N): ").lower().startswith('y'):
        p.set_email_address(input("New email: ").strip())
    if input("Change nickname? (y/N): ").lower().startswith('y'):
        p.set_last_name(input("New nickname: ").strip())
    if input("Change street? (y/N): ").lower().startswith('y'):
        p.set_street_address(input("New street: ").strip())
    if input("Change city? (y/N): ").lower().startswith('y'):
        p.set_city(input("New city: ").strip())
    if input("Change state? (y/N): ").lower().startswith('y'):
        p.set_state(input("New state: ").strip())
    if input("Change zip? (y/N): ").lower().startswith('y'):
        p.set_zip(input("New zip: ").strip())
    if input("Change phone number? (y/N): ").lower().startswith('y'):
        p.set_phone(input("New phone number: ").strip())

def delete_friend(friends: list[Person], p: Person):
    # deletes a friend with 2 confirmations so not done on accident
    if input(f"Are you sure you want to delete {p.get_first_name()} {p.get_last_name()}? (y/N): ").lower().startswith('y'):
        if input("This cannot be undone. Confirm deletion? (y/N): ").lower().startswith('y'):
            friends.remove(p)
            print(GREEN + "Deleted." + RESET)
        else:
            print("Deletion cancelled.")
    else:
        print("Deletion cancelled.")

def run_reports(friends: list[Person]):
    # calls the submenu
    # depending on option picked can do various things
    while True:
        print(BOLD + "=== Reports ===" + RESET)
        print("3.1 List friends alphabetically")
        print("3.2 List by upcoming birthdays")
        print("3.3 Mailing labels")
        print("3.9 Return to previous menu")
        choice = input("Select (3.x): ").strip()
        if choice == '3.1':
            for p in sorted(friends, key=lambda x: (x.get_last_name().lower(), x.get_first_name().lower())):
                print(f" - {p.get_first_name()} {p.get_last_name()}")
        elif choice == '3.2':
            print(YELLOW + "\nUpcoming birthdays:" + RESET)
            upcoming = []
            for p in friends:
                b = p.birthday
                if not b:
                    continue
                days_away = b.days_until()
                upcoming.append((days_away, p))
            if not upcoming:
                print("  No birthdays on record.")
            else:
                for days_away, p in sorted(upcoming, key=lambda x: x[0]):
                    print(f"  - {p} {p.get_last_name()}: in {days_away} day(s)")

        elif choice == '3.3':
            for p in friends:
                name = f"{p.get_first_name()} {p.get_last_name()}"
                street = getattr(p, 'street_address', '')
                city = getattr(p, 'city', '')
                state = getattr(p, 'state', '')
                zip = getattr(p, 'zip', '')
                print(name)
                print(street)
                print(f"{city}, {state} {zip}")
                print("---")
        elif choice == '3.9':
            return
        else: 
            print("Invalid selection. Please choose 3.1, 3.2, 3.3, or, 3.9.")
        input("\nPress Enter to continue...")
            


def main():
    # main directory
    friends = load_friends(friends_file)
    while True:
        print(BOLD + '=== Friend Management ===' + RESET)
        print("1 Create new friend record")
        print("2 Search for a friend")
        print("3 Run reports")
        print("4 Exit")
        choice = prompt_int("Select:", 1, 4)
        if choice == 1:
            if input("Load data from CSV file(1) or create new friend(2)? (1/2): ").lower().startswith('1'):
                fn = input("Filename: ").strip()
                friends.extend(load_friends(fn))
            else:
                friends.append(create_friend())
        elif choice == 2:
            p = search_friends(friends)
            if p:
                print(YELLOW + f"Selected: {p.get_first_name()} {p.get_last_name()}" + RESET)
                action = input("Edit (e), Delete (d), Cancel (any): ").lower().strip()
                if action == 'e':
                    edit_friend(p)
                elif action == 'd':
                    delete_friend(friends, p)
                
        elif choice == 3:
            run_reports(friends)
        else:
            save_friends(friends_file, friends)
            print(GREEN + "Goodbye!" + RESET)
            break


if __name__ == '__main__':
    main()
            

       