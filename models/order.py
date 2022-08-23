from enum import Enum
class Status(Enum):
    placed= "placed"
    approved = "approved"
    delivered = "delivered"
class Order():
    def __init__(self,id:int,petId :int,quantity:int,shipDate:str,status : Status, complete : bool) -> None:
        
        """function creates class Order
         :returns: None 
         """
        self._id = id
        self._petId = petId
        self._quantity = quantity
        self._shipDate =shipDate
        self._status = status
        self._complete = complete
        
    @property
    def id(self):
        return self._id

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

