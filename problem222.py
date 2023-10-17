#!/usr/bin/env python3

import sys

count = int(sys.argv[1]) 
if count < 0:
	message = "Negative"
	print(message)

elif count > 0:
	message = "Positive"
	print(message)
	if count < 50:
		message = "smaller than 50"
		print(message)
		if count%2 == 0:
			print("it is an even number that is smaller than 50")
else:
        message = "must be 0"
        print(message)
