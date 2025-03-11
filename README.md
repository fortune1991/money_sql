# Money Pots  

## Video Demo:  
<https://www.youtube.com/watch?v=9nUeLk2rJWc&ab_channel=MichaelFortune>  

## Description:  
Money Pots is a budgeting calculator designed for travelers. It allows users to divide their savings into "Vaults" and "Pots" to better manage their funds. A detailed explanation of its functionality is provided upon execution.  

The program's user interface (UI) is inspired by text-based adventure games, prompting users to input data through a series of interactive questions.  

## OOP and Design Principles  
One of the key goals of this project was to gain a deeper understanding of Object-Oriented Programming (OOP). The core elements—**User, Pot, Vault, and Transactions**—are implemented as class objects. These classes include instance and class methods that calculate updated values for Vaults and Pots.  

A key feature of the program is that users can create as many Vaults or Pots as they like. The **step-by-step instantiation** of these objects ensures they are linked correctly based on user input. **Error handling** was also carefully considered as part of the approach.  

At this stage, the primary development focus was ensuring that these objects interact within the expected hierarchy. As the program evolved, I also identified opportunities to consolidate reusable code into functions, improving the clarity and efficiency of the `main()` function.  

## Code Structure  
The codebase is organized into three main files:  

- **`project.py`** – Contains the main function along with three additional user-defined functions, as required by CS50.  
- **`project_classes.py`** – Houses all class definitions and associated methods.  
- **`project_functions.py`** – Includes supplementary user-defined methods. This separation enhances code maintainability.  

## Future Development  
Currently, the program is implemented in its simplest form, primarily modeling interactions between transactions, pots, and vaults. Some additional data, such as transaction dates, is collected but not yet integrated into the logic.  

The next phase of development aims to expand its functionality into **budget forecasting and financial modeling**. To achieve this, a database will be introduced—initially using **CSV files** and later transitioning to **SQL**.  

The UI will also evolve in multiple stages:  

1. Converting the text-based interface into a **CLI tool** using Typer.  
2. Developing a **web application** for broader accessibility.  
3. Creating a **mobile app** for on-the-go budget management.  

Through these iterations, I hope to explore different disciplines in computer science and continue my learning journey beyond CS50.  



