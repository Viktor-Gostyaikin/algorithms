true_line = 0
counter_line = 0
counter_array = 0
with open('input.txt', 'r') as file_in:
    # итерация по строкам
    n = int(file_in.readline().strip())
    for line in file_in:
        if counter_array > n:
            break
        else:
            counter_array += 1
            try:
                if int(line) == 1:
                    counter_line += 1
                    if counter_line > true_line:
                        true_line += 1
                else:
                    counter_line = 0
            except:
                pass

with open('output.txt', 'a') as file_out:
	file_out.write(str(true_line))