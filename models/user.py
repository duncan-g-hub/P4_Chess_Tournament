import json

from models.constances import DATA_DIR


class User:
    def __init__(self, last_name, first_name, birth_date, user_id, score=None):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.user_id = user_id
        self.score = score

    def add_user(self):
        user = {"last_name": self.last_name, "first_name": self.first_name, "birth_date": self.birth_date, "user_id": self.user_id}
        if not self.control_users():
            self.save_user(user)
            return True
        else:
            return False

    def control_users(self):
        users = load_users()
        for user in users:
            if user["user_id"] == self.user_id:
                return True
        return False


    def save_user(self, user):
        users = load_users()
        users.append(user)
        with open(f"{DATA_DIR}/users.json", "w") as file:
            json.dump(users, file, indent=4)


    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.birth_date} - {self.user_id}"

    def __repr__(self):
        return self.__str__()

def load_users():
    users = None
    while users is None :
        try :
            with open(f"{DATA_DIR}/users.json", "r") as file:
                users = json.load(file)
                return users
        except json.decoder.JSONDecodeError or FileNotFoundError:
            with open(f"{DATA_DIR}/users.json", "w") as file:
                json.dump([], file)



if __name__ == '__main__':
    jean = User("Morel","Jean", "18 Novembre 2001", "AB12345" )
    jean.add_user()

    paul = User("Durand","Paul", "13 Septembre 1988", "AB12346" )
    paul.add_user()