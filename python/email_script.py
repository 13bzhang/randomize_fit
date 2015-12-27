#!/usr/bin/env python

import smtplib
import random
 
# set up server info
server = smtplib.SMTP("STMP ADDRESS", PORT_NUMBER)
server.starttls()
server.login("SENDER EMAIL ADDRESS", "EMAIL PASSWORD")

# randomize minutes of exercise
minutes_excercise = random.choice([0, 15, 30, 45, 60])

# compose message
if minutes_excercise > 0:
	subject_text = "Exercise for " + str(minutes_excercise) + " Minutes Today!"
	msg_text = "Good morning! Please excercise for " + str(minutes_excercise) + \
	" minutes today. Thank you for using Randomize Fit."
else:
	subject_text = "Take the Day Off!"
	msg_text = "Good morning! You don't have to exercise today." \
	" Enjoy your day off! Thank you for using Randomize Fit."

message = "Subject: %s\n\n%s" % (subject_text, msg_text)

recipients = ["EMAIL OF RECIPIENTS"]

# send email
server.sendmail("SENDER EMAIL ADDRESS", recipients, message)
server.quit()