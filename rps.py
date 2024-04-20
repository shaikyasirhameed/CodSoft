import random
import tkinter as tk

# Function to determine winner
def determine_winner(user1_choice, user2_choice):
    if user1_choice == user2_choice:
        return "It's a tie!"
    elif (user1_choice == 'rock' and user2_choice == 'scissors') or \
         (user1_choice == 'paper' and user2_choice == 'rock') or \
         (user1_choice == 'scissors' and user2_choice == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Function to handle player selections
def play_game():
    user1_choice = user1_var.get()
    user2_choice = user2_var.get()
    
    result = determine_winner(user1_choice, user2_choice)
    
    result_label.config(text=result)
    
    if result.startswith('Player 1'):
        user1_score_var.set(user1_score_var.get() + 1)
    elif result.startswith('Player 2'):
        user2_score_var.set(user2_score_var.get() + 1)

# Function to reset the game
def reset_game():
    user1_score_var.set(0)
    user2_score_var.set(0)
    user1_var.set("")
    user2_var.set("")
    result_label.config(text="")
    
# GUI
root = tk.Tk()
root.title("Rock Paper Scissors Game by YASIR")
root.configure(bg='#3498db')  # Background color

# Player 1
user1_label = tk.Label(root, text="Player 1:", fg='#ffffff', bg='#3498db')  # White text on blue background
user1_label.grid(row=0, column=0)
user1_var = tk.StringVar(root)
user1_choices = ['rock', 'paper', 'scissors']
user1_dropdown = tk.OptionMenu(root, user1_var, *user1_choices)
user1_dropdown.grid(row=0, column=1)

# Player 2
user2_label = tk.Label(root, text="Player 2:", fg='#ffffff', bg='#3498db')  # White text on blue background
user2_label.grid(row=1, column=0)
user2_var = tk.StringVar(root)
user2_dropdown = tk.OptionMenu(root, user2_var, *user1_choices)
user2_dropdown.grid(row=1, column=1)

# Play Button
play_button = tk.Button(root, text="Play", command=play_game, fg='#ffffff', bg='#27ae60', padx=10, pady=5)  # White text on green background with padding
play_button.grid(row=2, column=0, columnspan=2)

# Result Label
result_label = tk.Label(root, text="", fg='#ffffff', bg='#3498db', font=('Helvetica', 16))  # White text on blue background, larger font
result_label.grid(row=3, column=0, columnspan=2)

# Score Labels
user1_score_var = tk.IntVar(root)
user2_score_var = tk.IntVar(root)
user1_score_label = tk.Label(root, textvariable=user1_score_var, fg='#ffffff', bg='#3498db')  # White text on blue background
user1_score_label.grid(row=4, column=0)
user2_score_label = tk.Label(root, textvariable=user2_score_var, fg='#ffffff', bg='#3498db')  # White text on blue background
user2_score_label.grid(row=4, column=1)

# Reset Button
reset_button = tk.Button(root, text="Play Again", command=reset_game, fg='#ffffff', bg='#c0392b', padx=10, pady=5)  # White text on red background with padding
reset_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
