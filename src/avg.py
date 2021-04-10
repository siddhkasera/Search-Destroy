# board1 = [22620,20682,2169, 2881,1449,2063,2543,153,247,866]
# board2 = [21938, 514,2794,17438,3096,605,298,351,1406,256]
# board3 = []

# array of averages for each 10 boards
basic1 = [16456.4, 989.3, 1763.3, 6803.3, 916.4, 1211.8, 1500.6, 1775.8, 40601.2, 18026.7]
basic2 = [12182.4, 3295.3, 1280.9, 2402.0, 1377.3, 1019.6, 7027.7, 1462.9, 2694.2, 1178.7]
improved_agent = [10080.9, 10926.3, 10284.2, 7892.6, 4274.0, 9263.7, 9205.4, 8203.1, 7647.9, 9295.2]

sum_1 = 0
sum_2 = 0
sum_imp = 0
for i in range(len(basic1)):
    sum_1 = sum_1 + basic1[i]

avg_1 = sum_1 / len(basic1)
print("Average for basic agent 1", avg_1)

for i in range(len(basic2)):
    sum_2 = sum_2 + basic2[i]

avg_2 = sum_2 / len(basic2)
print("Average for basic agent 2", avg_2)

for i in range(len(improved_agent)):
    sum_imp = sum_imp + improved_agent[i]

avg_imp = sum_imp / len(improved_agent)
print("Average for improved agent", avg_imp)
