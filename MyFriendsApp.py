from Friend import Person
from Birthday import Birthday

BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

friends_file = "/workspaces/comp-170-su25-project/friends_database.csv"
filename = friends_file 
def load_friends(filename):
    filename = friends_file 
    friends = []
    try:
        f = open(filename, encoding='utf-8')
        lines = f.read().splitlines()
    except FileNotFoundError:
        return friends
    for row in lines[1:]:
        cols = [c.strip() for c in row.split(',')]
        if not cols or not cols[0]:
            continue
        p = Person(cols[0], cols[1] if len(cols) > 1 else "")
        if len(cols) > 3 and cols[2].isdigit() and cols[3].isdigit():
            p.set_birthday(int(cols[2]), int(cols[3]))
        field_names = ('email_address','nickname','street_address', 'city','state','zip','phone')
        for i, attr in enumerate(field_names, start=4):
            if len(cols) > 1 and cols[i]:
                getattr(p, f"set_{attr}")(cols[i])
        friends.append(p)
    return friends
    
    #if len(lines) <= 1:
    #    result = friends
    #else: 
    #    header_skipped = lines[1:]
    #    for row in header_skipped:
     #       cols = row.split(',')
     #       first = '' 
     #       last = ''
     #       if len(cols) > 0:
     #           first = cols[0].strip()
     #       if len(cols) > 1:
     #           last = cols[1].strip()
     #       person = Person(first, last)
      #      if len(cols) > 3 and cols[2].isdigit() and cols [3].isdigit():
     #           m = int(cols[2])
     #           d = int(cols[3])
  #              person.set_birthday(m, d)
  #          if len(cols) > 4 and cols[4].strip() != '':
       #         person.set_email_address(cols[4].strip())
      #      if len(cols) > 5 and cols[5].strip() != '':
    #            person.set_nickname(cols[5].strip())
     ##       if len(cols) > 6 and cols[6].strip() != '':
      #          person.set_street_address(cols[6].strip())
        #    if len(cols) > 7 and cols[7].strip() != '':
        #        person.set_city(cols[7].strip())
       #     if len(cols) > 8 and cols[8].strip() != '':
       #         person.set_state(cols[8].strip())
      #      if len(cols) > 9 and cols[9].strip() != '':
      #          person.set_zip(cols[9].strip())
     #       if len(cols) > 10 and cols[10].strip() != '':
    #            person.set_phone(cols[10].strip())
    #        friends.append(person)
    #    result = friends
    #return result

friends_file = "/workspaces/comp-170-su25-project/friends_database.csv"
filename = friends_file 
def save_friends(filename, friends):
    filename = friends_file  
    header = ['frist_name', 'last_name','birth_month','birth_day','email_address','nickname','street_address','city','state','zip','phone']
    f = open(filename, 'w', encoding='utf-8')
    f.write(','.join(header) + '\n')
    for p in friends:
        bm = ''
        bd= ''
        if p.birthday is not None:
            bm = str(p.birthday.get_month())
            bd = str(p.birthday.get_day())
        row = [p.get_first_name(), p.get_last_name(), bm, bd,
               getattr(p, 'email_address', ''), getattr(p, 'nickname', ''),
               getattr(p, 'street_address', ''), getattr(p, 'city', ''),
               getattr(p, 'state', ''), getattr(p, 'zip', ''), getattr(p, 'phone', '')]
        f.write(','.join(row) + '\n')
    

def prompt_int(prompt, low, high):
    while True:
        try:
            n = int(input(f"{prompt} ").strip())
            if low <= n <= high:
                return n
        except ValueError:
            pass
        print(f"Please enter a number between {low} and {high}.")
    

def create_friend():
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
    # add more here
    return friend 

def search_friends(friends):
    key = input('Search name: ').lower().strip()
    matches = []
    for p in friends:
        fn = p.get_first_name().lower()
        ln = p.get_last_name().lower()
        if fn.find(key) != -1 or ln.find(key) != -1:
            matches.append(p)
    if len(matches) == 0:
        print('No matches found.')
        result = None
    else:
        print('Found ' + str(len(matches)) + ' match(es):')
        for i in range(len(matches)):
            p = matches[i]
            print(str(i+1) + '. ' + p.get_first_name() + ' ' + p.get_last_name())
        sel = prompt_int('Select number (0 to Exit):', 0, len(matches))
        if sel == 0:
            result = None
        else:
            result = matches[sel-1]
    return result

def edit_friend(p: Person):
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
    if input(f"Are you sure you want to delete {p.get_first_name()} {p.get_last_name()}? (y/N): ").lower().startswith('y'):
        if input("This cannot be undone. Confirm deletion? (y/N): ").lower().startswith('y'):
            friends.remove(p)
            print(GREEN + "Deleted." + RESET)
        else:
            print("Deletion cancelled.")
    else:
        print("Deletion cancelled.")




def main():
    friends = load_friends(friends_file)
    while True:
        print(BOLD + '=== Friend Management ===' + RESET)
        print('1 Create', '2 Search', '3 Reports', '4 Exit', sep='\n')
        choice = prompt_int('Select:', 1, 4)
        if choice == 1 :
            if input('Load CSV? (y/N): ').lower().startswith('y'):
                fn = input('Filename: ').strip()
                friends.extend(load_friends(fn))
            else:
                fnew = create_friend()
                friends.append(fnew)
        elif choice == 2:
            p = search_friends(friends)
        elif choice == 3:
            pass
        else:
            save_friends(friends_file, friends)
            print(BOLD + 'Goodbye!' + RESET)
            break


if __name__ == '__main__':
    main()
            

       