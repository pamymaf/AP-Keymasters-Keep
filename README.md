# Keymaster's Keep Games
My game implementations for Archipelago Keymaster's Keep.

Currently includes I Was A Teenage Exocolonist (contains spoilers) and OLDTV.

## APworld download
https://github.com/SerpentAI/Archipelago/releases/tag/kmk-0002

## What is Keymaster's Keep?
(Taken from release page linked above)

Keymaster's Keep is a dynamic, multi-game objective / challenge generator that seamlessly integrates with a thematic Archipelago randomizer. In other words, you have a typical Archipelago randomizer with goals, finite locations, progression items, logic etc. and Keymaster's Keep will generate and associate unique game challenges with each location. The APWorld features a plugin system to add games independently from releases, as well as a dedicated client to assist with the exploration and challenges of Keymaster's Keep.

When you play Keymaster's Keep...

  - You will generate a new keep with distinct areas
  - A few of these areas will be unlocked from the start
  - The rest will be locked and will require combinations of magic keys to unlock
  - These magic keys are scattered throughout the multiworld
  - Once an area is unlocked, a set of trials for a specific game will be revealed
  - For each trial you complete, you will manually check it off in the client and that will correspond to a location check
  - Your goal will either be to collect enough artifacts of resolve to unlock a final challenge to beat or to escape the keep with a certain number of magic keys in hand.

## Instructions
(Taken from Serpent.AI's discord post in AP's main discord)

- After installing the APWorld, the next time you start the Archipelago Launcher, a keymasters_keep directory will be added to your Archipelago installation.,
- To register a game implementation, add its Python file (e.g. cuphead_game.py) to that keymasters_keep directory. You can add multiple games at once,
- Close the Archipelago Launcher if it's still open (important!) and relaunch it,
- Click Generate Template Options,
- Voila! You will now have a YAML template that includes that game implementation,
- Templates will have to be regenerated every time you add new game implementations.,

Note: Game implementations are only required to generate YAML templates or an Archipelago seed. If a game has already been generated for you, you don't need the Python files to play.