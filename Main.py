from Stack_building import Stack

if __name__ == "__main__":
    s = Stack()
    balance_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    T = True
    while T:
#for stroke in balance_list:
        stroke = str(input("Введите строку: "))
        if stroke == 'exit':
            T = False
        else:

            for element in stroke:

                if element == "(":
                    s.push(element)
                if element == '[':
                    s.push(element)
                if element == '{':
                    s.push(element)

                if element == ')':
                    if (s.size() > 0 and s.peek() == '('):
                        s.pop()
                    else:
                        s.push(element)
                        break
                if element == ']':
                    if (s.size() > 0 and s.peek() == '['):
                        s.pop()
                    else:
                        s.push(element)
                        break
                if element == '}':
                    if (s.size() > 0 and s.peek() == '{'):
                        s.pop()
                    else:
                        s.push(element)
                        break

            if s.size() > 0:
                print("False")
            if s.size() == 0:
                print("True")