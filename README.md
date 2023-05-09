
# JEE Counsellor

A command-line tool for JEE counselling assistance.

## Introduction

JEE Counsellor is a Python-based tool designed to assist with the counselling process for JEE (Joint Entrance Examination). It provides information about different rounds of counselling, institutes, programs, and closing ranks based on user input. This tool aims to simplify the decision-making process for JEE aspirants by providing relevant data.

## Table of Contents

- [Installation](#installation)
  - [Through Executable (Fast to install and setup, but slow to execute.)](#executable)
    - [Windows](#windows)
    - [Mac](#mac)
    - [Linux](#linux)
  - [Cloning from the Source](#cloning-from-the-source)
    - [Windows](#cloning-from-the-source--windows)
    - [Mac](#cloning-from-the-source--linux-mac)
    - [Linux](#cloning-from-the-source--linux-mac)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [License](#license)

## Installation

### Executable (Might be Slow)

The JEE Counsellor tool is available as an executable for Windows, Mac, and Linux. Follow the instructions below to run the tool on your respective operating system.

#### Windows

- Download the `jcounsellor.exe` executable file from the [latest release](https://github.com/ksauraj/jee_counsellor/releases).

- Double-click the `jcounsellor.exe` file to run the tool.

#### Mac

- Download the `jcounsellor` executable file from the [latest release](https://github.com/ksauraj/jee_counsellor/releases).

- Open the Terminal application.

- Navigate to the directory where the `jcounsellor` file is located using the `cd` command. For example, if the file is in the Downloads folder, use the following command:
   ```bash
   cd ~/Downloads
   ```

- Make the file executable by running the following command:
   ```bash
   chmod +x jcounsellor
   ```

- Run the tool using the following command:
   ```bash
   ./jcounsellor
   ```

#### Linux

- Download the `jcounsellor` executable file from the [latest release](https://github.com/ksauraj/jee_counsellor/releases).

- Open the Terminal application.

- Navigate to the directory where the `jcounsellor` file is located using the `cd` command. For example, if the file is in the Downloads folder, use the following command:
   ```bash
   cd ~/Downloads
   ```

- Make the file executable by running the following command:
   ```bash
   chmod +x jcounsellor
   ```

- Run the tool using the following command:
   ```bash
   ./jcounsellor
   ```

## Cloning from the Source
By opting for this installation method, you gain the advantage of a dynamic and adaptable setup, ensuring access to the most recent code updates and the opportunity to actively participate in the project's advancement and enhancement.

### Cloning from the Source ( Windows )

#### Prerequisites

Before cloning the repository and running the tool, ensure that you have the following software installed on your Windows system:

- [Python 3.x](https://www.python.org/downloads/windows/)
- [Git](https://git-scm.com/download/win)

##### Steps

- Install Python:
   - Download the latest version of Python 3.x from the official Python website: [Download Python](https://www.python.org/downloads/windows/).
   - Run the installer and follow the installation instructions.
   - Make sure to select the option to add Python to your system's PATH during the installation process.

- Install Git:
   - Download Git for Windows from the official Git website: [Download Git](https://git-scm.com/download/win).
   - Run the installer and follow the installation instructions.
   - During the installation, you can choose the default options unless you have specific preferences.

- Clone the repository:
   - Open the Command Prompt (CMD) or Git Bash.
   - Navigate to the directory where you want to clone the repository using the `cd` command. For example, to clone the repository into the current directory, use:
     ```bash
     cd /path/to/desired/directory
     ```
   - Clone the repository using the following command:
     ```bash
     git clone https://github.com/ksauraj/jee_counsellor.git
     ```

- Navigate to the project directory:
   - Change the current directory to the cloned repository:
     ```bash
     cd jee_counsellor
     ```

- Install the dependencies:
   - Install the required dependencies using the following command:
     ```bash
     pip install -r requirements.txt
     ```

- Run the tool:
   - Launch the JEE Counsellor tool using the following command:
     ```bash
     python tool.py
     ```



### Cloning from the Source (Linux / Mac )

- Ensure that you have Python 3.x installed on your system.
- Clone the repository:

```bash
git clone https://github.com/ksauraj/jee_counsellor.git
```

- Navigate to the project directory:

```bash
cd jee_counsellor
```

- Install the dependencies:

```bash
pip install -r requirements.txt
```

- Run the tool:

```bash
python tool.py
```

## Dependencies

The following dependencies are required to run JEE Counsellor:

- Python 3.x
- pandas
- colorama

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

- Launch the tool by following the installation instructions.
- Select the counseling type (JOSAA or CSAB) and the respective round.
- Choose the institute type and program(s) you are interested in.
- Enter your rank to view the closing ranks and related information.
- The tool will display the results in a browser window.

## License

This project is licensed under the GNU General Public License v3.0. For more details, see the LICENSe file.


## Credit
- **Tool Developer**: This project has been developed by [Ksauraj](https://github.com/ksauraj).
