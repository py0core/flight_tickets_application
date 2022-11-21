import re
# checking for name = str
def is_name(name: str) -> bool:
    while not name.isalpha():
        return False

# checking for email validation
def is_email(email:str) -> bool:
    pat:str = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    while not re.match(pat, email):
         return False

# cheak for password validation
def is_pass(password:str) -> bool:
    while len(password) < 6  :
        return False


# Create Account Function
def account_info(start:bool) -> dict:
    while start is True:
        # creating a main dict
        accounts_info_dict: dict = dict()
        # cycling throw account info for input
        accounts_info: dict = {'first_name':str,'last_name':str,'email':str,'password':str}
        # looping for amount of account info
        for place in range(len(accounts_info)):
            # creating secondary dict
            accounts_dict:dict = {}
            # looping throw the account info for each input
            for info in accounts_info:
                # getting input
                accounts_dict[info] = input(f'{info}: ')
                # validating email input
                if info == 'email':
                    # looping while invalid
                    while is_email(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m{accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                        accounts_dict[info] = input(f'{info}: ')
                        # if invalid twice quiting the program
                        if  is_email(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                    # validating password input
                elif info == 'password':
                    # looping while invalid
                    while is_pass(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m password should be at least 6 characters log\033[0;30;0m')
                        accounts_dict[info] = input(f'{info}: ')
                        # if invalid twice quiting the program
                        if is_pass(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                     # validating password input
                else:
                    # looping while invalid
                    while is_name(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m{accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                        accounts_dict[info] = input(f'{info}: ')
                        # if invalid twice quiting the program
                        if  is_email(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                # adding secondary dict to main dict
            accounts_info_dict[accounts_dict['email']] = accounts_dict
            # indicating validation of program
            print('\033[0;32;1m Account Saved In System\033[0;30;0m')
            #end of program
            start = False
            return accounts_info_dict
print(account_info(True))
