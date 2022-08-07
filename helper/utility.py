def print_table(old_names_list):
    print("="*147)
    print("|| %-5s || %-58s || %-58s || %-8s ||" % ('Sr.No',  'Old Name', 'New Name', 'Modified'))
    print("="*147)
    for i, name in enumerate(old_names_list):
        print("|| %-5d || %-58s || %-58s || %-8s ||" % (i+1,  name, name, 'no'))
    print("="*147)


def remove_blank_space(directory, old_names_list):
    pass

def replace_blank_space(directory, old_names_list, pattern):
    pass

def remove_pattern(directory, old_names_list):
    pass

def replace_pattern(directory, old_names_list):
    pass

def add_prefix_pattern(directory, old_names_list, pattern):
    pass

def add_suffix_pattern(directory, old_names_list, pattern):
    pass

def remove_extension(directory, old_names_list):
    pass

def change_extension(directory, old_names_list, new_extension):
    pass


def welcome(old_names_list):
    print("\n\n")
    print("%88s" % ("Welcome to Bulk Rename Tool\n"))
    print("%88s" % "Created by Suresh (shhotu010)")

    while True:
        print("\n\n", '*' * 148)
        choices = '''
                        1. Print Table
                        2. Remove/Replace Blank Space
                        3. Remove/Replace Pattern
                        4. Add Prefix/Suffix Pattern
                        5. Remove/Change Extension
                        6. Exit
        '''
        print("\n\tList of operations: \n" + choices)
        print('*' * 148)
        choice = int(input("Enter your choice: "))
        print("\n\n")
        if choice == 1:
            print_table(old_names_list)
        elif choice == 2:
            while True:
                next_choice = int(input("Enter your choice: \n0. Remove blank spaces\n1. Replace blank spaces"))
                if next_choice == 0:
                    utility.remove_blank_spaces(directory, old_names_list)
                    break
                elif next_choice == 1:
                    utility.replace_blank_space(directory, old_names_list)
                    break
                else:
                    print("\n\n!!!Invalid choice\n")

        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            exit()
        else:
            print("Please enter a valid option.")

