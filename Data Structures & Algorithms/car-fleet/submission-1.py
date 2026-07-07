class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = zip(*sorted(zip(position, speed), reverse = True))
        base_time = (target - position[0])/speed[0]
        fleet_count = 1
        for i in range(1, len(position)):
            time = (target - position[i])/speed[i]
            if time > base_time:
                base_time = time
                fleet_count+=1
        return fleet_count



        


