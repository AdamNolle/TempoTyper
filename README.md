# TempoTyper
Keyboard Typing Rhythm Game for Capstone I

# TempoTyper Rules
This game has some similarities with Guitar Hero and Dance Dance Revolution. Players start by choosing a song. Then during the actual gameplay, letters will come up from the bottom of the screen and players are expected to type them once they reach their respective hitbox (which should coincide with the beat of the song). There are 8 hitboxes to show the recommended finger to use to type the given letter. There is also a multiplier if the player types enough letters correct in a row. At the end, the score along with total correct and incorrect letters will appear and the player can choose a new song or quit.

# Capstone I Work
#### COMPLETE
- Basic frontend
- Menu to allow players to choose from multiple songs
  - Stars to show level difficulty of song
  - Three songs and difficulties to choose from
- Have song playing while player is typing
  - Point multiplier if user gets multiple correct in a row
  - Game knows when player presses each key and how close it was to the correct timing
  - Letters have different colored backgrounds depending which keyboard row they are on
- Allow player to select a new song once the current one is done
- More songs can be added if new respective .mp3 and .txt files are added to the codebase

# Ideas for the future
### Relatively Simple
- Reset multiplier after unnecessary key presses
- Add more songs with varying difficulty levels
- Better looking frontend
- Short tutorial to explain how the game works
- Better scoring depending how close to the actual hitbox the player typed
### Complex
- Leaderboard
- Database to remember which songs players have unlocked, their previous high scores, etc.
- Add settings, perhaps with the ability to speed up/slow down songs
- Add specific setting that lets players choose which keys they want to practice
