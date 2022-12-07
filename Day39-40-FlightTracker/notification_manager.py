import smtplib
from flight_data import FlightData
from user_data import UserData


class NotificationManager:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def alert_flight(self, flight_details: FlightData, to_user: UserData):
        with smtplib.SMTP("smtp.gmail.com") as email_connection:
            email_connection.starttls()
            email_connection.login(user=self.email, password=self.password)
            header = f"From: {self.email}\nTo: {to_user.email}\nSubject: Low price alert!\n\n"
            msg = header + f"""Hello {to_user.name} {to_user.last_name}
Did you catch this new deal?
Only ${flight_details.price} to fly from TLV to 
{flight_details.city}-{flight_details.code},\nfrom {flight_details.date_from} to {flight_details.date_to}

{flight_details.link}"""
            email_connection.sendmail(from_addr=self.email, to_addrs=to_user.email, msg=msg)
