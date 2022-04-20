chars = "1234567890!@#$%^&*()qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]\{}|;:,./<>?"
import random

charlen = int(input("How long do you want your chars to be: "))

final = ""

for _ in range(charlen):
	rand = chars[random.randint(1, len(chars))]
	final = f"{final}{rand}"

print(final)
