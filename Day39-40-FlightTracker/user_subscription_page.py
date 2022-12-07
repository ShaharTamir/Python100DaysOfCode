from user_data import UserData
from data_manager import DataManager

if __name__ == "__main__":
    print("Welcome to the flight club subscription! Please enter your details:")
    user = UserData(
        input("first name: \n").title(),
        input("last name: \n").title(),
        input("email: \n").lower()
    )
    data_manager = DataManager()
    data_manager.get_subscribers()
    if data_manager.add_subscriber(user):
        print("user added successfully")
    else:
        print("User already subscribed")