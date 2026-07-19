stack_list = [23, 22, 12, 34]
stack_list.append(20)

print(stack_list)

stack_list.pop()

print(stack_list)

print('stack peek', stack_list[-1])

if(len(stack_list) == 0):
    print('Stack Empty')
else:
    print("stack not empty")