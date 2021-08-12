from my.classes import MyCell, MyShip

#функция для стрельбы по множеству ячеек разом.
def multi_hit(cells):

    for cell in cells:
        print("\nПульнем по {}".format(cell))
        cell.check()
        print("Плывем дальше?: {}".format(cell.ship.setLiveStatus()))

def main():
    #создаем ячейки игрового поля
    a1 = MyCell()
    a2 = MyCell()
    a3 = MyCell()

    #создаем корабли определяя список ячеек для корабля
    ship1 = MyShip([a1, a2, a3])
    print("\nВот такой получился корабик:\n", vars(ship1), "\nНу и что, что текстовый. Зато {} палубный\n".format(len(ship1.cells)))

    #когда от количества принтов стало рябить в глазах, решил что проще функцию написать для стрельбы по множеству ячеек разом.
    multi_hit([a1, a2, a3])

    #таким образом коробль оживить нельзя ведь ячейки уже битые
    #необходимо либо оживить ячейки, либо указать нестреляные
    #ship1.__init__([a2, a1, a3])
    #print(vars(ship1))

if __name__ == "__main__":
    main()