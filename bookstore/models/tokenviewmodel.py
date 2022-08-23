
class TokenViewModel:
    def __init__(self,token:str,expires:str,status:str,result:str) -> None:
        """function creates class TokenViewModel
         :returns: None 
         """
        self._token	= token
        self._expires= expires   
        self._status = status
        self._result = result

    @property
    def result(self):
        return self._result
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


class LoginViewModel:
    def __init__(self,userName:str,password:str) -> None:
        """function ceates class LoginViewModel
         :returns: None 
         """
        self._userName = userName
        self._password = password

    @property
    def userName(self):
        return self._userName
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