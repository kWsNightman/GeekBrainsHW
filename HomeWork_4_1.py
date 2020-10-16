from sys import argv

path, hours, rate_hour, prize = argv
print(round(float(hours)*float(rate_hour)+float(prize), 3))
