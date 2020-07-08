from typing import List

class Solution():
    def numRescueBoats(self,people: List[int],limit: int) -> int:
        people.sort()
        ini =0
        fim = len(people)-1
        boats_num =0

        while (ini<=fim):
            if ini == fim:
                boats_num+=1
                break
            if people[ini]+people[fim]<=limit:
                ini += 1
            fim -= 1
            boats_num += 1
        return boats_num

if __name__=="__main__":

    teste =  Solution()
    print(teste.numRescueBoats([1,1,1,2,2,3],3))