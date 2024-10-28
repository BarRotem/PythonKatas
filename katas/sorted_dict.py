class SortedDict(dict):
    """
    Implement SortedDict class which is a regular Python dictionary,
    but the keys are maintained in a sorted order

    Usage example:
    x = SortedDict()

    x['banana'] = 'ccc'
    x['apple'] = 'aaa'
    x['orange'] = 'bbb'

    list(x.keys())
    >> ['apple', 'banana', 'orange']

    list(x.values())
    >> ['aaa', 'ccc', 'bbb']

    list(x.items())
    >> [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]
    """

    def __init__(self):
        # Initialize an empty regular dict
        super().__init__()
        self.sorted_keys = []
        self.sorted_values = []
        self.sorted_dict = {}

    def __setitem__(self, key, value):
        assigned = False
        new_sorted_dict = {}
        for old_key in self.keys():
            if old_key > key and not assigned:
                # If old_key should come after the new key, push new key at this position
                # Make sure the mark the new value as assigned, so this check will not be performed again
                new_sorted_dict[key] = value
                assigned = True
            # Always retain old dictionary's structure
            new_sorted_dict[old_key] = self.sorted_dict[old_key]
        if not assigned:
            # New key will not be assigned when it is alphabetically last, make sure to append it in this case
            new_sorted_dict[key] = value
        self.sorted_dict = new_sorted_dict
    def items(self):
        return self.sorted_dict.items()

    def values(self):
        return self.sorted_dict.values()

    def keys(self):
        return self.sorted_dict.keys()


if __name__ == '__main__':
    s_dict = SortedDict()
    s_dict['a'] = None
    s_dict['t'] = None
    s_dict['h'] = None
    s_dict['q'] = None
    s_dict['b'] = None
    print(s_dict.items())
