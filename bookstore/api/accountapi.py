import json
import requests
import pytest  
from models.tokenviewmodel import LoginViewModel,TokenViewModel
from models.bookmodel import BookModal, CreateUserResult,GetUserResult
from models.userbooksresult import MessageModal



def bearer_auth_session()->requests:
     """ bearer authontication
     :param: url -> str
     :returns: session
     """
     User ={ "userName": "veredaharonov",
                "password": "12345@Aa"}
     hader = {'accept': 'application/json'}
     res = requests.post( 'https://bookstore.toolsqa.com/Account/v1/GenerateToken' ,data=User,headers=hader)
     my_token = res.json()["token"]
     session = requests.session()
     session.headers.update(hader)
     session.headers.update({'Authorization': f'Bearer {my_token}'})
     return session
    

class accountApi():

    def __init__(self, url : str, headers = {'accept': 'application/json'})-> None:
        """function creates class accountApi
         :returns: None 
         """
        self._url = f"{url}Account/v1/"
        self._headers = headers
        self._session = requests.session()
        self._session.headers.update(self._headers)

    
   
    def post_account_authorize(self, account:LoginViewModel)-> bool:
        """ post account and authorize
        :param: account -> TokenViewModel
        :returns: bool
         """
        account_data = account.toJson()
        res = self._session.post(url=f"{self._url}Authorized", data=account_data, headers=self._headers)
        if res.status_code == 200:
         return res.json()
        else:
            return None
   

    def post_account_generatetoken(self, account:LoginViewModel)-> TokenViewModel:
        """ 
         post account and generates token
         :param: account -> TokenViewModel
         :returns: TokenViewModel
        """
  
        account_data = account.toJson()

        res = self._session.post(url=f"{self._url}GenerateToken", data=account_data, headers=self._headers)
        if res.status_code == 200:
         my_token = res.json()["token"]
         self._session.headers.update(self._headers)
         self._session.headers.update({'Authorization': f'Bearer {my_token}'})
         account = TokenViewModel(**res.json())
         return account
        else:
            return None

    def post_account_user(self, account:LoginViewModel)->CreateUserResult:
        """
        post new account
        :param: account -> TokenViewModel
        :returns: CreateUserResult
        """
        account_data = account.toJson()
        res = self._session.post(url=f"{self._url}User", data=account_data, headers=self._headers)
        if res.status_code == 201:
         account = CreateUserResult(**res.json())
         return account
        else:
            return None
    
    def delete_account_by_id(self,id:str)->MessageModal:
        """ delete account by id
        :param:id ->str
        :returns: status_code
         """
        res = self._session.delete(url=f"{self._url}User/{id}", headers=self._headers)
        if res.status_code == 200:
            user = res.json()
            my_user = MessageModal(**user)
            print(my_user)
            return my_user 
        else:
            return None
            

    def get_account_by_id(self,id:str)->GetUserResult:
        """ get account by id
        :param:id ->str
        :returns: status_code
        """
        res = self._session.get(url=f"{self._url}/User/{id}")
        if res.status_code == 200:
            user = res.json()
            my_user = GetUserResult(**user)
            return my_user 
        else:
            return None


