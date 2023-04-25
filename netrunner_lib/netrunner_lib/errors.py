"""Custom netrunner_lib error definitions
This file should always be included as `from netrunner_lib import errors`, so it is easier to track where the errors are being used (i.e. raise errors.FILE_NOT_FOUND).
"""

class INVALID_FILE_EXTENSION(Exception):
    """Exception raised an invalid file extension

    Attributes:
        - file_name: file name attempted to be used
        - extra_info:str any extra info provided for the error
    """
    def __init__(self, file_name:str,extra_info:str=""):
        self.file_name = file_name
        self.extra_info = extra_info
        super().__init__(f"Invalid file extension: {self.file_name} -- {self.extra_info}")

class CARD_NOT_FOUND(Exception):
    """Exception raised when a card isn't found where it was expected

    Attributes:
        - card_name: file name attempted to be used
        - extra_info:str any extra info provided for the error
    """
    def __init__(self, card_name:str,extra_info:str=""):
        self.card_name = card_name
        self.extra_info = extra_info
        super().__init__(f"Card not found: {self.card_name} -- {self.extra_info}")

class FILE_NOT_FOUND(Exception):
    """Exception raised when a file was not found

    Attributes:
        - file_name:str file name attempted to be used
        - extra_info:str any extra info provided for the error
    """
    def __init__(self, file_name:str,extra_info:str=""):
        self.file_name = file_name
        self.extra_info = extra_info
        super().__init__(f"File not found: {self.file_name} -- {self.extra_info}")

class CARD_STATE_ERROR(Exception):
    """Exception raised when card state is invalid

    Attributes:
        - card_state:str current state of the card
        - extra_info:str any extra info provided for the error
    """
    def __init__(self, card_state:str,extra_info:str=""):
        self.card_state = card_state
        self.extra_info = extra_info
        super().__init__(f"Invalid card state: {self.card_state} -- {self.extra_info}")
    