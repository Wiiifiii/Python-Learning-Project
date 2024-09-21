# -*- coding: utf-8 -*-
"""
#KT 4

Tutustu omatoimisesti Pandas-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. 
Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa.  
Esimerkkisovellus on vapaavalintainen.

#TASK 4
Independently explore the Pandas library. You can use resources like the W3Schools website for reference.
Create an example program that uses the Pandas library and explain it with Python comments.
The example application is up to your choice.

"""
# Importing the Pandas library
import pandas as pd

# Explanation: Pandas is a powerful library for data manipulation and analysis.
# It provides data structures like DataFrames to store data in rows and columns, similar to a table in a database.

if __name__ == '__main__':
    # Create a dictionary with sales data
    sales_data = {
        'Product': ['Laptop', 'Tablet', 'Smartphone', 'Tablet', 'Laptop', 'Smartphone'],
        'Region': ['North', 'South', 'East', 'West', 'North', 'East'],
        'Units Sold': [50, 30, 150, 70, 45, 120],
        'Price per Unit': [1000, 500, 800, 450, 1100, 850]
    }

    # Create a Pandas DataFrame from the dictionary
    df = pd.DataFrame(sales_data)

    # Explanation: The DataFrame is the core data structure of Pandas, similar to a table.
    # It's created here from a dictionary, with the keys becoming column headers.

    print("Sales Data:")
    print(df)
    print()

    # Calculate total sales for each transaction (Units Sold * Price per Unit)
    df['Total Sales'] = df['Units Sold'] * df['Price per Unit']

    # Explanation: We can create new columns in the DataFrame by performing operations on existing columns.
    # Here, we calculate the 'Total Sales' by multiplying 'Units Sold' and 'Price per Unit'.

    print("Sales Data with Total Sales:")
    print(df)
    print()

    # Group by product and calculate the total units sold and total sales for each product
    product_summary = df.groupby('Product').agg({'Units Sold': 'sum', 'Total Sales': 'sum'})

    # Explanation: `groupby()` allows us to group the data by a specific column (in this case, 'Product'),
    # and `agg()` allows us to apply aggregation functions (like sum) on the grouped data.
    
    print("Total Units Sold and Total Sales by Product:")
    print(product_summary)
    print()

    # Filter the DataFrame to show only transactions where total sales are greater than 50,000
    high_sales = df[df['Total Sales'] > 50000]

    # Explanation: We can filter data in a DataFrame by applying conditions.
    # Here, we're selecting only rows where the 'Total Sales' column has values greater than 50,000.

    print("Transactions with Total Sales > 50,000:")
    print(high_sales)
    print()

    # Calculate the average price per unit for each product
    avg_price = df.groupby('Product')['Price per Unit'].mean()

    # Explanation: Here we group the data by 'Product' and calculate the mean (average) of the 'Price per Unit' column.
    
    print("Average Price per Unit by Product:")
    print(avg_price)



