import sheep
import wolf
sheep_list=[]
for i in range(1, 6):
    sheep_list.append(sheep.Sheep(10.0, 0.5, i))
wolf = wolf.Wolf(10.0, 1.0)

while len(sheep_list) != 0 and wolf.find_closest_sheep(sheep_list)[1]<100:
    for sheep in sheep_list:
        sheep.move()
        #print(sheep.log())
    wolf.move(sheep_list)
    #print(wolf.log())

