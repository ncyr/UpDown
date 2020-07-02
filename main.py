import os, datetime, time, requests

# Create a secure SSL context
HOSTNAME = input('Enter Hostname: ')
LOCATION = input('Enter Location: ')
MAILTO = input('Enter Mailto Email: ')
SIZE = input('Enter byte size: ')
message = "HOST: " + HOSTNAME + " is down @ " + LOCATION
#use something like mailgun or sendgrind
def send_simple_message():
	return requests.post(
		"YOUR-SMTP-ADDRESS",
		auth=("api", "YOUR-KEY-HERE"),
		data={"from": "SYSTEM DOWN <you@whatever.com>",
			"to": [MAILTO],
			"subject": HOSTNAME + "@" + LOCATION + " WENT DOWN",
			"text": message })

while True:
    response = str(os.system("ping -n 1 -l " + SIZE + " " +HOSTNAME))
    #and then check the response...
    if response == str(0):
        print(HOSTNAME, 'is up!')
        time.sleep(1)
    else:
        print(HOSTNAME, 'is down!')
        # Try to log in to server and send email
        send_simple_message()
        time.sleep(1)

