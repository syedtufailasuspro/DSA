class Solution:
    def trap(self, hei: List[int]) -> int:
        hei.append(0)
        space = []
        for i in range(1,len(hei)):
            if hei[i]>0 and hei[i-1] - hei[i] > 0:
                space.append(hei[i-1])
            elif hei[i] == 0 and space !=[]:
                space.append(hei[i-1])
            elif hei[i]>0 and hei[i-1] - hei[i] <0 and space !=[]:
                space.append(hei[i-1])
        print(space)
