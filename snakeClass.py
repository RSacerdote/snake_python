class Snake():
    auto_mode = False
    def __init__(self, initial_length = 2, pos = (0,0)):
        self.head = pos
        self.body = [pos]
        for i in range(initial_length-1):
            self.body.append((pos[0], pos[1]+1))

    def show(self, grid, tail = None):
        if tail is not None:
            grid[tail[0]][tail[1]] = 0
        
        for part in self.body:
            grid[part[0]][part[1]] = -1
        return grid

    def tryToEat(self, grid):
        if grid[self.head[0]][self.head[1]] == 1:
            return True
        else:
            return False

    def move(self, grid):
        self.checkForCollision() # check futuro
        
        # Adicionar cabeca na direcao do movimento

        ate = self.tryToEat(grid) 

        if ate:
            tail = None
        else:
            tail = self.removeTail()
        
        self.show(grid, tail)
        pass

    def checkForCollision(self, grid):
        pass

    def removeTail(self):
        return self.body.pop()