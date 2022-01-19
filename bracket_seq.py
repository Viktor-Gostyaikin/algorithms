def is_correct_bracket_seq(seq: str):
    bracket_open = 0
    bracket_close = 0
    bracket_open_sq = 0
    bracket_close_sq = 0
    bracket_open_fig = 0
    bracket_close_fig = 0
    for bracket in seq:
        if bracket == '(':
            bracket_open += 1
        elif bracket == ')':
            if bracket_open <= bracket_close:
                bracket_close += 1
                break
            bracket_close += 1
        elif bracket == '[':
            bracket_open_sq += 1
        elif bracket == ']':
            if bracket_open_sq <= bracket_close_sq:
                bracket_close_sq += 1
                break
            bracket_close_sq += 1
        elif bracket == '{':
            bracket_open_fig += 1
        elif bracket == '}':
            if bracket_open_fig <= bracket_close_fig:
                bracket_close_fig += 1
                break
            bracket_close_fig += 1
    if bracket_open == bracket_close and (
        bracket_open_sq == bracket_close_sq) and (
        bracket_open_fig == bracket_close_fig):
        return True
    return False


def main():
    with open('input.txt', 'r') as file:
        seq = (file.readline().strip())
    print(is_correct_bracket_seq(seq))

if __name__ == '__main__':
    main()