import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "!@#$%^&*()."

string = lower + upper + numbers + symbol
length =8
password = "".join(random.sample(string,length))

print("Your new password is:" + password)