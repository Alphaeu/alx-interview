# Prime Game

## Overview

The Prime Game is a competitive game played between two players, Maria and Ben. Given a set of consecutive integers starting from 1 up to and including `n`, players take turns choosing a prime number from the set and removing that number and its multiples. Maria always goes first. The player who cannot make a move loses the game. The goal of this project is to determine the winner of each game round based on optimal play by both players.

## Requirements

- **Editors Allowed**: vi, vim, emacs
- **Environment**: The code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- **Style**: The code should adhere to PEP 8 style guidelines (version 1.7.x)
- **Executables**: All files must be executable

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/alx-interview.git
   ```
2. Navigate to the project directory:
   ```sh
   cd alx-interview/0x0A-primegame
   ```

## Usage

1. Ensure the script is executable:
   ```sh
   chmod +x 0-prime_game.py
   ```
2. Run the script:
   ```sh
   ./0-prime_game.py
   ```

## Function Description

### `isWinner(x, nums)`

Determines the winner of each game round.

- **Parameters**:
  - `x` (int): The number of rounds.
  - `nums` (list of int): An array of `n` values representing the set of consecutive integers for each round.
  
- **Returns**:
  - `str`: The name of the player that won the most rounds ("Maria" or "Ben").
  - `None`: If the winner cannot be determined.

### Example

```python
from 0-prime_game import isWinner

print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
# Output: Winner: Ben
```

## Algorithm

The solution employs the following key algorithms and techniques:

1. **Sieve of Eratosthenes**: To efficiently find all prime numbers up to a given limit.
2. **Game Simulation**: To simulate each game round based on the precomputed prime numbers.
3. **Optimal Play**: Both players play optimally to determine the winner of each round.

## Files

- `0-prime_game.py`: Contains the main logic for determining the winner of the Prime Game.
- `README.md`: This file, providing an overview and instructions for the project.

## License

This project is licensed under the MIT License.

---

B
B
A
By understanding prime numbers, game theory, and algorithm optimization, this project effectively determines the winner of a competitive game scenario. The provided solution is efficient and adheres to the specified requirements.
