# Github Status Web Scraping with Python

This project is a Python script that performs web scraping on the official Github Status website (https://www.githubstatus.com/) and returns the status of each component to the user via the terminal.

## Installation

To run this script, please follow these instructions:

1. Clone the repository:

```
git clone https://github.com/devwander/github-status-web-scraping-python.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

To use this script, simply navigate to the directory where the main.py file is located and run:

```
python3 main.py
```

This will display the current status of each Github component, as well as a final message indicating whether all systems are operational.

## Sample Output

Here's an example of what the output of the script might look like:

```
Current status:
Git Operations ------------------------------------------------------------- Operational
API Requests --------------------------------------------------------------- Operational
Webhooks ------------------------------------------------------------------- Operational
Visit www.githubstatus.com for more information ---------------------------- Operational
Issues --------------------------------------------------------------------- Operational
Pull Requests -------------------------------------------------------------- Operational
Actions -------------------------------------------------------------------- Operational
Packages ------------------------------------------------------------------- Operational
Pages ---------------------------------------------------------------------- Operational
Codespaces ----------------------------------------------------------------- Operational
Copilot -------------------------------------------------------------------- Operational
✔️ All Systems Operational
```