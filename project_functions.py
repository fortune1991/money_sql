import datetime, os, sqlite3
from project_classes import User, Vault, Pot, Transaction
from time import sleep

def submit_transaction(x, pot, user):
    # Collect transaction name
    print_slow("\nPlease provide a name reference for this transaction: ")
    transaction_name = input()
    # Collect transaction id
    transaction_id = x + 1
    # Collect date data and create date object
    print_slow("\nExcellent. Now we'll define when the transaction took place. Please note, all date input values must be in the format DD/MM/YY")
    date = collect_date("Date of transction: ")
    # Collect transaction type
    while True:
        types = ["in", "out"]
        print_slow('\nPlease define the type of transaction. "in" or "out": ')
        transaction_type = input()
        if transaction_type not in types:
            print_slow_nospace("\nincorrect transaction reference")
        else:
            break
    # Collect transaction amount
    print_slow("\nWhat is the transaction amount?: ")
    while True:
        amount = int_validator()
        if amount > 0:
            break
        else:
            print_slow("\namount must be greater than 0")
        
    if type == "out":
        amount = amount * -1
    else:
        pass

    #Input all information into the Class
    transaction = Transaction(transaction_id=transaction_id, transaction_name=transaction_name, date=date, pot=pot, type=transaction_type, amount=amount, user=user)
    transaction_data = [(transaction_id, transaction_name, date, pot.pot_id, transaction_type, amount, user.username)]
    if transaction:
        transaction_data
        print_slow("\nThanks, your transaction has been created succesfully")
        # save transaction to database
        # Establish a connection to the Database
        db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        # Save transaction to database
        cur.executemany("INSERT INTO transactions VALUES(?, ?, ?, ?, ?, ?, ?)", transaction_data)
        con.commit()
        con.close()
    else:
        print_slow("ERROR: transaction not created succesfully")
    
    return transaction

def print_slow(txt):
    for x in txt: 
        print(x, end='', flush=True)
        sleep(0) #0.025 at end of programme
    print("",end="\n\n")

def print_slow_nospace(txt):
    for x in txt: 
        print(x, end='', flush=True)
        sleep(0) #0.025 at end of programme
    print("",end="\n")

def int_validator():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print_slow("\nInvalid input. Please enter a valid integer: ")
        
    return value

def collect_date(message):
    while True:
        print_slow(message)
        try:
            date_input = input()
            date = datetime.datetime.strptime(date_input,"%d/%m/%y")
            break 
        except ValueError as err:
            print_slow(f"\n{str(err)}")
    return date

def convert_date(string):
    try:
        date_input = string
        date = datetime.datetime.strptime(date_input,"%Y-%m-%d %H:%M:%S")
    except ValueError as err:
        print_slow(f"\n{str(err)}")

    return date

def summary(vaults, pots):
    for i in vaults:
        print_slow_nospace(f"\n\033[31mVault\033[0m") 
        vault_value = vaults[i].vault_value()
        print_slow_nospace(f"{vaults[i].vault_name} = ${vault_value}")
        print_slow_nospace(f"\033[31mPots\033[0m") 
        
        for j in pots:
                if pots[j].vault == vaults[i]:
                    print_slow_nospace(f"{pots[j].pot_name} = ${pots[j].amount}")
                else:
                    continue

def create_user(*args):
    # Establish a connection to the Database
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if args:
        username = args[0]
        user = User(username)
    else:
        print_slow("Now firstly, what is your name?: ")
        username = input()
        user = User(username)
        # save user to database
        users_data = [
        (user.username,),
        ]
        cur.executemany("INSERT INTO users VALUES(?)", users_data)
        con.commit()
        con.close()
    return user

def create_pot(x, vault, user):
    # Establish a connection to the Database
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Collect pot name
    print_slow("\nWhat is your preferred name for the pot?: ")
    pot_name = input()
    # Collect pot id
    pot_id = x + 1
    # Collect start date data and create date object
    print_slow("\nExcellent. Now we'll define when the pot will be in use. Please note, all date input values must be in the format DD/MM/YY")
    start_date = collect_date("What is the start date that this pot will be active?: ")
    # Collect end date data and create date object
    end_date = collect_date("\nWhat is the end date that this pot will be active?: ")
    # Collect pot amount
    print_slow("\nWhat is the amount of money in the pot?: ")
    while True:
        amount = int_validator()
        if amount > 0:
            break
        else:
            print_slow("\namount must be greater than 0") 

    #Input all information into the Class
    pot = Pot(pot_id=pot_id, pot_name=pot_name, start=start_date, end=end_date, vault=vault, amount=amount, user=user)
    
    if pot:
        print_slow_nospace("\nThanks, your pot has been created succesfully")

        # save pot to database
        pots_data = []
        pots_data.append((pot.pot_id, pot.pot_name, pot.start, pot.end, pot.vault_id, pot.amount, pot.username))
            
        cur.executemany("INSERT INTO pots VALUES(?, ?, ?, ?, ?, ?, ?)", pots_data)
        con.commit()
        con.close()
    else:
        print_slow("\nERROR: pot not created succesfully")
    
    return pot

def create_vault(x, user):
    # Establish a connection to the Database
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Collect vault name
    print_slow("\nWhat is your preferred name for the vault?: ")
    vault_name = input()
    # Collect vault id
    vault_id = x + 1
    # Collect start date data and create date object
    print_slow("\nExcellent. Now we'll define when the vault will be in use. Please note, all date input values must be in the format DD/MM/YY")
    start_date = collect_date("What is the start date that this vault will be active?: ")
    # Collect end date data and create date object
    end_date = collect_date("\nWhat is the end date that this vault will be active?: ")
    #Input all information into the Class
    vault = Vault(vault_id=vault_id, vault_name=vault_name, start=start_date, end=end_date, user=user)
    if vault:
        print_slow_nospace("\nThanks, your vault has been created succesfully")
        # save vault to database
        vaults_data = []
        vaults_data.append((vault.vault_id, vault.vault_name, vault.start, vault.end, vault.username))
        cur.executemany("INSERT INTO vaults VALUES(?, ?, ?, ?, ?)", vaults_data)
        con.commit()
        con.close()
    else:
        print_slow("\nERROR: vault not created succesfully")
    return vault

def create_profile():
    # Create a User object
    user = create_user()
    # Count number of existing vaults in database. if not exist = 0
    start_vault = count_vaults()
    # Count number of existing pots in database. if not exist = 0
    start_pot = count_pots()
    # Create a Vault object with valid data
    print_slow(f"Hi {user.username}, let me help you create some vaults. How many do you want to create?: ")
    no_vaults = int_validator()
    vaults = {}
    
    try:
        for x in range(no_vaults):
            print_slow(f"Vault {(x+1)+start_vault}")
            vaults["vault_{0}".format((x+1)+start_vault)] = create_vault((x+start_vault), user)
    
    except ValueError as e:  
        print_slow(f"Error: {e}")

    except Exception as e:  
        print_slow(f"An unexpected error occurred: {e}")

    # Create Pot objects with valid data
    print_slow("Now, let me help you create some pots. How many do you want to create?: ")
    no_pots = int_validator()
    pots = {}
    
    while True:
        try:
            for x in range(no_pots):
                print_slow(f"Pot {(x+1)+start_pot}")
                
                while True: 
                    print_slow("What vault should this pot be assigned to?: ")
                    vault_input = input()

                    # Find the vault using a simple loop
                    selected_vault = None
                    for vault in vaults.values():
                        if vault.vault_name == vault_input and vault.username == user.username:
                            selected_vault = vault
                            break

                    if selected_vault:
                        pots[f"pot_{(x+1)+start_pot}"] = create_pot((x+start_pot), selected_vault, user)
                        break
                    else:
                        print_slow(f"Vault '{vault_input}' not found. Please enter a valid vault name.")
                        
            break
        
        except ValueError as e:  
            print_slow(f"Error: {e}")
            
        except Exception as e:  
            print_slow(f"An unexpected error occurred: {e}")
            
    # Summary of the vaults and pots values
    print_slow("See below list of vaults and their summed values")
    summary(vaults, pots)
    return user, vaults, pots

def instructions():
    return """
In this program, your savings are organized into two categories: Vaults and Pots.

- A Vault is a collection of Pots, each assigned a specific time frame.
- A Pot represents an individual budget within a Vault.

For example, between 17/03/25 and 17/01/26, you might create a 'Travelling' Vault
to manage your holiday expenses. This Vault could contain multiple Pots, each
representing a budget for a different destination.

Once you've set up your Vaults and Pots, the program will enter an infinite loop
where you can choose from three options:

1. Submit a transaction – Transactions are linked to a specific Pot and either 
increase or decrease its balance, depending on the selected type.
2. View a summary – This provides an updated overview of your Vaults and Pots, 
reflecting any transactions you've made.
3. Exit the program – A final summary of your balances will be displayed before 
the program closes.
4. Create a new vault - will be associated with the user currently logged in
5. Create a new pot - will be associated with the user currently logged in

Please note: This program does not store data permanently. Once you exit, all 
Vault and Pot data will be lost.

We hope you enjoy using Money Pots!"""

def re_vaults(name, user):
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Create vault and vault_ids variables
    vaults = {}
    vault_ids = []
    # Searcb the vaults database for all information for defined user 
    res = cur.execute("SELECT * FROM vaults WHERE username = ?", (name,))
    returned_vaults = res.fetchall()
    for vault in returned_vaults:
        # Create variables
        vault_ids.append(int(vault[0]))
        vault_id = int(vault[0])
        vault_name = vault[1]
        start_date = convert_date(vault[2])
        end_date = convert_date(vault[3])
        # Create vault instance
        vault = Vault(vault_id=vault_id, vault_name=vault_name, start=start_date, end=end_date, user=user)
        # Add instance to vaults object dictionary
        vaults["vault_{0}".format(vault_id)] = vault
    
    con.close()
    return vaults, vault_ids

def re_pots(vaults, vault_ids, user):
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Create pots and pot_id variables
    pots = {}
    pot_ids = []
    # Searcb the vaults database for all information for defined vault_ids
    for vault in vault_ids:
        res = cur.execute("SELECT * FROM pots WHERE vault_id = ?", (vault,))
        returned_pots = res.fetchall()
        for pot in returned_pots:
            # Create variables
            pot_id = int(pot[0])
            pot_name = pot[1]
            start_date = convert_date(pot[2])
            end_date = convert_date(pot[3])
            amount = int(pot[5])
            vault = vaults[f"vault_{pot[4]}"] # Dictionary key format is "Vault_1: Object"
            # Create pot instance
            pot = Pot(pot_id=pot_id, pot_name=pot_name, start=start_date, end=end_date, vault=vault, amount=amount, user=user)
            # Add instance to pots object dictionary
            pots[f"pot_{pot.pot_id}"] = pot
            # Append pot_id to list
            pot_ids.append(pot_id)

    con.close()
    return pots, pot_ids

def re_transactions(pots, pot_ids, user):
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Create pots and transaction_id variables
    transactions = {}
    transaction_ids = []
    # Searcb the pots database for all information for defined pot_ids
    for pot in pot_ids:
        res = cur.execute("SELECT * FROM transactions WHERE pot_id = ?", (pot,))
        returned_transactions = res.fetchall()
        for transaction in returned_transactions:
            # Create variables
                transaction_id = int(transaction[0])
                transaction_name = transaction[1]
                date = convert_date(transaction[2])
                type = (transaction[4])
                amount = int(transaction[5])
                pot = pots[f"pot_{transaction[3]}"] # Dictionary key format is "Pot_1: Object"
                # Create pot instance
                transaction = Transaction(transaction_id=transaction_id, transaction_name=transaction_name, date=date, pot=pot, type=type, amount=amount, user=user)
                # Add instance to transactions object dictionary
                transactions[f"transaction_{transaction.transaction_id}"] = transaction
                # Append transaction_id to list
                transaction_ids.append(transaction_id)
    con.close()
    return transactions, transaction_ids

def count_pots():
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Search the database
    res = cur.execute("SELECT * FROM pots")
    returned_pots = res.fetchall()
    # Calculate Length of returned pots
    return len(returned_pots)
    
def count_vaults():
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Search the database
    res = cur.execute("SELECT * FROM vaults")
    returned_vaults = res.fetchall()
    # Calculate Length of returned pots
    return len(returned_vaults)
        
def count_transactions():
    # Establish Database Connection
    db_path = "/Users/michaelfortune/Developer/projects/money/money_sql/money.db" 
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Search the database
    res = cur.execute("SELECT * FROM transactions")
    returned_transactions = res.fetchall()
    # Calculate Length of returned pots
    return len(returned_transactions)