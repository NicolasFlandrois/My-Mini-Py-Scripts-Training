#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Mon 17 May 2021 17:54:20 CEST
# Author: Nicolas Flandrois
# Last updated by: Nicolas Flandrois
# Last updated date: Mon 17 May 2021 17:54:20 CEST
# Description: How to convert back and forth base64 to/from string
import base64


# Converting a Base64 String, into a Human-Readable String (Here a URL)
# Ascii Version
msg_cntr = 'QWxlYSBKYWN0YSBFc3QgIQ=='

b64_str = msg_cntr.encode('ascii')
b64_bytes = base64.b64decode(b64_str)
decode_str = b64_bytes.decode('ascii')
print("The bytes string (base64, before):\t", msg_cntr,
      "\nBase 64 URL (after):\t", decode_str)

# UTF-8 Version
msg_cntr = 'VmVuaSBWZWRpIFZpY2kgIQ=='

b64_str = msg_cntr.encode('utf-8')
b64_bytes = base64.b64decode(b64_str)
decode_str = b64_bytes.decode('utf-8')
print("The bytes string (base64, before):\t", msg_cntr,
      "\nBase 64 URL (after):\t", decode_str)


# Convert a Human-Readable String into a Base 64 string
my_string = "Hello World !"
my_base64_str = base64.b64encode(bytes(my_string, 'utf-8')).decode('utf-8')

print("The initial string (before):\t", my_string,
      "\nBase 64 str (after):\t", my_base64_str)
