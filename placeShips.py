
 
 
def placeShips( width, height):    #self,
   
   #определяем количество ячеек занятых клетками кораблей
   num_cells_ship = width * height // 5;
   if width * height % 5 > 0:
      num_cells_ship += 1;

   #Собираем клетки кораблей в корабли. Согласно классическому виду игры - это пирамида, где колличество одиночных кораблей
   #равно длине самого крупного корабля
   ships = {}
   i, size= 1, 0;
   while True :
      size += i;
      if num_cells_ship < size: 
         break;      
      num_cells_ship -= size ;      
      i += 1;

   #Собираем начальную пирамидку кораблей
   for j in range(i-1):
      ships.update({ j+1 : i-j-1 });

   #Сортируем оставшиеся клетки кораблей не уложившиеся в классическую пирамиду
   if num_cells_ship >= i  and (num_cells_ship > size//2):
      num_cells_ship -= i;
      ships.update({ i : 1 });

   for j in range(i-1):
      if num_cells_ship >= i-j-1:
         num_cells_ship -= i-j-1;
         ships[i-j-1] += 1;

   print(ships)
 
 

placeShips(10, 10);