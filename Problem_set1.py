s = 'zsyuibdualrggcyqaum'
#Longest substring in alphabetical order is: beggh

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

all_sequences = []
longest_substring = []

s_letter = list(s)

for letter in s_letter:
    if len(longest_substring) == 0:
        longest_substring.append(letter)
    else:
        check_letter = longest_substring[-1]
        print check_letter, letter
        check_idx = alphabet.index(check_letter)
        print check_idx
        current_idx = alphabet.index(letter)
        if current_idx >= check_idx:
            longest_substring.append(letter)
        else:
            all_sequences.append(longest_substring)
            longest_substring = []


print all_sequences
max_length = float('-inf')
max_idx = 0
for idx in range(len(all_sequences)):
    current_length = len(all_sequences[idx])
    if current_length > max_length:
        max_lenght = current_length
        max_idx = idx

print(all_sequences[max_idx])

target_sequence = all_sequences[max_idx]

target_string = ''.join(target_sequence)
prior_idx = s.find(target_string) - 1
print s[prior_idx]

if alphabet.index(s[prior_idx]) < alphabet.index(target_string[0]):
    target_sequence[:0] = s[prior_idx]

final_string = ''.join(target_sequence)

print "Longest substring in alphabetical order is: " + final_string
