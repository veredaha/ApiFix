
class Customer():
    """function creates class Customer
         :returns: None 
         """
    def __init__(self,id:int, username:str, address:str) -> None:
        self._id = id
        self._username = username
        self._address = address