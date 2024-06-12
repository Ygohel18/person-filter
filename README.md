## Single Person Image Filter

This Python script processes images in a selected folder to identify and move images that do not contain a single clearly visible person to a subfolder named 'tmp'. This script uses AI models for face detection.

### Features

- Select a folder containing images.
- Identify images with a single clearly visible person using Mediapipe.
- Move images not meeting the criteria to a 'tmp' subfolder.
- Concurrent processing of images using threading for improved performance.

### Requirements

- Python 3.6+
- opencv-python-headless
- mediapipe
- tk
- numpy

### Installation

#### Ubuntu

1. Install Python:
   sudo apt update
   sudo apt install python3 python3-pip python3-venv -y

2. Clone the repository:
   git clone https://github.com/ygohel18/person-filter
   cd person-filter

3. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the script:
   python main.py

#### Windows

1. Install Python:
   Download and install Python from the official website (https://www.python.org/downloads/).

2. Clone the repository:
   git clone https://github.com/ygohel18/person-filter
   cd person-filter

3. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the script:
   python main.py

### Usage

1. Run the script using the steps mentioned above.
2. A dialog will appear to select the folder containing the images.
3. The script will process each image in the folder:
   - Images containing a single clearly visible person will remain in the original folder.
   - Images not meeting the criteria will be moved to a 'tmp' subfolder within the selected folder.

### Contact

For support, please contact:

- Email: [me@yashgohel.com](mailto:me@yashgohel.com)  
- Instagram: [@ygohel18](https://instagram.com/ygohel18)  
- LinkedIn: [@ygohel18](https://linkedin.com/in/ygohel18)


### Credits

This script was created with the help of ChatGPT.
