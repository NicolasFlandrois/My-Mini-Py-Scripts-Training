import re
def is_valid_IP_re(strng):
    """
    IPv4 Validator. (RegEx Version)
    Given a string, this function verify and validate if it's in IPv4 format.
    An IPv4 is four octets, with values between 0 and 255, inclusive.
    No 0 padding
    Numerical Positif or equal 0 (Not Alphabet upper nor lower cases)
    No space
    Not None
    No special caracters ' -!:;,§/?*ù%µ$£^+=)°]ç_è-('"é&]@^\\`|[{#~¹²'
    """
    if(re.match("(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$", strng)   != None):
        return True
    else:
        return False


print('\nTesting IP Regex')
print(is_valid_IP_re('12.255.56.1')     == True )
print(is_valid_IP_re('')                == False)
print(is_valid_IP_re('abc.def.ghi.jkl') == False)
print(is_valid_IP_re('123.456.789.0')   == False)
print(is_valid_IP_re('12.34.56')        == False)
print(is_valid_IP_re('12.34.56 .1')     == False)
print(is_valid_IP_re('12.34.56.-1')     == False)
print(is_valid_IP_re('123.045.067.089') == False)
print(is_valid_IP_re('127.1.1.0')       == True )
print(is_valid_IP_re('0.0.0.0')         == True )
print(is_valid_IP_re('0.34.82.53')      == True )
print(is_valid_IP_re('192.168.1.300')   == False)
print(is_valid_IP_re('    ')            == False)

# OR

def is_valid_IP(strng):
    """
    IPv4 Validator.
    Given a string, this function verify and validate if it's in IPv4 format.
    An IPv4 is four octets, with values between 0 and 255, inclusive.
    No 0 padding
    Numerical Positif or equal 0 (Not Alphabet upper nor lower cases)
    No space
    Not None
    No special caracters ' -!:;,§/?*ù%µ$£^+=)°]ç_è-('"é&]@^\\`|[{#~¹²'
    This version (albeit not a regex) raises an exception if the string
    starts with a space.
    """
    try:
        if strng.startswith(' '):
            raise
        elif strng.endswith(' '):
            raise
        else:
            lst = strng.split('.')
            length = len(lst)
            string = ''.join(lst)
            integer = int(string)
            if length is 4:

                if int(lst[0]) not in range(0, 256) :
                    raise
                elif len(lst[0]) > 1 and lst[0].startswith('0'):
                    raise
                elif int(lst[1]) not in range(0, 256):
                    raise
                elif len(lst[1]) > 1 and lst[1].startswith('0'):
                    raise
                elif int(lst[2]) not in range(0, 256):
                    raise
                elif len(lst[2]) > 1 and lst[2].startswith('0'):
                    raise
                elif int(lst[3]) not in range(0, 256):
                    raise
                elif len(lst[3]) > 1 and lst[3].startswith('0'):
                    raise
                else:
                    return True

            else:
                raise
    except:
        return False




print('\nTesting IP (Non regex Version)')
print(is_valid_IP('12.255.56.1')     == True )
print(is_valid_IP('')                == False)
print(is_valid_IP('abc.def.ghi.jkl') == False)
print(is_valid_IP('123.456.789.0')   == False)
print(is_valid_IP('12.34.56')        == False)
print(is_valid_IP('12.34.56 .1')     == False)
print(is_valid_IP('12.34.56.-1')     == False)
print(is_valid_IP('123.045.067.089') == False)
print(is_valid_IP('127.1.1.0')       == True )
print(is_valid_IP('0.0.0.0')         == True )
print(is_valid_IP('0.34.82.53')      == True )
print(is_valid_IP('192.168.1.300')   == False)
print(is_valid_IP('    ')            == False)
