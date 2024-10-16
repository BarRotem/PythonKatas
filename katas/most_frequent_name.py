def most_frequent_name(file_path):
    """
    Receives a path to a file containing names (name in each line)
    The function should return the most frequent name in the file.

    You can assume file_path exists in the file system.
    """
    with open(file_path, mode='r') as file:
        #Initialize names_list containing all names separated by \n
        names_list = file.read().splitlines()
        #Count all name occurrences
        name_counts = {}
        for name in names_list:
            if name in name_counts:
                name_counts[name] += 1
            else:
                name_counts[name] = 1
        #Return name with max occurrences
        max_count = max(name_counts, key=name_counts.get)
        return max_count


if __name__ == '__main__':
    print(most_frequent_name('files/names.txt'))
