from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.updt()

    def updt(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", move=False, align="center",
                   font=("courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.updt()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new = open("data.txt", mode="w")
            new.write(str(self.high_score))
        self.score = 0
        self.updt()
