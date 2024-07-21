# Shape Area Calculator


## Project Overview:
The Shape Area Calculator is a Python program that allows users to calculate the area of different geometric shapes, including rectangles, circles, and triangles. This README provides comprehensive details about the project, its functionality, and how to use it.

## Features:
1. **Rectangle Area Calculation**: Enter the length and width to get the area.
2. **Circle Area Calculation**: Provide the radius for the circle's area.
3. **Triangle Area Calculation**: Input the base and height for triangle area computation.

## How to Run:
1. Ensure you have Python installed.
2. Install required dependencies: `pip install -r requirements.txt`
3. Run the main function: `python project.py`

## Testing:
To ensure the accuracy of area calculations, we have included test functions using `pytest` in `test_project.py`. Run tests with: `pytest test_project.py`

## User Interaction:
The program prompts users to choose a shape and input the required dimensions. It then displays the calculated area.

## Notes:
- The program approximates the value of pi as 3.14 for simplicity.
- Feel free to extend the project with additional shapes or features.
- Contributions and feedback are welcome!

## Future Improvements:
This project can be enhanced by incorporating more shapes, handling user input validation, and improving the precision of mathematical constants.

## Acknowledgments:
Thanks to the CS50 Python course for inspiration and learning opportunities.

## Detailed Documentation:
### Rectangle Area Calculation:
The function `calculate_rectangle(length, width)` takes the length and width as parameters and returns the area.

### Circle Area Calculation:
The function `calculate_circle(radius)` takes the radius as a parameter and returns the area.

### Triangle Area Calculation:
The function `calculate_triangle(base, height)` takes the base and height as parameters and returns the area.
