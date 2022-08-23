
class BookModal():
     def __init__(self,isbn :str,title:str,subTitle:str,author:str,publish_date : str ,publisher:str,pages:int,description:str,website:str)  -> None:
         """function creates class BookModal
         :returns: None 
         """
         self._isbn	= isbn
         self._title =title     
         self._subTitle =	subTitle
         self._author	= author
         self._publish_date	= publish_date
         self._publisher= publisher
         self._pages	= pages
         self._description	= description      
         self._website = website

     @property
     def isbn(self):
         return self._isbn

     @property
     def title(self):
         return self._title
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

class AllBooksModal():
    def __init__(self,books:list)->None:
        """function creates class AllBooksModal
         :returns: None 
         """
        self._books = books


            


class GetUserResult:
    def __init__(self,userId:str, username:str,books:BookModal) -> None:
        """
           function creates class GetUserResult
           :returns: None 
        """
        self._userId	=userId
        self._username	=username
        self._books =books

    @property
    def books(self):
        return self._books
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

class CreateUserResult:
    def __init__(self,userID:str, username:str,books:list) -> None:
        """
           function creates class CreateUserResult
           :returns: None 
        """
        self._userID	=userID
        self._username	=username
        self._books =books

    @property
    def username(self):
        return self._username

    @property
    def userID(self):
        return self._userID



