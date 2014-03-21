__author__ = 'Miten'

import imaplib
from HTMLParser import HTMLParser
from email.parser import Parser
import email
import BeautifulSoup

# user = raw_input("Username: ")
# password = raw_input("Password: ")

user = "miten@mitenpatel.com"
password = "goodbye2"

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user,password)
mail.list()

mail.select("inbox")

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
emails = {}

for id in id_list:
    id = int(id)
    if int(id) > 7410:

        result, data = mail.fetch(id, "(RFC822)")

# latest_email_id = id_list[-1]
# result, data = mail.fetch(latest_email_id, "(RFC822)")

        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        print email_message

        html = email_message
        soup = BeautifulSoup(str(html))
        print soup.prettify()
        parser = Parser()



        email = parser.parsestr(raw_email)

        print "From:    ", email.get('From')
        print "To:      ", email.get('To')
        print "Subject: ", email.get('Subject')




        if email.is_multipart():
            for payloads in email.get_payload():
            # if payload.is_multipart(): ...
                print "Body:    ", payloads.get_payload()
        else:
            print "Body:    ",email.get_payload()

        k = id
        v = raw_email

        emails[k] = v



# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data


parsed_emails = []

# for x in emails:


#     parser = MyHTMLParser()
#     parsed_emails.append(parser.feed(emails[x]))



