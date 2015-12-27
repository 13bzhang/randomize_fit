# Randomize Fit

Randomly Assigned Exercises Send to Your Email

This is a proof of concept for Randomize Fit, an app that alerts you daily to encourage you to exercise. You will be randomly assigned a certain number of minutes to exercise for that day. The Python script `email_script.py` will send you and/or other recipients an email alert.

# Directions for use

1. Fill in the necessary email information in the Python script.

2. Schedule the script to run at a set time daily so it can blast out some emails. You can use [crontab](https://docs.oracle.com/cd/E23824_01/html/821-1451/sysrescron-24589.html).

If you want to blast out the emails at 6 a.m. each day, add this to the end of your crontab file:

```
0 6 * * * python /whatever_directory/email_script.py
```
