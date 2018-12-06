import logging


class ClassTemplate:
    """
    Class' comments
    """
    Attribute = True

    def hello_world(self):
        """
        Method's comments
        """
        self.Attribute = False
        print("Hello world")
        logging.info("hello_world method was used.")

