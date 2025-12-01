class Fone:
    def __init__(self, id:str, number: str):
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
        self.__fones=[]
    
    def addFone(self, id: str, number:str):
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
            return
        
        print("fail: invalid number")

    def rmFone(self, index:int):
        try:
            self.__fones.pop(index)
        
        except:
            print("fail: indice invalido")

    def toggleFavorited(self):
        self.__fav = not self.__fav

    def __str__(self):
        flag="@" if self.__fav else "-"
        return f"{flag} {self.__name} [" + ", ".join(str(c) for c in self.__fones)+"]"
        

    def isFavorited(self):
        return self.__fav
    
    def getName(self):
        return self.__name
    
    def getFones(self):
        return self.__fones
    
    def setName(self, name:str):
        self.__name=name
    
class Agenda:
    def __init__(self):
        self.__contacts={}

    def addContact(self, name:str, fones:list):
        if name not in self.__contacts:
            self.__contacts[name] = Contact(name)
            
        contact = self.__contacts[name]

        for id_, num in fones:
            contact.addFone(id_, num)
    
    def rmContact(self, name:str):
        if name in self.__contacts:
            del self.__contacts[name]
        else:
            print("fail: contato nao existe")

    def favorite(self, name: str):
        if name in self.__contacts:
            self.__contacts[name].toggleFavorited()
        else:
            print("fail: contato nao existe")

    def getContact(self, name:str):
        return self.__contacts.get(name, None)

    def getFavorites(self):
        return [c for c in self.__contacts.values() if c.isFavorited()]
    
    def search(self, pattern):
        res = []
        for contact in self.__contacts.values():
            if pattern in str(contact):
                res.append(contact)
        return sorted(res, key=lambda c: c.getName())
    
    def __str__(self):
        contatos_ord = sorted(self.__contacts.values(), key=lambda c: c.getName())
        return "\n".join(str(c) for c in contatos_ord)
    


def main():
    agenda=Agenda()

    while True:
        line = input()
        args = line.split()
        print("$"+line)

        if args[0]=="end":
            break

        elif args[0]=="show":
            print(agenda)

        elif args[0]=="add":
            name=args[1]
            fones=[]
            for f in args[2:]:
                id_, num =f.split(":")
                fones.append((id_, num))
            agenda.addContact(name, fones)
        
        elif args[0]=="rm":
            agenda.rmContact(args[1])

        elif args[0]=="rmFone":
            name=args[1]
            index=int(args[2])
            contact=agenda.getContact(name)
            if contact:
                contact.rmFone(index)
            else:
                print("fail: contato nao existe")

        elif args[0]=="fav":
            name = args[1]
            contact = agenda.getContact(name)
            if contact:
                contact.toggleFavorited()
            else:
                print("fail: contato nao existe")

        elif args[0]=="search":
            pattern = args[1]
            results = agenda.search(pattern)
            for c in results:
                print(c)
        
        elif args[0] == "showFav":
            for c in agenda.getFavorites():
                print(c)
        

main()