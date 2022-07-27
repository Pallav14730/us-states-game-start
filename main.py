import turtle
import pandas
screen = turtle.Screen()
screen.title("Map Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# print(answer_state)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
# print(state_list)
guessed_state = []
while len(guessed_state) < 50:
    answer_state = turtle.textinput(title="Guess the Game", prompt="What's another state name ?")

    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()