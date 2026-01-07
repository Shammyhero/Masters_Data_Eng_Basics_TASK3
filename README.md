# Word Count Project

This project contains a Python script (`word_count.py`) to perform word counting operations on text data and a sample CSV file (`data/test.csv`) for testing.

## Files

- `word_count.py`: A Python script that processes text to count word frequencies using Apache Spark.
- `data/test.csv`: A sample dataset used by the `word_count.py` script for word counting.
- `requirements.txt`: Lists the Python dependencies required to run the project.

## Installation

To set up the project, follow these steps:

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Create a virtual environment:**
    It's recommended to use a virtual environment to manage project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install dependencies:**
    Install the necessary Python packages using `pip` and the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

After installation, you can run the word count script:

1.  **Ensure your virtual environment is active.**

2.  **Execute the script:**
    The script will process the `data/test.csv` file and print the top 10 most frequent words to the console.
    ```bash
    python word_count.py
    ```

## Usage

The `word_count.py` script utilizes Apache Spark to efficiently count words from a specified CSV file.

-   The script takes an `input_path` (defaulting to `data/test.csv`) and an optional `top_n` parameter (defaulting to 10) for the number of top words to display.
-   It performs text cleaning (lowercase, punctuation removal), stop word filtering, and then calculates word frequencies.
-   The output will be a list of the most frequent words and their counts.
