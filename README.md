# Information Security Code Guide

## Setting Up a Virtual Environment

### Creating a Virtual Environment

To create a new virtual environment, you can use the following command:

```bash
python -m venv env
```

> **Note**: `env` is the name of the virtual environment; feel free to choose any name.

#### Specifying Python Version

If you need a specific Python version, you can specify it like this:

```bash
python3.x -m venv env
```

> **Note**: Replace `3.x` with the desired version (e.g., '3.8', '3.9').

### Activating the Virtual Environment

#### On Windows

```bash
env\Scripts\activate
```

#### On macOS or Linux

```bash
source env/bin/activate
```

## Installing Scapy

To install Scapy, simply run the following command:

```bash
pip install scapy
```
