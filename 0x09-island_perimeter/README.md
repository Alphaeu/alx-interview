# Island Perimeter

## Project Description

The "Island Perimeter" project involves calculating the perimeter of an island represented in a 2D grid. The grid consists of 0s and 1s, where 0 represents water and 1 represents land. The cells in the grid are connected horizontally and vertically (not diagonally), and the grid is completely surrounded by water. The goal is to write a function that calculates the perimeter of the island in this grid.

## Requirements

- Python 3.4.3
- Your code should follow the PEP 8 style guide (version 1.7)
- No additional modules are allowed
- All files should be executable and end with a new line
- The first line of all Python files should be exactly `#!/usr/bin/python3`

## File Structure

- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: Contains the main function to test the implementation.
- `README.md`: This file, containing the project description and instructions.

## Function Specification

### `island_perimeter(grid)`

Calculates the perimeter of the island in the given grid.

#### Arguments:
- `grid` (list of list of int): A 2D list representing the grid, where 0 represents water and 1 represents land.

#### Returns:
- `int`: The perimeter of the island.

## Usage

To test the implementation, run the `0-main.py` script:

```bash
./0-main.py
```

### Example

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Expected output: 12
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x09-island_perimeter
   ```
3. Make the Python files executable:
   ```bash
   chmod +x *.py
   ```

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Derrick Alphaeus](https://github.com/Alphaeu)

---

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
