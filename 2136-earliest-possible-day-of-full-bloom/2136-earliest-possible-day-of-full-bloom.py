class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_and_grow_time = [(a,b) for a,b in zip(plantTime,growTime)]
        plant_and_grow_time = sorted(plant_and_grow_time,key = lambda x:-x[1])
        result = [0 for i in range(len(plantTime))]
        total_plant_time = sum(plantTime) + plant_and_grow_time[-1][1]
        remaining_day = total_plant_time
        additional_time = [0]
        for i in range(len(plant_and_grow_time)-1):
            current = plant_and_grow_time[i][1]
            remaining_day -= plant_and_grow_time[i][0]
            if current > remaining_day:
                additional_time.append(current-remaining_day)
        return max(additional_time)+total_plant_time 
                
        