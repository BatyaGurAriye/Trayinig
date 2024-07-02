class OurFirstError(Exception):
    def __init__(self):
        super().__init__("this is our error!!")
