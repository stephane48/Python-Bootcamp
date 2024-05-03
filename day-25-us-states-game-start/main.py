import turtle, pandas, csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.shape()

continue_playing = True
correct_answer = []
count = 0
good_answer = 0

data = pandas.read_csv("50_states.csv")

while len(correct_answer) < 50:
    answer_state = (screen.textinput(title=f"{good_answer}/50 States Correct",
                                     prompt="What's another state's name")).title()

    if answer_state == "Exit":
        missing_states = [state for state in data["state"].to_list() if state not in correct_answer]
        # for state in data["state"].to_list():
        #     if state not in correct_answer:
        #         missing_states.append(state)

        # Create a DataFrame with the missing states
        missing_states_df = pandas.DataFrame({"missing_states": missing_states})

        # Save the missing states to a CSV file
        missing_states_df.to_csv("state_to_learn.csv", index=False)
        break

    if answer_state in data["state"].to_list():
        # Create a turtle object
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()

        #Find the coordinates of the state
        state_row = data[data["state"] == answer_state] #this will pull out a row
        x = int(state_row["x"])
        y = int(state_row["y"])

        #Move user answer to the coordinate and write the state name
        tim.goto(x, y)
        tim.write(answer_state, align="center", font=("Arial", 8, "normal"))

        #Record the correct guesses in a list
        correct_answer.append(answer_state)

        #Keep track of the score
        good_answer += 1



