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
        txt = "Hello world"
        print("txt")
        logging.info("hello_world method was used.")
        return txt
