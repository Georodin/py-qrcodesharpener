# QR Code Analyzer and Recreator

This Python application allows you to analyze a QR code image and recreate it as either a high-resolution PNG or SVG file. By scanning each cell's center pixel, the program determines whether it’s black or white, then generates a clean, high-quality version of the QR code in your chosen output format.

## Features

- Load an existing QR code image to analyze.
- Set QR code dimensions (number of rows and columns).
- Choose output format: `PNG` or `SVG`.
- Generate a clean, high-resolution QR code based on analysis.

## Requirements

Before running this application, ensure you have the following installed:

- Python 3.6 or higher
- [Pillow](https://python-pillow.org/) (for image processing)
- [svgwrite](https://pypi.org/project/svgwrite/) (for SVG generation)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (for the GUI, typically included with Python installations)

### Install the Dependencies

Use `pip` to install the required packages:

```bash
pip install pillow svgwrite
```

`tkinter` is typically included with Python. If you’re on Linux and don’t have it, install `tkinter` using your package manager (e.g., `sudo apt-get install python3-tk`).

## Usage

1. **Run the script**:
    ```bash
    python QrCodeSharpener.py
    ```
   
2. **Use the GUI**:
   - Select an input QR code image file.
   - Set the QR code grid dimensions (rows and columns).
   - Choose the output format (`PNG` or `SVG`).
   - Click on "Start Conversion" to generate the recreated QR code.

The recreated QR code will be saved as either `recreated_qr_code.png` or `recreated_qr_code.svg` in the working directory.

## Example

Here's a basic example of how the application works:
1. The user selects a QR code image and enters grid dimensions (e.g., 33 x 33).
2. The script processes the image, analyzing each cell's color.
3. The recreated QR code is saved in the selected format and displayed in the console.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

---

**Happy coding!**
