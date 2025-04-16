# Money Pots  

## Description:  
Money Pots is a budgeting calculator designed for travelers. It allows users to divide their savings into "Vaults" and "Pots" to better manage their funds. A detailed explanation of its functionality is provided upon execution.  

The program's user interface (UI) is inspired by text-based adventure games, prompting users to input data through a series of interactive questions.  

## OOP and Design Principles  
One of the key goals of this project was to gain a deeper understanding of Object-Oriented Programming (OOP). The core elements—**User, Pot, Vault, and Transactions**—are implemented as class objects. These classes include instance and class methods that calculate updated values for Vaults and Pots.  

A key feature of the program is that users can create as many Vaults or Pots as they like. The **step-by-step instantiation** of these objects ensures they are linked correctly based on user input. **Error handling** was also carefully considered as part of the approach.  

At this stage, integration of an SQLite3 database was also incorporated. To interact with the database, it also required a basic "login" function to recognise the returning user and some logic to reinstantiate the User, Vaults, Pots and Transaction objects from the database records.  

## Code Structure  
The codebase is organized into three main files:  

- **`project.py`** – Contains the main function along with three additional user-defined functions 
- **`project_classes.py`** – Houses all class definitions and associated methods.  
- **`project_functions.py`** – Includes supplementary user-defined methods. This separation enhances code maintainability.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fortune1991/money_sql.git
   cd money-pots

2. **Run the application**:
    ```bash
    python3 project.py

## Future Development  
I plan to develop the project as below: 

1. **Additional features** provided for "Forecasting", to predict future expenditure and it's impact on budgets 
2. Use **Grafana** to provide realtime analytics from the database
3. Devoloping the programme as a **RESTFUL API** using the Flask framework. This will be deployed and hosted on AWS.
4. Developing a **web application** for broader accessibility, using the Flask Framework. This will be deployed and hosted on AWS.

Through these iterations, I hope to explore different disciplines in computer science and continue my learning journey beyond CS50.  