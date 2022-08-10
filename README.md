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
Click on the ‘code’ button
Copy the HTTPS link 
Type git Use the git clone command along with the copied URL from earlier.
```
 $ git clone https://github.com/GiammarcoBozzelli/FoodLover.git

```
Press Enter.

**Now you are ready to try our program!**

You can try using our software by writing :
```
python3 main.py cornstarch
```

To see all available options
```
python3 main.py -h
```


## Functionalities 🛰

When the user types the name of the food,  our software provides him with a user-friendly, easy readable information table. The software returns only the information that the user wants to know: for example if the user wants to know only carbs of that specific food, the output will show only the carbs.
Our software also gives the possibility to the user to type the first letters of the food he is looking for and see all the foods that contain those specific letters.
If The food that the user is interested in knowing the information of is not present in the dataset, the user can add it using the argument ‘-a’ (--add).. 

Note: The food name has to be a string. Can be more than one word and it can contain spaces

OUTPUT | OUTPUT DESCRIPTION 
------------ | ------------- 
Food| Food selected by the user 
Calories| Calories measured on 100 grams of the food selected
Carbs| Crabs in grams of the food selected 
Fats| Total fats in grams of the food selected 
Proteins| Total protein in grams of the food selected 

Note: if the user does not specify the parameters all of them will be given as output by default. 


## Command line parameters: 💾
```
Python3 main.py cornstarch
```




**Positional parameters:** 
- food


**Optional parameters:**
- *-s, –show* : show the list of foods starting with the specified letters; 
- *-h, --help* : show this help message and exit;
- *-a, --add* : Add a food to the database;
- *-p, --protein* : show this help message and exit;
- *-f, --fats* : show this help message and exit;
- *-c, --carbs* : show this help message and exit;
- *-cal, –calories* : show this help message and exit;

## Data Sources 📁

### CSV file
As a database for our software we have used the csv files attached. This dataset contains nutrition values for about 8.8k types of food. We downloaded this dataset from kaggle. https://www.kaggle.com/datasets/trolukovich/nutritional-values-for-common-foods-and-products. We did not use all the nutrition values as we thought that they were too specific. We only used carbs, proteins, fats and calories. 
The software allows to add a food in the CSV file if it's not present

## Testing 🕵️‍♀️
We have tested  Modules.py .You can find both tests in the test.py doc.

To run them from the main folder use:
```
python3 -m unittest test.py
```

All tests run correctly. 



## Authors 🧑‍🤝‍🧑🧑‍🤝‍🧑
- Chiara Dalto 
- Eros Lovato 
- Giammarco Bozzelli
- Angelica Habib

## License 

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)

