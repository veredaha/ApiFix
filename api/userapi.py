from urllib import response
from models.user import User
from models.order import Order
from models.order import Status

import json
import requests



class userApi():

    def __init__(self, url:str,headrs={'accept': 'application/json'})-> None:
        """function creates class userApi
         :returns: None 
         """
        self.url = f"{url}"
        self.headrs = headrs
        self.session = requests.session()
        self.session.headers.update(self.headrs)



    def create_user(self,user:User)->User: 
        """
        create new user
        :param:user->User
        :return:User
        """
        user_data = user.toJson()
        res = self.session.post(url=f"{self.url}user", data=user_data)
        if res.status_code == 200:
            my_user = User(**res.json())
            return my_user
        else:
            return None

    def create_users_with_list(self,users:list)->User: 
        """
        create users with list
        :param:user->User
        :return:User
        """
        res = self.session.post(url=f"{self.url}user/createWithList", data=users)
        if res.status_code == 200:
            my_users = User(**res.json())
            return my_users
        else:
            return None

    def login_user(self,username:str,password:str)->response:
        """
        loging in
        :param:username->str
        :param:password->str
        :return:response
        """
        res = self.session.get(url=f"{self.url}user/login?{username}=theUser&password={password}")
        if res.status_code == 200:
            return res.text
        else:
            return None

    def log_out(self)->response:
     """
     logging out
     :return:response
        """
     res = self.session.get(url=f"{self.url}user/logout")
     if res.status_code == 200:
         return res.text
     else:
         return None

    def get_user_by_name(self,username:str)->User:
     """
        get user by name
        :param:username->str
        :return:User
        """
     res = self.session.get(url=f"{self.url}user/{username}")
     if res.status_code == 200:
            my_user = User(**res.json())
            return my_user 
     else:
            return None


    def update_user(self,user,username):
        """
        update user
        :paramuser->User
        :param:username->str
        :return:User
        """
        my_user = user.toJson()
        res = requests.put(url=f"{self.url}user/{username}", data=my_user)
        if res.status_code == 200:
            my_user = User(**res.json())
            return my_user
        else:
            return None
           
           
    def delete_order_by_name(self,name:str)->response:
        """
     delete user by name
     :return:response
        """
        res = self.session.delete(url=f"{self.url}user/{name}")
        return res

