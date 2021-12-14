import random
from collections import defaultdict

FLAG = "1T5-4LW4Y5-M0R53-C0D3"

MORSE_CODE_ASCII = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ',':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-'}
ASCII_MORSE_CODE = {v:k for k, v in MORSE_CODE_ASCII.items()}
MORSE_CODE_LEDS = {k:[2 if a == '-' else (1 if a == '.' else 0) for a in v] for k, v in MORSE_CODE_ASCII.items()}

def land(b1, b2):
    return int(b1 == 1 and b1 == b2)

def nand(b1, b2):
    return int(not land(b1, b2))

def circuit(bits):
    left = land(nand(bits[0], bits[1]), nand(bits[2], bits[4]))
    right = land(left, bits[3])
    return left + right

def encode(flag: str) -> str:
    flag_morse_code = []

    for c in FLAG:
        flag_morse_code += MORSE_CODE_LEDS[c]
        flag_morse_code.append(0)

    encoding = defaultdict(list)

    for i in range(26):
        bits = [int(b) for b in "{0:05b}".format(i)]
        val = circuit(bits)
        encoding[val].append(chr(ord("A") + i))

    flag_encoded = []

    for b in flag_morse_code:
        flag_encoded.append(random.choice(encoding[b]))

    return ''.join(flag_encoded)

def decode(message: str) -> str:
    decoding = {}

    for i in range(26):
        bits = [int(b) for b in "{0:05b}".format(i)]
        val = circuit(bits)
        decoding[chr(ord("A") + i)] = val

    flag = ""
    buffer = []
    for c in message:
        if decoding[c] == 0:
            flag += ASCII_MORSE_CODE[''.join(buffer)]
            buffer = []
        else:
            buffer.append('-' if decoding[c] == 2 else '.')
    
    return flag

if __name__ == "__main__":
    encoded_flag = encode(FLAG)
    print("Message:", encoded_flag)
    decoded_flag = decode(encoded_flag)
    print("Check:", FLAG == decoded_flag)
