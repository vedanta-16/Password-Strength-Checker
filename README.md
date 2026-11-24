# 🔐 Password Strength Checker

A Python-based **Password Strength Checker** that evaluates password security based on length, uppercase and lowercase letters, numbers, and special characters.

It also checks passwords against a common password dataset (**RockYou**) to identify commonly used passwords and estimates potential password-cracking time.

Built using **Python** and **Colorama**, this project provides terminal-based password security analysis with clear, color-coded results.

## 🚀 Features

- **Password Length Analysis:** Checks whether the password meets recommended length requirements.
- **Character Validation:** Checks for uppercase letters, lowercase letters, numbers, and special characters.
- **Common Password Detection:** Checks passwords against the RockYou password dataset.
- **Password Strength Evaluation:** Evaluates password strength based on multiple security criteria.
- **Cracking Time Estimation:** Estimates how long a password could take to crack.
- **Color-Coded Output:** Uses Colorama for readable terminal results.

## 🛠️ Technologies Used

- Python 3
- Colorama
- RockYou Password Dataset
- Regular Expressions

## 📁 Project Structure

```text
Password-Strength-Checker/
│
├── password-strength-checker.py
├── rockyou.txt
├── requirements.txt
└── README.md
```

*Note: The RockYou dataset is optional but required for common-password checking. Its filename and location must match the path configured in the Python script.*

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Password-Strength-Checker
```

### 3. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
```

Activate it:

**Linux / Kali Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file, install Colorama directly:

```bash
pip install colorama
```

### 5. Add the RockYou Dataset

If your script uses the RockYou dataset, ensure that `rockyou.txt` is available in the location expected by your code.

On Kali Linux, the compressed dataset may be available at:

```bash
/usr/share/wordlists/rockyou.txt.gz
```

Extract it using:

```bash
sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz
```

Copy it into your project directory if your script expects a local file:

```bash
cp /usr/share/wordlists/rockyou.txt ./rockyou.txt
```

## ▶️ How to Run

Run the following command from the project directory:

```bash
python3 password-strength-checker.py
```

The program will prompt you to enter a password and display its security analysis in the terminal.

## 📊 Analysis Criteria

| Security Check | Description |
|---|---|
| Length | Evaluates password length |
| Uppercase | Checks for capital letters |
| Lowercase | Checks for small letters |
| Numbers | Checks for numeric characters |
| Special Characters | Checks for symbols |
| RockYou Check | Identifies common passwords |
| Crack Time | Estimates potential cracking time |

## 🎯 Learning Objectives

- Understand password security fundamentals.
- Learn how password complexity affects security.
- Explore dictionary-based password checking.
- Understand common password vulnerabilities.
- Practice Python scripting and terminal-based application development.

## ⚠️ Disclaimer

This project is developed for educational and cybersecurity learning purposes only.

- Do not use real or sensitive passwords for testing.
- Password cracking time is an estimate, not a guarantee.
- RockYou is a historical leaked password dataset and should only be used for authorized security research and educational purposes.

## 👨‍💻 Author

**Vedanta Kashelkar**

Cybersecurity Enthusiast | BSc Information Technology Graduate



---

⭐ If you find this project useful, consider giving the repository a star!
