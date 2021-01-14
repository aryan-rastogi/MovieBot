# MovieBot by Aryan Rastogi
A discord bot with various utilities, including choosing a movie

Available Commands:

!FlipCoin - Flips a coin and outputs heads or tails

!RollDie - Rolls a die and outputs a number from 1 to 6

!Enhance <username>
  - Returns the profile picture of the member whos name is specified by <username> 
    and sends it as a message
  - If left blank, it will send the profile picture of the sender of the message

!GetMovie <genre> 
  - If given a valid genre, will output the name of one of the top 50 movies of
    that genre on IMDB
  - If left blank, it will send the name of one of the top 50 movies across all genres

!GetGenres
  - Outputs a list of all available genres
  
This bot uses many APIs and packages including:
  - Discord API
  - Requests
  - Beautiful Soup 4
