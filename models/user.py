
class User():
    def __init__(self,id : int, username:str,firstName:str,lastName:str,email:str,password:str,phone :str, userStatus:int) -> None:
        """function creates class User
         :returns: None 
         """
        self._id = id	
        self._username = username
        self._firstName = firstName
        self._lastName	= lastName
        self._email	=email
        self._password	= password 
        self._phone	= phone
        self._userStatus = userStatus

    @property
    def username(self):
        return self._username

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