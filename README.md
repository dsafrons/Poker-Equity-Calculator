# Poker Odds (Python)

A Python program to calculate, simulate, and visualize poker hand odds.  
The code is written in an **object-oriented, Java-esque style**, with dedicated classes for cards, hands, scoring, and visualization.

## Features

- **Object-Oriented Design**  
  - `Card` and `Hole` classes to represent individual cards and player hands  
  - `Score` / `ScoreHelper` for evaluating hand strength  
  - `PokerGame` for simulating multi-player games  
- **Odds Calculation**  
  - Evaluates possible hands using combinations of hole cards and table cards  
  - Supports ranking and scoring of poker hands  
- **Visualization (PyGame)**  
  - GUI display of cards using sprites (`visual.py`)  
  - Adjustable to different table setups  
- **Testing Utilities**  
  - `Test` class with a `timeit` decorator for benchmarking and performance checks  

## Requirements

- Python 3.8+
- [pygame](https://pypi.org/project/pygame/)

Install dependencies:
```
pip install pygame
```

## Project Structure
```
Poker-Odds-Tree/
├── main.py         # PokerGame class: builds deck, simulates dealing and odds
├── cards.py        # Card and Hole classes with values, suits, num_value mapping
├── scoring.py      # ScoreHelper: evaluation utilities (flushes, pairs, etc.)
├── visual.py       # PyGame visualization for table and cards
├── tests.py        # Test harness with performance timer
├── README.md
└── .idea/          # IDE config (can be ignored)
```

## How It Works

**1. Deck & Hands**

- The deck is generated as 52 `Card` objects (values Ace-King × 4 suits).
- Each player receives a `Hole` hand.

**2. Scoring**

- `ScoreHelper` combines player hole cards and community table cards.
- Provides utilities to filter by suit, rank values, and detect combinations.
- Used by `Score` to classify hands (pairs, straights, flushes, etc.).

**3. Visualization**

- `visual.py` initializes a PyGame window, loads card images, and displays the table.

**4. Testing & Performance**

- `tests.py` includes a `timeit` decorator to measure runtime of simulations.

## Future Improvements

- Enhance the game with betting, chips, and multiple players
- Monte Carlo simulations for exact odds percentages
- Integration with external data for large-scale analysis
