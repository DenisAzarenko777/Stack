class Stack:

    def __init__(self):
        self.stack_list = list()

    def isEmpty(self):
        if self.stack_list == []:
            return 'False'
        else:
            return 'True'

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

if __name__ == "__main__":
    pass