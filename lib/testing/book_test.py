
class Book:
    def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")
        self.page_count = page_count

    def turn_page(self):
        return "Flipping the page...wow, you read fast!"
