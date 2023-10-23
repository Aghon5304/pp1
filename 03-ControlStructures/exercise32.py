computer_science_fan = input("Are you interested in computer science? (Y/N): ")
computer_games_fan = input("Do you like playing computer games? (Y/N): ")
instagram_account = input("Do you have an Instagram account? (Y/N): ")
if computer_science_fan =="Y" or computer_science_fan=='y':
    computer_science_fan="Yes"
else:
    computer_science_fan="No"
if computer_games_fan=="Y" or computer_games_fan =='y':
    computer_games_fan="Yes"
else:
    computer_games_fan="No"
    
if instagram_account=="Y" or instagram_account =='y':
    instagram_account="Yes"
else:
    instagram_account="No"
print(f"Interested in computer science: {computer_science_fan}\nPlaying computer games: {computer_games_fan}\nHas an Instagram account: {instagram_account}")