from mpmath import mp

mp.dps = 100000  # Precision is 100,000 decimal places
pi_str = str(mp.pi)[2:]  # Get the decimal part of π

sequence_1 = '999999'
sequence_2 = '888888'
sequence_3 = '000000'
sequence_4 = pi_str[:6]
sequence_5 = '1234567'  # phone number

positions = {
    sequence_1: pi_str.find(sequence_1),
    sequence_2: pi_str.find(sequence_2),
    sequence_3: pi_str.find(sequence_3),
    sequence_4: pi_str.find(sequence_4),
    sequence_5: pi_str.find(sequence_5)
}

print("Position of sequence '999999':", positions[sequence_1])
print("Position of sequence '888888':", positions[sequence_2])
print("Position of sequence '000000':", positions[sequence_3])
print("Position of first six digits:", positions[sequence_4])
print("Position of first seven digits of phone number:", positions[sequence_5])