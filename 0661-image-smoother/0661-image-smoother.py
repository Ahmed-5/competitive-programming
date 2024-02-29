class Solution:
    def smooth_index(self, img, x, y):
        r = len(img)
        c = len(img[0])
        vs = [img[x][y]]
        
        if y+1<c:
            vs.append(img[x][y+1])
        if y-1>=0:
            vs.append(img[x][y-1])
        
        if x+1<r:
            vs.append(img[x+1][y])
            if y+1<c:
                vs.append(img[x+1][y+1])
            if y-1>=0:
                vs.append(img[x+1][y-1])
        
        if x-1>=0:
            vs.append(img[x-1][y])
            if y+1<c:
                vs.append(img[x-1][y+1])
            if y-1>=0:
                vs.append(img[x-1][y-1])
                
        return int((sum(vs)/len(vs))//1)
        
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        r = len(img)
        c = len(img[0])
        
        smooth = []
        
        for i in range(r):
            smooth.append([])
            for j in range(c):
                smooth[i].append(self.smooth_index(img, i, j))
                
        return smooth