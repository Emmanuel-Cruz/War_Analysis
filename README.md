# War_Analysis
Taking the novice card game of war and analyzing it in games of 2 vs 3+. Analysis in terms of turns until winner, or if there ever is a winner at certain levels! 

BASICALLY:
  In war the deck of cards is split into equal parts. The player(s) then put the first card in the deck face up, and whoever has the highest card value wins the pot of cards played, and this is repeated until a player runs out of cards. Normally 10-15 minute game but I am wanting to prove it!
  Conclusions so far...
    - War is not always a terminal game assuming a deck of perfectly shuffled cards.
    - There is a possibility that a game will last forever, games with more players tend to end faster for one player until there are 2         players left, then it takes forever.
  
  
TODO:::
  Tie mechanism mostly functional, but only for games of 2. Games of 3+ require more attention to detail.
  Working on a bug where a tie can sometimes raise the number of cards in a deck
  Working on better telling the program how to handle lost players (who ran out of cards during different points of the game)
  Working on statistical analysis
    Regression/Prediction/Time taken to win
