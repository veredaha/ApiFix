import json
import requests
import pytest
from models.bookmodel import AllBooksModal, BookModal,GetUserResult
from models.collectionofIsbn import AddListOfBooks,CollectionOfIsbn
from models.userbooksresult import ReplaceIsbn,MessageModal,StringObject,BooksResult,UserBooksResult




class BookStoreApi():

 def __init__(self, url:str,headers = {'accept': 'application/json'})-> None:
        """function creates class BookStoreApi
        :returns: None 
         """
        self._url = f"{url}Account/v1/"
        self._headers = headers
        self._session = requests.session()
        self._session.headers.update(self._headers)

 def get_books(self):
    """ get books
     :param: url -> str
     :returns: session
     """
    res = self._session.get(url=f"{self._url}Books")
    if res.status_code ==200:
            #books = res.json()
            #allbooks =[]
            #for b in books['books']:
             # allbooks.append(BookModal(**b))
            #return allbooks
            return res
    else:
            return None

 def post_book(self,book: BookModal) -> AddListOfBooks:
     """ post new book
     :param: book -> BookModal
     :returns: book
     """
     book_data = book.toJson()
     res = self._session.post(url=f"{self._url}Books", data=book_data)
     if res.status_code == 201:
            book = res.json()
            my_book = CollectionOfIsbn(**book)
            return my_book
     else:
            return None

 def delete_book(self,id)-> MessageModal:
     """ delete book
     :param: book -> str
     :returns: book
     """
     res = self._session.delete(url=f"{self._url}Books?UserId={id}" ,headers=self._headers)
     if res.status_code == 200:
            book = res.json()
            my_book = MessageModal(**book)
            return my_book
     else:
            return None
 
 def get_book_by_isbn(self,isbn:str)-> BookModal:
  """ get book by isbn
     :param: isbn -> str
     :returns: book ->BookModal
     """
  res = self._session.get(url=f"{self._url}Book?ISBN={isbn}",headers=self._headers)
  if res.status_code == 200:
            book = res.json()
            my_book = BookModal(**book)
            return my_book
  else:
            return None
  
 def delete_book_by_isbn(self,string:StringObject)-> MessageModal:
     """ delete book by isbn
     :param: isbn -> str
     :returns: book
     """
     string = string.toJson()
     res = self._session.delete(url=f"{self._url}Books" ,data =string,headers=self._headers)
     if res.status_code == 200:
            dele = res.json()
            my_dele = UserBooksResult(**dele)
            return my_dele
     else:
            return None
 def put_book(self,isbn:str,replace:ReplaceIsbn)-> BookModal:
     """ put book
     :param: isbn->str
     :param: replace-> ReplaceIsbn
     :returns: book
     """
     replace = replace.toJson()
     res = self._session.put(url=f"{self._url}Books/{isbn}" ,data=replace,headers=self._headers)
     if res.status_code == 200:
            new = res.json()
            newisbn = ReplaceIsbn(**new)
            return newisbn
     else:
            return None

