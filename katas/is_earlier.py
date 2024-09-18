def is_earlier(date1, date2):
    """
    Compares two ISO 8601 date strings and returns True if the first date is earlier than the second date.
    """
    split_date1 = date1.split("-")
    split_date2 = date2.split("-")
    for time_component_index in range(len(split_date1)):
        if int(split_date1[time_component_index]) > int(split_date2[time_component_index]):
            #This means date1 is later than date2
            return False
        elif int(split_date1[time_component_index]) < int(split_date2[time_component_index]):
            # This component was found smaller, after checking all previous ones. return true
            return True
    #This statement is executed only when all components were checked and were equal.
    #This means that the dates are similar, return False.
    return False


date1 = "2023-07-29"
date2 = "2023-08-01"
result = is_earlier(date1, date2)
print(result)  # Expected output: True

date1 = "2024-01-01"
date2 = "2023-12-31"
result = is_earlier(date1, date2)
print(result)  # Expected output: False

date1 = "2022-12-31"
date2 = "2022-12-31"
result = is_earlier(date1, date2)
print(result)  # Expected output: False

"""
To complete this exercise:
--------------------------
Implement the 'is_earlier' function to compare two ISO 8601 date strings and return True if the first date is 
earlier than the second date.

Exercise Breakdown:
-------------
ISO 8601 is an international standard for date and time representation. An ISO date string typically looks like "YYYY-MM-DD". 
Note that the dates are formatted in a way that chronological order corresponds to lexicographical order.

"""
