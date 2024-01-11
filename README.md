# FIR Analysis System

The FIR Analysis System is a web application built using Flask that allows users to analyze First Information Reports (FIRs) through natural language processing (NLP) techniques.

## Features

- Process text inputs and images to recommend IPC sections
- Supports multiple languages, with initial focus on Hindi.
- Ensures compliance with legal and regulatory requirements.
- Web interface for user interaction.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ykp-kgp/fir-analysis-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fir-analysis-system
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter text or upload an image to analyze FIR information.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.

