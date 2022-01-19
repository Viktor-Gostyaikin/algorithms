counter_array = 0
last_num = None
true_line = ''
with open('input.txt', 'r') as file_in:
    n = int(file_in.readline().strip())
    with open('output.txt', 'a') as file_out:
        # file_out.write(str(true_line))
        for line in file_in:
            if counter_array > n:
                break
            else:
                counter_array += 1
                try:
                    current_num = int(line)
                    if current_num != last_num:
                        last_num = current_num
                        file_out.write(str(current_num)+'\n')
                except:
                    pass
                