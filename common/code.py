import random


def __random_str(start, end):
    return chr(random.randint(start, end))


def new_code_str(len):

    code_str= ''
    for _ in range(len):
        flag = random.randint(0, 2)
        start, end = (ord('a'), ord('z')) if flag == 0 \
            else (ord('A'), ord('Z')) if flag == 1 \
            else (ord('0'), ord('9'))
        code_str += __random_str(start, end)
    return code_str

if __name__ == '__main__':
    print(new_code_str(6))