
from models.pet import Pet
from models.pet import Status
import json
import requests



class petApi():

    def __init__(self, url:str, headers={'accept': 'application/json'})-> None:
        """function creates class petApi
         :returns: None 
         """
        self.url = f"{url}"
        self.headrs = headers
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def update_pet(self,pet:Pet)->Pet:
        """ update pet
        :param:pet->Pet
        :returns: pet
         """
        my_pet = pet.toJson()
        res = requests.put(url=f"{self.url}pet", json=my_pet)
        if res.status_code == 200:
            my_pet = Pet(**res.json())
            return my_pet
        else:
            return None
        
    def post_new_pet(self,pet:Pet )->Pet:
        """ add new pet
        :param:pet->Pet
          :returns: pet
        """
        pet_data = pet.toJson()
        res = self.session.post(url=f"{self.url}pet", data=pet_data)
        if res.status_code == 200:
            my_pet = Pet(**res.json())
            return my_pet
        else:
            return None

    def get_pet_by_status(self, status:Status) -> list:
        """ get pet by status
        :param: stataus->Status
          :returns: pet
          """
        res = self.session.get(url=f"{self.url}pet/findByStatus?status={Status[status].value}")
        result = [] 
        if res.status_code == 200:
         pets = res.json()
         for a in pets:
            result.append(pet)
         return result 
        else:
            return None
    
    def get_pet_by_tags(self, tags) -> list:
        """ get pet by tags
     :returns: pet
     """
        res = self.session.get(url=f"{self.url}pet/findByTags?tags={tags}")
        result=[]
        if res.status_code == 200:
         pets = res.json()
         for a in pets:
            result.append(pet)
         return result 
        else:
            return None

    def get_pet_by_id(self,pet_id : int)->Pet:
        """ get pet by id
        :param: pet_id->int
        :returns: pet
        """
        res = self.session.get(url=f"{self.url}pet/{pet_id}")
        if res.status_code == 200:
            my_pet = Pet(**res.json())
            return my_pet  
        else:
            return None


    def update_with_form_data(self ,pet:Pet,petid:int, petname:str, petstatus:str)->Pet:
        """ update pet
        :param: pet->Pet
        :param: pet_id->int
        :param: petname->str
        :param: petstatus->str
        :returns: pet
        """
        pet_data = pet.toJson()
        res = self.session.post(url=f"{self.url}pet/{petid}?name={petname}&status={petstatus}", data=pet_data)
        if res.status_code == 200:
            my_pet = Pet(**res.json())
            return my_pet
        else:
            return None

    def delete_pet(self,petid:int)->Pet:
        """ delete pet
     :param:oetid->id
     :returns: pet
     """
        res = self.session.delete(url=f"{self.url}pet/{petid}")
        return res
            
    def upload_image(self,image:str,petid:int)->Pet:
        """ upload image
        :param: image->str
        :param:petid->int
        :returns: pet
     """
        res = self.session.post(url=f"{self.url}pet/{petid}/uploadImage", data=image)
        if res.status_code == 200:
            my_pet = Pet(**res.json())
            return my_pet
        else:
            return None


url = "https://petstore3.swagger.io/api/v3"
headrs ={'accept': 'application/json'}
api = petApi(url,headrs)
pet = Pet(10, 'vv', None, None ,None,None)  
image = '/tmp/inflector7440998430605450804.tmp'
r = api.upload_image('@87fc90b8adc99582eb71d99a6b0c33b46935.jpg',10)
#@87fc90b8adc99582eb71d99a6b0c33b46935.jpg
print(r)
