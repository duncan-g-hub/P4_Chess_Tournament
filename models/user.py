import json
from models.constances import DATA_DIR


class User:
    def __init__(self, lastname, firstname, birthdate, user_id, score=None):
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.user_id = user_id
        self.score = score

    def add_user(self):
        user = {"lastname": self.lastname, "firstname": self.firstname, "birthdate": self.birthdate, "user_id": self.user_id}
        if not self.control_users():
            self.save_user(user)
            return True
        else:
            return False

    def control_users(self):
        users = self.load_users()
        for user in users:
            if user["user_id"] == self.user_id:
                return True
        return False


    def save_user(self, user):
        users = self.load_users()
        users.append(user)
        with open(f"{DATA_DIR}/users.json", "w") as file:
            json.dump(users, file, indent=4)


    def load_users(self):
        users = None

        while users is None :
            try :
                with open(f"{DATA_DIR}/users.json", "r") as file:
                    users = json.load(file)
                    return users
            except json.decoder.JSONDecodeError or FileNotFoundError:
                with open(f"{DATA_DIR}/users.json", "w") as file:
                    json.dump([], file)





    def __str__(self):
        return f"{self.lastname} {self.firstname} - {self.birthdate} - {self.user_id}"

    def __repr__(self):
        return self.__str__()



if __name__ == '__main__':
    jean = User("Morel","Jean", "18 Novembre 2001", "AB12345" )
    jean.add_user()

    paul = User("Durand","Paul", "13 Septembre 1988", "AB12346" )
    paul.add_user()