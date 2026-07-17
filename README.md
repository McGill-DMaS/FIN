# FIN: Function Inlining Normalizer

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/Paper-Journal%20of%20Systems%20and%20Software-2F6F9F.svg)](https://www.sciencedirect.com/science/article/pii/S0164121225002729)
[![DOI](https://img.shields.io/badge/DOI-10.1016%2Fj.jss.2025.112603-007EC6.svg)](https://doi.org/10.1016/j.jss.2025.112603)
[![BibTeX](https://img.shields.io/badge/Cite-BibTeX-success.svg)](#citation)

> **FIN: Boosting Binary Code Embedding by Normalizing Function Inlinings**  
> Mohammadhossein Amouei, Benjamin C. M. Fung, and Philippe Charland  
> *Journal of Systems and Software*, Volume 231, Article 112603, 2026  
> **[Read the paper](https://www.sciencedirect.com/science/article/pii/S0164121225002729)** · **[DOI](https://doi.org/10.1016/j.jss.2025.112603)** · **[BibTeX](#citation)**

## Project Description

This repository contains the tool developed for the FIN paper. FIN constructs ground-truth function-inlining datasets by analyzing and comparing the debugging information of two ELF binaries. It identifies function calls in the first binary that have been inlined into the second binary.

## Prerequisites

Before installing FIN, ensure that the following prerequisites are available:

- Python
- Poetry

## Installing Poetry

### Step 1: Install `pipx`

`pipx` allows Python applications to be installed and executed in isolated environments.

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

After installation, you may need to restart your shell or terminal before the `pipx` command becomes available.

### Step 2: Install Poetry

Install Poetry through `pipx`:

```bash
pipx install poetry
```

This installs Poetry in an isolated environment while making it accessible from your terminal.

## Installation

Clone the repository and run the setup script:

```bash
git clone https://github.com/McGill-DMaS/FIN.git
cd FIN
python setup.py
```

## Usage

FIN requires two ELF binaries produced from the same program but compiled using different optimization levels or compilers:

- The **original binary**, from which function calls are extracted.
- The **target binary**, in which inlined function calls are identified.

Run FIN using the following command:

```bash
python fin.py \
    --ida <path-to-IDA-Pro> \
    -o <path-to-original-binary> \
    -t <path-to-target-binary>
```

### Arguments

| Argument | Description |
|---|---|
| `--ida` | Path to the IDA Pro installation or executable. |
| `-o` | Path to the original ELF binary. |
| `-t` | Path to the target ELF binary. |

## Citation

If you use FIN in your research, please cite the following paper:

> M. Amouei, B. C. M. Fung, and P. Charland, “FIN: Boosting Binary Code Embedding by Normalizing Function Inlinings,” *Journal of Systems and Software*, vol. 231, Art. no. 112603, 2026.

<details>
<summary><strong>Show BibTeX</strong></summary>

```bibtex
@article{amouei2026fin,
  title   = {{FIN: Boosting Binary Code Embedding by Normalizing Function Inlinings}},
  author  = {Amouei, Mohammadhossein and Fung, Benjamin C. M. and Charland, Philippe},
  journal = {Journal of Systems and Software},
  volume  = {231},
  pages   = {112603},
  year    = {2026},
  issn    = {0164-1212},
  doi     = {10.1016/j.jss.2025.112603},
  url     = {https://www.sciencedirect.com/science/article/pii/S0164121225002729},
  keywords = {Binary code, similarity detection, function inlining,
              control-flow graph, random forest}
}
```

</details>

## Disclaimer

This software is provided as-is, without warranty or support. The authors assume no responsibility for damages, loss of income, or other problems arising from its use.

For further information, please consult the paper and the source code. Questions and issue reports may be submitted through the repository's issue tracker.
