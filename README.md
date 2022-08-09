# FoodLover
# FOODLOVERS 

### Lab of Software Project Development 
## GET TO KNOW WHAT YOU EAT!

The aim of our project is to create a simple software that provides the user the nutritional values of the food he gives as input. 
Our software will provide the user data about proteins, calories, fats and carbohydrates


**Let's check in detail how it works!**

## Get started! 💻
To run the program, as a prerequisite you should have at least **Python 3.10 version.**

In order to start you have to install the required dependencies: 
```
pip3 install -r requirements.txt
```
How to clone the repository and download it: 
Click on the ‘code0 button
Copy the HTTPS link 
Type git Use the git clone command along with the copied URL from earlier.
Ex: $ git clone https://github.com/USERNAME/REPOSITORY
Press Enter.

**Now you are ready to try our program!**

You can try using our software by writing :

```
python3 main.py <name of a food>

```

## Functionalities 🛰

When the user types the name of the food,  our software provides him with a user-friendly, easy readable information table. The software returns only the information that the user wants to know: for example if the user wants to know only carbs of that specific food, the output will show only the carbs.
Our software also gives the possibility to the user to type the first letters of the food he is looking for and see all the foods that contains those specific letter.
If The food that the user is interested in knowing the information of is not present in the dataset, the user can add it using the argument ‘-a’ (--add).. 

Note: The food name has to be a string. Can be more than one word and it can contain spaces

