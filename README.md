# Student Result Processing System

## Introduction

This Python program is designed to process student results and generate histograms based on the results. It takes input regarding pass, defer, and fail credits for each student and categorizes them into different result categories: Progress, Progress (module trailer), Exclude, or Module retriever. The program also provides a graphical representation of the distribution of students across these categories through histograms.

## Features

- Validates input for pass, defer, and fail credits to ensure they fall within the correct range and add up to 120 credits.
- Categorizes students into different result categories based on their credit distribution.
- Generates histograms to visualize the distribution of students across different result categories.

## Usage

1. Run the program.
2. Input the pass, defer, and fail credits for each student when prompted.
3. Repeat the process for multiple students if necessary.
4. Press 'q' when finished to view the results and histograms.

## File Structure

- `student_results.py`: Main Python script containing the program logic.
- `graphics.py`: Module for graphical representation (provided separately).
- `student_results.txt`: Text file where the results are stored.

## Requirements

- Python 3.x
- `graphics` module (provided)

## Author

- **Name:** jathushan Varnakulasingam
- **Date:** 11/12/2023

## License

This project is licensed under the [MIT License](LICENSE).
