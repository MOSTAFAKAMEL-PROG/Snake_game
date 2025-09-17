from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=self.high_score()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_scoreboard()
    def high_score(self):
        with open("myscore.txt","r+") as file:
           return int(file.read())
    def save_highscore(self):
        with open("myscore.txt","w") as file:
            file.write(str(self.highscore))
    def update_scoreboard(self):
        self.write(f"Score : {self.score}   high score : {self.highscore}", align="center",font=("Arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore=self.score
            self.save_highscore()
        self.write(f"-----Game over-----\n\nFinal score: {self.score}\nHigh score : {self.highscore}",align="center",font=("Arial",24,"normal"))
        