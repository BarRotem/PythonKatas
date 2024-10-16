def file_exceptions(file_path, op='r'):
    """
    Replaces ' ' by '_' in the given file_path.

    You have to except the MOST SPECIFIC exception and print an informative message for ALL potential file-related exceptions.
    The message must contain the exception name, e.g. RuntimeError, ZeroDivisionError, ...
    """
    try:
        with open(file_path, op) as file:
            content = file.read()
            content_modified = content.replace(' ', '_')
            return content_modified
    except FileNotFoundError:
        return f"FileNotFoundError : The file you're trying to open : '{file_path}' doesn't exist."
    except IsADirectoryError:
        return f"IsADirectoryError : The file you're trying to open : '{file_path}' is a directory !"
    except FileExistsError:
        return f"FileExistsError : The file you're trying to open : '{file_path}' already exists."
    except PermissionError:
        return f"PermissionError : You don't have sufficient permission to open : '{file_path}'"


if __name__ == '__main__':
    print(file_exceptions('files/nonexistent_file.txt'))
    print(file_exceptions('files/somefile'))
    print(file_exceptions('files/'))
    print(file_exceptions('files/someotherfile', op='x'))
    print(file_exceptions('files/someotherfile'))

