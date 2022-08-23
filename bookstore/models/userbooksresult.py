class UserBooksResult: 
 def __init__(self, userId:str, isbn:str, message:str) -> None:
    """function creates class UserBooksResult
       :returns: None 
    """
    self._userId =userId	  
    self._isbn = isbn
    self._message = message

class MessageModal:
    
    def __init__(self,code:int, message:str) -> None:
       """function creates class MessageModal
       :returns: None 
          """
       self._code = code
       self._message = message

    @property
    def code(self):
        return self._code
class ReplaceIsbn:

    def __init__(self, userId:str, isbn:str) -> None:
       """function creates class ReplaceIsbn
         :returns: None 
       """
       self._userId =userId	  
       self._isbn = isbn

    @property
    def userId	(self):
        return self._userId
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

class BooksResult:
    
    def __init__(self,userId:str, message:str) -> None:
       """function creates class BooksResult
       :returns: None 
         """
       self._userId =userId	
       self._message = message


class StringObject:
    def __init__(self, isbn:str, userId:str) -> None:
       """function creates class StringObject
       :returns: None 
        """
       self._isbn = isbn
       self._userId =userId	 

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