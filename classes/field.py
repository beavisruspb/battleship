class Field:

    cells = None

    ships = None

    def makeField(self, width, height, cells = []):

        field = dict()

        #Приватная служебная функция для правильного составления буквенных индексов
        #Возвращает list стрингов
        def __getWidhtIndex(width):

            from string import ascii_lowercase
            import itertools

            ss = list()

            #ваще не понимаю как это работает
            def iter_all_strings():
                for size in itertools.count(1):
                    for s in itertools.product(ascii_lowercase, repeat=size):
                        yield "".join(s)


            for s in iter_all_strings():
                ss.append(s)
                if len(ss) == width:
                    break
            return ss

        #если адресов ячеек не передали и свойство cells объекта так же пустое то возвращает пустое игровое поле
        if self.cells == [] or cells == []:
            for a in __getWidhtIndex(width):
                bb = list()
                for b in range(1, height+1):
                    bb.append("cell_link_"+str(b))
                field.update( { a : bb } )

        return field


if __name__ == "__main__":
    print ( Field.makeField(63,2) )