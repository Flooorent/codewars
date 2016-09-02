#!/usr/bin/python

def brainfuck(code, input):
    buff = []
    data = {}
    length_code = len(code)
    index_code = 0
    index_input = 0 
    data_pointer = 0

    while (index_code < length_code):
        c = code[index_code]

        if c == '>':
            data_pointer += 1
            index_code += 1
        elif c == '<':
            data_pointer -= 1
            index_code += 1
        elif c == '+':
            data[data_pointer] = (data.get(data_pointer, 0)+1) % 256
            index_code += 1
        elif c == '-':
            data[data_pointer] = (data.get(data_pointer, 0)-1) % 256
            index_code += 1
        elif c == '.':
            buff.append(chr(data.get(data_pointer, 0)))
            index_code += 1
        elif c == ",":
            data[data_pointer] = ord(input[index_input])
            index_code += 1
            index_input += 1
        elif c == '[':
            if data.get(data_pointer, 0) == 0:
                stack = ['[']
                next_index = index_code+1
                while len(stack) > 0:
                    if code[next_index] == ']':
                        stack.pop()
                    elif code[next_index] == '[':
                        stack.append('[')
                    next_index += 1
                index_code = next_index
            else:
                index_code += 1
        else:
            if data.get(data_pointer, 0) != 0:
                stack = [']']
                next_index = index_code-1
                while len(stack) > 0:
                    if code[next_index] == '[':
                        stack.pop()
                    elif code[next_index] == ']':
                        stack.append(']')
                    next_index -= 1
                index_code = next_index+2
            else:
                index_code += 1

    return ''.join(buff)
