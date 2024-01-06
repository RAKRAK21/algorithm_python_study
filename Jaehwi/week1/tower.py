tower_num = int(input())
tower_height = list(map(int, input().split()))

for idx in range(0, len(tower_height)):
    if idx == 0:
        print(0, end=" ")
        continue
    
    for comp in range(idx-1, -1, -1):
        if tower_height[idx] <= tower_height[comp]:
            print(comp+1, end=" ")
            break
        
        if comp == 0:
            print(0, end=" ")




# for idx in range(len(tower_height)-1, 0, -1):
#     flag = True
#     for comp in range(idx-1, -1, -1):
#         if tower_height[comp] >= tower_height[idx]:
#             tower_height[idx] = comp+1
#             flag = False
#             break
#     if flag == True:
#         tower_height[idx] = 0

# tower_height[0] = 0

# for val in tower_height:
#     print(val, end=" ")