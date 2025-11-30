class Fone:
    def __init__(self, id: str, number: str):
        self.__id=id
        self.__number=number

    def isValid(self) -> bool:
        p="0123456789()."
        return all (c in p for c in  self.__number)
    
    def get_id(self):
        return self.__id
    
    def get_number(self):
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, name: str=""):
        self.__name=name
        self.__fav=False
        self.__fone=[]
    
    def addFone(self, id:str, number:str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fone.append(fone)
            return
        print("fail: invalid number")
    
    def rmFone(self, index:str):
        try:
            self.__fone.pop(index)
        except: 
            print("fail: indice invalido")

    def toogleFavorited(self):
        self.__fav = not self.__fav

    def __str__(self):
        flag="@" if self.__fav else "-"
        return f"{flag} {self.__name} [" + ", ".join(str(c) for c in self.__fone)+"]"

    def isFavorited(self):
        return self.__fav
    
def main():
    contact = Contact()

    while True:
        line = input()
        args = line.split(" ")
        print("$"+line)
        
        if args[0]=="end":
            break

        elif args[0]=="init":
            contact=Contact(args[1])
        
        elif args[0]=="add":
            contact.addFone(args[1], args[2])
        elif args[0]=="show":
            print(contact)

        elif args[0]=="rm":
            contact.rmFone(int(args[1]))

        elif args[0]=="tfav":
            contact.toogleFavorited()

main()