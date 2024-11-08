import sheep
import wolf
import json
import csv

sheep_list=[]
round_number=1
sheeps_alive = 15
file_json = open(r"pos.json", "w")
file_csv = open(r"alive.csv", "w", newline='')
writer = csv.writer(file_csv)

for i in range(sheeps_alive):
    sheep_list.append(sheep.Sheep(10.0, 0.5, i))
wolf = wolf.Wolf(10.0, 1.0)

while len(sheep_list) != 0 and round_number<=50:
    for sheep in sheep_list:
        sheep.move()

    sheeps_alive = wolf.move(sheep_list, sheeps_alive)
    #print(f"Round {round_number}, wolf position ({round(wolf.position_x,3)}, {round(wolf.position_y,3)}), alive sheeps: {sheeps_alive}")
    to_json={
        "round_no":round_number,
        "wolf_pos":[round(wolf.position_x,3),round(wolf.position_y,3)],
        "sheep_pos":([f"Sheep - id:{sheep.sheep_id} position ({'null' if sheep.position_x is None else sheep.position_x}, {'null' if sheep.position_y is None else sheep.position_y})"for sheep in sheep_list])
    }
    file_json.write(json.dumps(to_json, indent=3))
    writer.writerow([round_number,sheeps_alive])
    round_number+=1
file_json.close()
file_csv.close()


