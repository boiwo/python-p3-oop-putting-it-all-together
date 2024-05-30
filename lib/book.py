
#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def __setattr__(self, name, value):
        if name == 'page_count' and not isinstance(value, int):
            print('page_count must be an integer')
        else:
            super().__setattr__(name, value)

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')

        