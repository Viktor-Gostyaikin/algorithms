with open('input.txt', 'r') as file:
	words = [sorted(line.strip()) for line in file]
with open('output.txt', 'a') as file_out:
    if words[0] == words[1]:
        file_out.write('1')
    else:
        file_out.write('0')