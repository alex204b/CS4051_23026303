#CS4051_23026303
#The purpose of the program is to calculate the MODE, MEDIAN, MEAN and SKEWNESS of a vector
#The author of the proggram is Bordei Alexandru StudentID:23026303
#08.05.2024

import math  #Import the math library to access mathematical functions.

#Read integers from user input and return them as a list.
def read_vector():
    vector = []  #Initialize an empty list to store integers.
    while True:  #Begin an infinite loop to continuously prompt for input until valid input is received.
        #Prompt user for a string of numbers, allowing both commas and spaces as separators.
        input_str = input("Enter numbers separated by spaces or commas (at least two numbers required): ")
        #Remove commas and split the string into a list based on spaces.
        inputs = input_str.replace(',', ' ').split()
        #Check if all split inputs are numeric and if there are at least two numbers.
        if all(item.lstrip('-').isdigit() for item in inputs) and len(inputs) >= 2:
            #Convert all string inputs to integers and add them to the vector list.
            vector.extend(map(int, inputs))
            return vector  # Return the filled vector.
        elif not all(item.lstrip('-').isdigit() for item in inputs):
            #If any input is non-numeric, inform the user and prompt again.
            print("Error: Please enter only numbers. Try again.")
        else:
            #If fewer than two numbers are entered, prompt for more input.
            print("Error: Please enter at least two numbers.")

#Function to add more numbers to the existing vector.
def add_more_numbers(vector):
    while True:  #Similar to read_vector, loop until valid input is received.
        input_str = input("Enter additional numbers separated by spaces or commas: ")
        inputs = input_str.replace(',', ' ').split()  #Remove commas and split the string into a list based on spaces.
        if all(item.lstrip('-').isdigit() for item in inputs): #Check if all split inputs are numeric and if there are at least two numbers.
            vector.extend(map(int, inputs))
            return vector  #Return the updated vector.
        else:
            print("Error: Please enter only numbers. Try again.")

# Function to read numbers from a specified file.
def read_from_file():
    filepath = input("Enter the path to the data file: ")  # Ask the user for the file path.
    vector = []
    try:
        with open(filepath, 'r') as file:  #Attempt to open the specified file in read mode.
            data = file.read()  #Read the entire file content.
            inputs = data.replace(',', ' ').split()  #Process the data like input strings.
            if all(item.lstrip('-').isdigit() for item in inputs):
                vector.extend(map(int, inputs)) #Convert all string inputs to integers and add them to the vector list.
            else:
                print("Error: File contains non-numeric values.")
                return None
        return vector
    except FileNotFoundError:  #If the file cannot be found, notify the user.
        print("Error: File not found.")
        return None

#Calculate the mode of the vector.
def calculate_mode(vector):
    from collections import Counter  #Import Counter to count occurrences of each element.
    vector_sorted = sorted(vector)  #Sort the vector to prepare for counting.
    count = Counter(vector_sorted)  #Count the frequency of each element in the vector.
    max_occurrences = max(count.values())  #Find the maximum occurrence frequency.
    mode = [num for num, freq in count.items() if freq == max_occurrences]  # Identify all numbers that occur most frequently.
    if len(mode) == len(vector):  #If each number appears only once, indicate no mode.
        print("No mode; every value appears only once.")
    elif len(count) == 1:  #If all numbers are the same, that number is the mode.
        print(f"Mode: {mode[0]} (all numbers are the same)")
    else:
        print(f"Mode: {mode}")  #Display the mode(s).

#Calculate the median of the vector.
def calculate_median(vector):
    vector_sorted = sorted(vector)  #Sort the vector.
    n = len(vector_sorted)  #Find the number of elements in the vector.
    mid = n // 2  #Find the middle index.
    if n % 2 == 0:  #If there's an even number of elements, calculate median as the average of the two middle numbers.
        median = (vector_sorted[mid - 1] + vector_sorted[mid]) / 2
    else:  #If there's an odd number of elements, the median is the middle element.
        median = vector_sorted[mid]
    return median  #Return the median.

#Calculate the mean of the vector.
def calculate_mean(vector):
    mean = sum(vector) / len(vector)  #Sum the vector and divide by the number of elements.
    return mean  #Return the mean.

#Calculate the standard deviation of the vector.
def calculate_std_deviation(vector):
    mean = calculate_mean(vector)  #First calculate the mean.
    variance = sum((x - mean) ** 2 for x in vector) / (len(vector) - 1)  #Then calculate variance.
    return math.sqrt(variance)  #Take the square root of variance to get standard deviation.
def calculate_skewness(vector):
    # Calculate the mean (average) of the vector
    mean = calculate_mean(vector)
    
    # Calculate the median of the vector
    median = calculate_median(vector)
    
    # Calculate the standard deviation of the vector. This involves:
    # 1. Subtracting the mean from each element x in the vector,
    # 2. Squaring the result of each subtraction,
    # 3. Summing all the squared results,
    # 4. Dividing the total by the number of elements minus one (for sample standard deviation),
    # 5. Taking the square root of the result to get the standard deviation
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in vector) / (len(vector) - 1))
    
    # Calculate the skewness using the formula: (3 * (mean - median)) / standard deviation
    # This formula assesses the asymmetry of the data distribution around the mean.
    skewness = (3 * (mean - median)) / std_dev
    
    # Print the calculated skewness value
    print("Skewness:", skewness)
#Define the menu function for user interaction.
def menu():
    vector = read_vector()  #Initialize the vector by reading from user input.
    #Define available actions with corresponding functions.
    actions = {
        '1': ("Calculate Mode", lambda: calculate_mode(vector)), #Option to calculate the mode.
        '2': ("Calculate Median", lambda: calculate_median(vector)), #Option to calculate the median.
        '3': ("Calculate Mean", lambda: calculate_mean(vector)), #Option to calculate the mead.
        '4': ("Calculate Skewness", lambda: calculate_skewness(vector)), #Option to calculate the skewness.
        '5': ("Add more numbers", lambda: add_more_numbers(vector)), #Option to calculate add more numbers in the vector.
        '6': ("Load numbers from a file", lambda: read_from_file()), #Option to read a vector from file.
        '7': ("Read a new vector", lambda: read_vector()), #Option to read a new vector. 
        '8': ("Exit", None)
    }

    #Loop to display the menu and process user choices.
    while True:
        print("\nMenu Options:")
        for key in actions:
            print(f"{key}. {actions[key][0]}")  #Print each menu option.
        choice = input("Select an option: ")  #Ask for user input.
        if choice == '8':  # Exit option.
            print("Exiting the program.")
            break  #Exit loop and end program.
        elif choice in actions and actions[choice][1]:
            result = actions[choice][1]()  #Execute the function associated with the chosen option.
            if result is not None:
                print("Updated Vector:", result)  #Show updated vector or result.
        else:
            print("Invalid option, please try again.")  #Handle invalid input.

menu()  #Calling the menu function.
