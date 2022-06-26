# -*- coding: utf-8 -*-
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class ClientData:

     def __init__(self):
         self._name = ""
         self._email =""
       
     def get_name(self):
         return self._name
       
     def set_name(self, a):
         self._name = a

     def del_name(self):
         del self._name
         
     def get_email(self):
         return self._email
       
     def set_email(self, a):
         self._email = a

     def del_email(self):
         del self._email
     
     name = property(get_name, set_name, del_name)
     email = property(get_email, set_email, del_email)
    
class ServerSubject(ABC):
    """
    The ServerSubject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, client: Client) -> None:
        """
        Attach an clinet to the server.
        """
        pass

    @abstractmethod
    def detach(self, client: Client) -> None:
        """
        Detach an clinet from the server.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all clients about an event.
        """
        pass


class Server(ServerSubject):
    """
    The Server receive some clientData from user and notifies clients.
    """
    Cdata = ClientData()

        
    _clients: List[Client] = []


    def attach(self, client: Client) -> None:
        print("Server: Attached an client.")
        self._clients.append(client)

    def detach(self, client: Client) -> None:
        self._clients.remove(client)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Server Notifying clients...")
        for client in self._clients:
            client.update(self)

    def run(self) -> None:
        import re

        while True:
            a = input("Enter a Name: ")
            self.Cdata.name = a
            if len(self.Cdata.name) < 4:
                print("Make sure your Name is at lest 4 letters")
                continue
            elif ' ' in self.Cdata.name:
                self.Cdata.name = self.Cdata.name.replace(" ", "_")
    
            self.Cdata.email = input("Enter a Emailid: ")
            
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            
            if(re.fullmatch(regex, self.Cdata.email)):
                print("Valid Email")
                break
            else:
                print("Invalid Email")

        self.notify()


class Client(ABC):
    """
    The Client interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: ServerSubject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Clients react to the updates issued by the Server they had been
attached to.
"""


class ClientA(Client):
    def update(self, subject: ServerSubject) -> None:
          print("ClientA: Reacted to the event: ", subject.Cdata.name, subject.Cdata.email )


class ClientB(Client):
    def update(self, subject: ServerSubject) -> None:
         print("ClientB: Reacted to the event: ",subject.Cdata.name, subject.Cdata.email)


if __name__ == "__main__":
    # The client code.

    subject = Server()

    observer_a = ClientA()
    subject.attach(observer_a)

    observer_b = ClientB()
    subject.attach(observer_b)

    subject.run()

