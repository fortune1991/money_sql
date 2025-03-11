import datetime, os, sqlite3
from project_classes import User, Vault, Pot, Transaction
from project_functions import submit_transaction, print_slow, int_validator, collect_date, convert_date, summary, create_pot, create_user, create_vault, create_profile, instructions, re_vaults, re_pots, re_transactions, count_pots, count_transactions, count_vaults
from time import sleep
from database import create_database


def main():
    vaults = {}
    pots = {}
    transactions = {}
    
    # check if database exists

    database_exists = os.path.isfile("/Users/michaelfortune/Developer/projects/money/money_sql/money.db")
    
    if not database_exists:

        create_database()
        
        print_slow("""
Welcome to Money Pots, your savings and budgeting calculator.
        """)
        print_slow(instructions())
        
        user, vaults, pots = create_profile()
    
    if database_exists:

        # Establish a connection to the Database
        db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        #log user in
        while True:
            print_slow("""
Welcome to Money Pots, your savings and budgeting calculator. Let me help you to login and view your profile. What's your username?
    """)
            login = input().strip() # Remove trailing white space
            user_exists = False

            # SQL QUERY TO DETERMINE IF USER EXISTS

            res = cur.execute("SELECT username FROM users")
            returned_users = res.fetchall()
            for user in returned_users:
                if login == user[0]:
                    user_exists = True
            
           # REINSTANTIATE OBJECTS FROM DATABASE
                        
            if user_exists == True:
                #reinstantiate user
                user = create_user(login)

                #reinstantiate vaults 
                vaults, vault_ids = re_vaults(login, user)
                
                #reinstantiate pots
                pots, pot_ids = re_pots(vaults, vault_ids, user)

                #reinstantiate transactions - START HERE!!!
                #transaction_exists = os.path.isfile("database/transactions.csv")

                transaction_exists = False
                res = cur.execute("SELECT * FROM transactions")
                returned_transactions = res.fetchall()
                if len(returned_transactions) > 0:
                    transaction_exists = True

                if not transaction_exists:
                    pass

                else:
                    transactions, transaction_ids = re_transactions(pots, pot_ids, user)

                # Update Pots and Vaults values

                for pot in pots.values():
                    pot.pot_value()
                
                for vault in vaults.values():
                    vault.vault_value()

                break

            else:
                print()
                print("User doesn't exist. Respond 'Try again' 'New user' or 'Exit'")    
                print()

                response = input()

                if response == "New user":
                    print()
                    print("Excellent. Please answer the following questions to create a new user profile")
                    user, vaults, pots = create_profile()
                    break
                elif response == "Try again":
                    continue
                elif response == "Exit":
                    exit()
                else:
                    print("Unknown Command. Please try to login again")                
     
    # Loop until exit

    while True:
        print_slow('Now, I await your commands to proceed. Please type: \n\n "Transaction" to submit a new transaction, \n "Summary" to get a report of vault/pot values, or \n "Instructions" to get a further information on how to use Money Pots \n "Vault" to create a new vault \n "Pot" to create a new pot \n "Exit" to terminate the programme')
        print()
        print()
        action = input()

        if action == "Transaction":
    
        # Submit Transactions

            print_slow("Excellent. Now, let me help you create a new transaction.")
            print()
            transactions = {}
            no_transactions = 1
            
            while True:
                try:
                    for x in range(no_transactions):
                        print(f"Transaction {x+1}")
                        print()
                        
                        while True: 
                              
                            # Count existing transactions
                            
                            start_transaction = count_transactions()
                            
                            print_slow("What pot should this pot be assigned to?: ")
                            pot_input = input()

                            # Find the pot using a simple loop
                            selected_pot = None
                            for pot in pots.values():
                                if pot.pot_name == pot_input and pot.username == user.username: 
                                    selected_pot = pot
                                    break

                            if selected_pot:
                                transactions[f"transaction_{x+1}"] = submit_transaction(start_transaction, selected_pot, user)
                                selected_pot.pot_value()
                                break
                            else:
                                print(f"pot '{pot_input}' not found. Please enter a valid pot name.")
                                print()
                    break
                
                except ValueError as e:  
                    print(f"Error: {e}")
                    print()

                except Exception as e:  
                    print(f"An unexpected error occurred: {e}")
                    print()
            
            print()

        # Print Summary

        elif action == "Summary":

            summary(vaults, pots)
            print()

        # Print Instructions

        elif action == "Instructions":
            print_slow(instructions())

        # Create new Vault

        elif action == "Vault":
            vault_count = count_vaults()
            vaults[f"vault_{(vault_count + 1)}"] = create_vault(vault_count, user)
            print()
        
        # Create new Pot

        elif action == "Pot":
            print_slow("What vault will this pot be assigned to? ")
            pot_vault = input()
            pot_count = count_pots()
            selected_vault = None
            for vault in vaults.values():
                if vault.vault_name == pot_vault and vault.username == user.username:
                    selected_vault = vault

            if selected_vault:
                pots[f"pot_{(pot_count + 1)}"] = create_pot(pot_count, selected_vault, user)

            else:
                print(f"Vault '{vault_input}' not found. Please enter a valid vault name.")
                print()
        
        # Exit

        elif action == "Exit":
            print_slow("OK, the program will now terminate. See final values of the vaults and pots below. Thanks for using Money Pots!")
            print()
            summary(vaults, pots)
            print()
            exit()

        else:
            print_slow("Invalid command. Please try again")
            print()
        

if __name__ == "__main__":
    main()