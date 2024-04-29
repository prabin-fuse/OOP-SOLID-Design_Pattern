'''
Download the python file from this link. Suppose we have a NotificationService class that is responsible for sending notifications. The NotificationService class directly depends on the EmailSender class to send emails.
In this implementation, the NotificationService class directly depends on the EmailSender class, which violates the Dependency Inversion Principle. The high-level NotificationService should not depend on the low-level EmailSender, as it tightly couples the classes together.
Redesign this program to follow the  Dependency Inversion Principle (DIP) principle which represents that “Abstractions should not depend upon details. Details should depend upon abstractions.”
'''

from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient,message,subject=None):
        pass 

class EmailSender(MessageSender):
    def send_message(self, recipient, message, subject):
        print(f"Sending email to {recipient} : {subject} - {message}")

class NotificationService:
    def __init__(self, email_sender:EmailSender):
        self.email_sender = email_sender

    def send_notification(self, recipient, message, subject=None):
        self.email_sender.send_message(recipient, message, subject)

#Testing email:
email_sender = EmailSender()
notification_service = NotificationService(email_sender=email_sender)

notification_service.send_notification("prabin.bohara@fusemachines.com", "Hello Prabin! How are you doing", "Messsage Notification")