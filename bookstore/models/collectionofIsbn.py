class CollectionOfIsbn:
    def __init__(self,isbn:str) -> None:
        """function creates class CollectionOfIsbn
         :returns: None 
         """
        self._isbn = isbn

class AddListOfBooks(CollectionOfIsbn):
    def __init__(self,userId:str,collectionOfIsbns:None) -> None:
        """function creates class AddListOfBooks
         :returns: None 
         """
        self._userId=userId
        self._collectionOfIsbns =None
        if collectionOfIsbns is not None:
            self.collectionOfIsbns =collectionOfIsbns
    def toJson(self) -> str:
        """from class to json
         :returns: str
         """
        result = {}
        for key, val  in self.__dict__.items():
            if val is not None:
                if key.startswith("_"):
                    result[key[1:]] = val
                else:
                    result[key] = val
        return result

