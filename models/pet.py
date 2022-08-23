
from enum import Enum


class Pet():

    def __init__(self, id, name, category=None, photoUrls=None, tags=None, status=None)-> None:
        """function creates class Pet
         :returns: None 
         """
        self._photo_urls = None
        self._tags = None
        self._status = None
        self._id = id
        self._name = name
        self._category = category
        if photoUrls is not None:
            self._photo_urls = photoUrls
        if tags is not None:
            self._tags = tags
        if status is not None:
            Status[status]
            self._status = status

    @property
    def photoUrls(self):
        return self._photoUrls

    @property
    def name(self):
        return self._name


    @property
    def status(self):
        return self._status

    @property
    def tags(self):
        return self._tags

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


class Status(Enum):
    available = "available"
    pending = "pending"
    sold = "sold"

class Tag():
    def __init__(self,id = None, name = None) -> None:
        """function creates class Tag
         :returns: None 
         """
        self._id = None
        self._name = None
        if id is not None:
            self._id = id
        if name is not None:
            self._name = name

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

class Category():

    def __init__(self, id=None, name=None):
        """function creates class Category
         :returns: None 
         """

        self._id = None
        self._name = None
        if id is not None:
            self._id = id
        if name is not None:
            self._name = name


