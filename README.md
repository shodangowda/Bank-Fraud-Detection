Bank Fraud Detection System

A Python-based banking fraud detection project designed to identify suspicious banking activities and improve transaction security using machine learning techniques. The system provides user authentication, transaction handling, profile management, and fraud detection functionalities through an interactive banking application.

Features
User Login and Authentication
Secure Banking Transactions
User Profile Management
Fraud Detection using Machine Learning
Transaction Monitoring
Database Integration using SQLite
Banking Dashboard Interface
Technologies Used
Python
Machine Learning
SQLite Database
Jupyter Notebook
Tkinter (GUI)
Pandas
NumPy
Scikit-learn
Project Structure
Bank-Fraud-Detection/
│
├── MainLogin.py              # User login module
├── MainProfile.py            # User profile management
├── Transfer.py               # Money transfer functionality
├── banking_app_ml.py         # Machine learning fraud detection logic
├── banking_app_ml.ipynb      # Jupyter notebook for ML model
├── BankMT.db                 # SQLite database
├── BankNH.db                 # SQLite database
├── README.md                 # Project documentation
└── __pycache__/              # Python cache files
Installation
Clone the Repository
git clone https://github.com/YOUR_USERNAME/Bank-Fraud-Detection.git
Navigate to Project Folder
cd Bank-Fraud-Detection
Install Required Libraries
pip install pandas numpy scikit-learn
How to Run the Project
Run the Main Banking Application
python MainLogin.py
Run Machine Learning Module
python banking_app_ml.py
Open Jupyter Notebook
jupyter notebook

Then open:

banking_app_ml.ipynb
Machine Learning Module

The fraud detection system uses machine learning algorithms to analyze transaction patterns and identify suspicious activities. The model helps improve banking security by detecting abnormal transaction behavior.

Database

The project uses SQLite databases:

BankMT.db
BankNH.db

These databases store user information, account details, and transaction records.

Future Enhancements
Real-time fraud detection
OTP verification system
Cloud database integration
AI-based risk prediction
Mobile banking support
Advanced user dashboard
Author

Shodan Gowda

License

This project is developed for educational and academic purposes.
