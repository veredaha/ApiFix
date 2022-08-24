from urllib import response
from models.pet import Pet
from models.order import Order
from models.order import Status

import json
import requests



class storeApi():

    def __init__(self, url:str,headrs={'accept': 'application/json'})-> None:
        """function creates class storeApi
         :returns: None 
         """
        self.url = f"{url}"
        self.headrs = headrs
        self.session = requests.session()
        self.session.headers.update(self.headrs)


    def get_inventory(self)-> list:
        """ get inventory
        :returns: list
         """
        res = self.session.get(url=f"{self.url}store/inventory")
        if res.status_code == 200:
         return res.status_code
        else:
            return None

    def place_order(self,order:Order)->Order:
        """ place order
        :param:oreder->Order
        :returns: order
          """
        order_data = order.toJson()
        res = self.session.post(url=f"{self.url}store/order", data=order_data)
        if res.status_code == 200:
            ord = Order(**res.json())
            return ord
        else:
            return None

    def get_purchase_by_id(self, order_id:int)->Order:
        """ get purchase by id
        :param:oreder->Order
        :returns: order
          """
        res = self.session.get(url=f"{self.url}store/order/{order_id}")
        print(res)
        if res.status_code == 200:
            my_order = Order(**res.json())
            return my_order
        else:
            return None

    def delete_order_by_id(self,order_id:int)->response:
        """ delete order by id
        :param:order_id->int
        :returns: order
          """
        res = self.session.delete(url=f"{self.url}store/order/{order_id}")
        return res




