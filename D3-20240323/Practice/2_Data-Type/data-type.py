# Numeric data types
age = 30  # Integer (int)
price = 19.99  # Float (float)

# Textual data type
name = "Amanda"  # String (str)

# Boolean data type
is_registered = True  # Boolean (bool)

# Collection data types
fruits = ["apple", "cherry", "lime"]  # List (list)
customer = {  # Dictionary (dict)
    "name": "Rendy",
    "age": 30,
    "city": "New York"
}

# Accessing elements in collections
first_fruit = fruits[0]  # Accessing first element in list
customer_name = customer["name"]  # Accessing value by key in dictionary

# Printing data and data types
print("Age:", age, " (type:", type(age), ")")
print("Price:", price, " (type:", type(price), ")")
print("Name:", name, " (type:", type(name), ")")
print("Registered:", is_registered, " (type:", type(is_registered), ")")
print("First fruit:", first_fruit)
print("Customer name:", customer_name)
