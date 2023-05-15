import re
class brackets:
    correct = ['(',')']
    def __init__(self,brack:str):

        self.brack=brack

    def correct_method(self):

        if ((self.correct[0] and self.correct[1]) in self.brack) is not True:
            raise Exception('В строке нет скобок.')

        else:
            """
            В первых 3 строках скобочная группа разбивается на тип данных Stack, отсчет ведется от [0] элемента списка.
            """
            list = re.split("",self.brack)
            list.pop(0)
            list.pop(-1)

            print((list))

            if list[0]==list[-1]:
                return False
            else:
                for i in range(1,len(list)):
                    print(i)
                    if list[i]==list[-i-1]:

                        return False
                    else:

                        continue
                return True

a='((())))'
obj=brackets(a)
print(obj.correct_method())