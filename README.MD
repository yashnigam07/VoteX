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
