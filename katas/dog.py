class Dog:
    """
    The Dog class has a constructor (__init__) that initializes the name and breed attributes of the class.
    It also has two methods: bark(), which prints a simple bark message,
    and describe(), which prints the dog's name and breed.

    1. In the constructor, create a new attribute called `self.position` which defines the position state of the dog.
       The attribute possible values are: sitting, standing, jumping. Default is sitting.
    2. Implement the following methods: sit(), stand(), jump(). Each method changes the position of the dog.
    3. Extend the bark() function to receive an argument called `n` with default values of 2, the dog should bark n times.
    4. Add the dog position to the description printed in describe method. E.g.: `I'm John, a Puddle. I'm standing.`

    """

    def __init__(self, name, breed, position="sitting"):
        self.name = name
        self.breed = breed
        self.position = position  # Position possible values are : sitting, standing, jumping

    def bark(self, n=2):
        for i in range(n):
            print("Woof! Woof!")

    def sit(self):
        self.position = "sitting"

    def stand(self):
        self.position = "standing"

    def jump(self):
        self.position = "jumping"

    def describe(self):
        print(f"I'm {self.name}, a {self.breed}. I'm {self.position}")
        print()


if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")

    my_dog.bark(7)
    my_dog.describe()
