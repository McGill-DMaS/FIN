# FIN: Function Inlining Normalizer

[![GitHub license](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)

## Project Description

This repository hosts the tool developed for the FIN paper, designed to construct a ground truth inlining dataset. The tool analyzes and compares the debug information of two ELF binaries to identify function calls from the first binary that have been inlined into the second binary.

## Prerequisites
Before you begin, ensure that the following prerequisites are met:
- python
- poetry

## Installing Poetry
### Step 1: Install `pipx`
`pipx` allows you to install and run Python applications in isolated environments.

To install `pipx`, run the following command:

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Once installed, you may need to restart your shell or terminal for the `pipx` command to be available.

### Step 2: Install Poetry using `pipx`

Once `pipx` is installed, use it to install Poetry:

```bash
pipx install poetry
```

This ensures that Poetry is installed in an isolated environment and is easily accessible from your terminal.

## Installation

After installing Poetry, follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/McGill-DMaS/FIN.git
    cd FIN/
    ```
2. Setup the project:
    ```bash
    python setup.py
    ```

## Usage
To detect function inlining, you need two ELF files of the same program, but compiled with different optimization levels or compilers for comparison. Then, you can then run the following command, where `-o` specifies the path to the original binary file (from which function calls are extracted), and `-t` specifies the target binary file (in which inlined function calls are identified).
```bash
python fin.py --ida <path-to-IDA-Pro> -o <path-to-original-binary> -t <path-to-target-binary>
```

## Disclaimer

The software is provided as-is with no warranty or support. We do not take any responsibility for any damage, loss of income, or any problems you might experience from using our software. If you have questions, you are encouraged to consult the paper and the source code. If you find our software useful, please cite our paper above.

## Citation

If you use this code, please cite the following paper:

```bibtex
@article{AMOUEI2026112603,
title = {{FIN: Boosting binary code embedding by normalizing function inlinings}},
journal = {Journal of Systems and Software},
volume = {231},
pages = {112603},
year = {2026},
issn = {0164-1212},
doi = {https://doi.org/10.1016/j.jss.2025.112603},
url = {https://www.sciencedirect.com/science/article/pii/S0164121225002729},
author = {Mohammadhossein Amouei and Benjamin C.M. Fung and Philippe Charland},
keywords = {Binary code, Similarity detection, Function inlining, Control flow graph, Random forest},
}


