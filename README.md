# codebase-cleanup-template

To get started with the ["Codebase Cleanup" Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/README.md).

## Setup

Create virtual environment:

```sh
conda create -n cleanup-env python=3.8
```

```sh
conda activate cleanup-env
```

Install packages:

```sh
pip install -r requirements.txt
```


## Configuration

Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).

Sign up for a [SendGrid Account](https://sendgrid.com/), verify single sender, then obtain a Sendgrid API Key. 


Set environment variables using a ".env" file approach:

```sh
ALPHAVANTAGE_API_KEY="..."

SENDER_ADDRESS="example@gmail.com"
SENDGRID_API_KEY="SG...."
```


## Usage and Details

Run the game:

```sh
python -m app.game
```

The game will simulate a game of rock, paper, scissors between the user and the computer.  To begin the game, write the above command into the command line and hit enter.  The terminal will prompt the user to choose rock, paper, or scissors.  If the user input does not match one of these three choices, the computer will show an error message and exit the program.  

If the user choice is valid, the computer will then make a choice at random between one of the three options.  Once this is done, the user and computer choices will be passed into a function called determine_winner, which will select the winning choice, if there is one.  Inside of the function is a dictionary which pairs the winning choices.  The function will navigate the dictionary to return either a string variable that says "rock", "paper", or "scissors", or it will return a None value.

After the function returns the winning value or None, the result is passed through an if statement that determines whether the user or computer won, or if it was a tie.  The program will then print a message telling the user of the outcome and will exit.



Run the inventory report:

```sh
python -m app.groceries
```

This program will list the inventory and calculate the average price of the items on the inventory list.  

The program will begin by looking for a file called "products.csv" in the app directory.  If there is none, it will use a file called "default_products.csv".  

The report will consist of a summary of the number of products, followed by a list of the names of the products and their prices.  At the end of the report, the program will calculate the average price across all products in the inventory list.  To do this, the program will pull the prices of the products off of the csv, convert them to floats, and append them to the list.  The program uses the statistics module to calculate the mean and then prints it in the output as dollars and cents.

The program uses an imported function called to_usd that is written in another file called utils.py, inside the app directory.  This function takes a float value and will return a string formatted as $0.00.  The function is stored in another file because it is used across several files in the app directory.  All prices in the groceries file are formatted by this function.



Run the crypto analysis:

```sh
python -m app.crypto
```

The crypto.py file allows a user to see the current price of any cryptocurrency.  The program pulls data from the AlphaVantage API.  The way the user will interface with the program is by seeing an initialization message, then they will be prompted to enter a ticker symbol for a cryptocurrency.  When they choose one, say BTC.  The program will then show the latest date for the data and will show the last closing price.

To do this, the program passes the ticker that the user selects into a function called fetch_data_crypto.  This function is imported from another file called alphavantage_service.py.  The function interfaces with the API and converts the returned json response into a dictionary.  The remainder of the program works with the dictionary and returns the desired data, formatted as USD using the to_usd function described above.

Run the stocks report:

```sh
python -m app.stocks
```

The stocks.py file functions very similarly to the crypto.py file with a few differences.  The user will see the same data represented and requested the same way, but on the back end there are a couple differences.

The function that interfaces with AlphaVantage is called fetch_data_stocks, and will collect a csv file rather than a json file from the API.  Because it collects this datatype, the function returns a pandas dataframe instead of a dictionary.  Because this is the case, the way the code is written is to deal with the dataframe object rather than a dictionary object.  

Run the unemployment report:

```sh
python -m app.unemployment
```

The unemployment.py file will show historical monthly unemployment data, generating a bar chart and a csv file for the user.  Similarly to the stocks.py and crypto.py files, the unemployment.py program interfaces with the AlphaVantage API and pulls data off of the internet.  Unlike the stocks and crypto files, this program requires no user input.  It simply will generate the chart and export the data to a csv when it is activated.

This program uses a standalone function called fetch_data_unemployment, which is stored in the alphavantage_service.py file and imported into the program.  The fetch_data_unemployment function returns a dictionary object containing the relevant unemployement data, specifically dates and unemployment rates.

After the function is run and the data is downloaded from the AlphaVantage API, the dictionary is converted into a pandas dataframe, which is later used to make the bar chart.  The pandas and plotly.express packages are used for data analysis and visualization.  The bar chart and data csv are stored as a png file and a csv file within a folder named "reports" inside of the repository directory on the user's local computer.

## Testing

To run the tests that have already been written into the code, type the following on the command line:

```sh
pytest
```

To test new or other existing functions in the repository, follow these steps:

1. Create a new file in the "tests" directory whose name either starts with "test_" or ends with "_test.py"
2. Import the desired function into the test file
3. Write a function definition using the following steps:  
    
    a. Write the "assert" key word on the next line, then write the tested function with the desired inputs, use the == operator to write the expected output

When the desired tests are written, use the above command again from the command line. 