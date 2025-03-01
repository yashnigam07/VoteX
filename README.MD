# **Electronic Voting System (VoteX)**

## **Project Overview**

The **Electronic Voting System** (VoteX) is a secure and user-friendly application that allows users to vote for candidates in various positions. It includes an admin mode for viewing results and managing the voting process. The system also ensures security by restricting certain keys and providing a lock screen feature.

## **Features**

- **Voting System**: Allows voters to choose candidates for multiple positions such as President, Vice President, Treasurer, and others.
- **Admin Mode**: Admins can access results and manage votes by entering a secure password.
- **Security**: Includes key restrictions to prevent unauthorized actions like closing or minimizing the application (e.g., `Alt+F4`, `Win`, `Ctrl+Esc`).
- **Lock Screen**: Admins can lock the screen to prevent any interference during the voting process.
- **CSV Storage**: All votes are saved in a CSV file for easy retrieval and management.
- **Anonymous Voting**: Voters are assigned an anonymous ID to ensure privacy.
- **Audit Trails**: Tracks all activities within the system for enhanced transparency and security.

## **Requirements**

- Python 3.x
- `tkinter` (for the GUI)
- `keyboard` (to block and unblock keys)
- `ctypes` (for locking the screen)
- `csv` (for saving votes)

## **Setup Instructions**

1. **Clone the Repository**:
     git clone https://github.com/your-username/votex.git
     cd votex

2. **Install Dependencies**:
- Ensure you have Python 3 installed.
- Install the necessary Python packages:
  ```
  pip install tkinter keyboard
  ```

3. **Run the Application**:
- Simply run the Python file:
  ```
  python voting_app.py
  ```

4. **CSV Data**:
- All votes are stored in the `voting_data.csv` file. This file is created automatically when the first vote is submitted.

## **Usage**

- **Voting**: Voters need to enter their name, roll number, and select the duration before voting for candidates in different positions.
- **Admin Mode**: Enter the admin password (`admin123`) to view results and manage the voting system. Admin can unlock restricted keys and exit fullscreen mode.
- **Lock Screen**: Admins can lock the screen at any point using the "Lock Screen" button to secure the application.

## **Security**

- **Admin Authentication**: Only authorized admins can view voting results and modify key restrictions using a password.
- **Key Restrictions**: Critical system keys like `Alt+F4` and `Ctrl+Esc` are disabled during voting to prevent interference.
- **Encryption and Authentication**: Future plans include implementing cryptographic techniques to authenticate software and ensure data integrity.
- **Tamper-Evident Measures**: Plans to incorporate tamper-evident mechanisms to enhance system integrity.

## **Comparison with Other Voting Systems**

- **Offline vs. Online Voting**: VoteX is an offline system, which provides certain security advantages over online systems, such as reduced risk of network attacks. However, online systems offer greater convenience and accessibility.

## **Future Development Plans**

- **Enhanced Security Protocols**: Plans to implement two-factor authentication and biometric verification for enhanced security.
- **Audit Trails**: Already implemented to track system activities.

## **Troubleshooting Tips**

- **Common Issues**: If the application fails to start, ensure that all dependencies are installed correctly.
- **CSV File Issues**: If the CSV file is not created, check the file path and permissions.

## **License**

This project is licensed under the yashnigam.co.in

## **Contributors**

- **Yash Nigam**: Developer (Department of Electronics, Sri Venkateswara College, DU)

## **Additional Resources**
- **Documentation**: [VoteX Documentation](https://github.com/yashnigam/Vot)

---

### Key Improvements:
- **Security Enhancements**: Added discussion on tamper-evident measures and cryptographic authentication.
- **Audit Trails**: Highlighted the implementation of audit trails for transparency.
- **Comparison with Other Voting Systems**: Included a brief comparison of offline and online voting systems.
- **Future Development Plans**: Outlined plans for enhanced security protocols.
- **Troubleshooting Tips**: Added a section for common issues and solutions.
- **Additional Resources**: Linked to a wiki for more detailed information.

