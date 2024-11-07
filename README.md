# Dataset Generator

The Dataset Generator project is responsible for creating datasets in document-based conversational chat format for use in Augmented Generation Retrieval.

## Installation

To install the Dataset Generator, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/nelsonfrugeri-tech/dataset-generator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd dataset-generator
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To use the Dataset Generator, follow these steps:

1. Run the `chunk.py` script to break down the files passed into `file/source` and create the new chunking files:
   ```sh
   python chunk.py
   ```
2. Run the `dataset.py` script to create the conversational datasets:
   ```sh
   python dataset.py
   ```

## Contributing

We welcome contributions to the Dataset Generator project. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
