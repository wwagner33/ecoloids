# Ecoloids: Ecological Simulations

This project is a simplified version of SimCity designed for ecological simulations and ecoliteracy using agent-based modeling.

## Authors

- Wellington W. F. Sarmento
- Patrícia de Sousa Paula

## Project Structure

- `assets/`: Contains images and sounds used in the simulation.
- `data/`: Stores configuration files and map data.
- `src/`: Contains the source code for the simulation.
  - `agents/`: Contains agent classes (Citizen, Building, NatureElement).
  - `environment/`: Contains the grid and environment-related code.
  - `main.py`: The main entry point of the simulation.
  - `simulation.py`: Handles the simulation logic.
  - `utils.py`: Utility functions.

  ```bash
  ecoloids/
      ├── assets/
      │   ├── images/
      │   └── sounds/
      │
      ├── data/
      │   ├── config.json
      │   └── map_data.json
      │
      ├── src/
      │   ├── agents/
      │   │   ├── __init__.py
      │   │   ├── citizen.py
      │   │   ├── building.py
      │   │   └── nature_element.py
      │   │
      │   ├── environment/
      │   │   ├── __init__.py
      │   │   └── grid.py
      │   │
      │   ├── main.py
      │   ├── simulation.py
      │   └── utils.py
      │
      ├── requirements.txt
      └── README.md
    ```

## Requirements

- Python 3.x
- Pygame
- Numpy

## Installation

```bash
pip install -r requirements.txt
```

## Running Simulation

```bash
python src/main.py
```

