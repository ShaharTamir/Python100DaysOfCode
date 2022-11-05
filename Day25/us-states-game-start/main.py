import turtle as tt
import pandas
from state import State

screen = tt.Screen()
screen.title("States Guess Game")

# set up background image
screen.bgpic("blank_states_img.gif")
screen.setup(700, 500)

# set up database
states_db = pandas.read_csv("50_states.csv")
all_states = states_db.state.to_list()
states_found = []
total_states = len(all_states)
game_run = True

while len(states_found) < total_states:
    user_guess = screen.textinput(title=f"{len(states_found)}/{total_states} States Correct",
                                  prompt="What's another states name?")
    if user_guess is not None:
        user_guess = user_guess.title()
        if user_guess == "Exit":
            break
        if user_guess in all_states:
            state_data = states_db[states_db.state == user_guess]
            new_state = State(state_data.x, state_data.y, user_guess)  # state_data.state.item()
            states_found.append(user_guess)
            all_states.remove(user_guess)

pandas.DataFrame({"states": all_states}).to_csv("states_to_learn.csv")

