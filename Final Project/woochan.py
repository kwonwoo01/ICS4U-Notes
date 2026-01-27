from snake import Snake

class woochan(Snake):
    def __init__(self):
        start_x, start_y = (1, 1)

        color = (255, 0, 0)   
        name = "woochan"

        length = 150
        attack = 10
        hp = 40

        super().__init__(start_x, start_y, color, name, length, attack, hp)

    def _getPosition(self) -> tuple[int, int]:
        x, y, _ = self.body_positions[0]
        return (x, y)

    def _checkCollision(self, direction: list[int, int]) -> bool:
        x, y = self._getPosition()
        nx = x + direction[0]
        ny = y + direction[1]

        max_x, max_y = self.matrix_size()

        return nx < 0 or nx >= max_x or ny < 0 or ny >= max_y

    def move(self) -> list[int, int]:
        x, y = self._getPosition()
        max_x, max_y = self.matrix_size()

        
        if x == 0 and y < max_y - 1:
            direction = [0, 1]

       
        elif y == max_y - 1 and x < max_x - 1:
            direction = [1, 0]

    
        elif x == max_x - 1 and y > 0:
            direction = [0, -1]

    
        elif y == 0 and x > 0:
            direction = [-1, 0]

        else:
            direction = [-1, 0]

        return super().move(direction)

   
    def detect(self, map):
        pass