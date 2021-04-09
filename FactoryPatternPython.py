from __future__ import annotations
from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self) -> str:
        pass

class WebButton(Button):
    def click(self)->str:
        return "Returns new web button click"

class MobileButton(Button):
    def click(self) -> str:
        return "Returns new mobile button click"

class Dialog(ABC):

    @abstractmethod
    def factoryMethod(self):
        pass

    def someoperation(self)->str:
        b=self.factoryMethod()
        return f"{b.click()}"

class WebDialog(Dialog):

    def factoryMethod(self) -> Button:
        return WebButton()

class MobileDialog(Dialog):

    def factoryMethod(self)->Button:
          return MobileButton()

def callingClient(dialog:Dialog)-> None:
    print(str(dialog.someoperation()))

if __name__=="__main__":
    #calling concrete class 1
    webDialog = callingClient(WebDialog())
    #calling concrete class 2
    mobileDialog = callingClient(MobileDialog())