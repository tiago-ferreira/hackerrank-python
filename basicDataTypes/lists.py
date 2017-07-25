def read_commands(N):
    lines = list()
    for i in range(0, N):
        lines.append(raw_input())
    return lines

def execute_commands(lines):
    values = list()
    commands = list()
    for i in range(0, len(lines)):
        commands = lines[i].split( )
        command = commands[0]
        if(command == 'insert') :
            position = int(commands[1])
            value = int(commands[2])
            values.insert(position, value)
        if(command == 'print'):
            print values
        if(command == 'remove'):
            value = int(commands[1])
            values.remove(value)
        if(command == 'append'):
            value = int(commands[1])
            values.append(value)
        if(command == 'sort'):
            values.sort()
        if(command == 'pop'):
            values.pop()
        if(command == 'reverse'):
            values.reverse()

if __name__ == '__main__':
    N = int(raw_input())
    lines = read_commands(N)
    execute_commands(lines)