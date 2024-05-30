# #!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"


    def __setattr__(self, name, value):
        if name == 'size' and not isinstance(value, int):
            print('size must be an integer')
        else:
            super().__setattr__(name, value)

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = "New" 