# **Electronic Voting System (VoteX)**  

## **Project Overview**  

The **Electronic Voting System (VoteX)** is a secure and user-friendly application that allows users to vote for candidates in various positions. It includes an **admin mode** for viewing results and managing the voting process. The system ensures security by restricting certain keys and providing a lock screen feature.  

## **Features**  

✅ **Voting System** – Allows voters to select candidates for multiple positions such as President, Vice President, and Treasurer.  
✅ **Admin Mode** – Grants access to results and voting management via a secure password.  
✅ **Security Features** – Restricts certain system keys (`Alt+F4`, `Win`, `Ctrl+Esc`) to prevent unauthorized interference.  
✅ **Lock Screen** – Admins can lock the screen to maintain voting integrity.  
✅ **CSV Storage** – Votes are securely stored in a CSV file for easy retrieval and management.  
✅ **Anonymous Voting** – Voter anonymity is maintained through unique, anonymous IDs.  
✅ **Audit Trails** – Logs all activities within the system to enhance transparency and security.  

## **System Requirements**  

- Python 3.x  
- Required Python libraries:  
  ```sh
  pip install keyboard
  ```  
  *(Note: `tkinter`, `csv`, and `ctypes` are built-in with Python.)*  

## **Installation & Setup**  

1. **Clone the Repository**:  
   ```sh
   git clone https://github.com/your-username/votex.git
   cd votex
   ```  

2. **Install Dependencies**:  
   ```sh
   pip install keyboard
   ```  

3. **Run the Application**:  
   ```sh
   python voting_app.py
   ```  

4. **CSV Data Storage**:  
   - Votes are stored in `voting_data.csv`, automatically created upon the first vote submission.  

## **Usage Guide**  

### **For Voters**  
- Enter **name**, **roll number**, and select a voting duration.  
- Cast votes for candidates in different positions.  

### **For Admins**  
- Log in using the admin password (`admin123`).  
- Manage votes, view results, and unlock restricted keys.  
- Use the **Lock Screen** button to prevent unauthorized access.  

## **Security Measures**  

🔒 **Admin Authentication** – Only authorized admins can access results and modify settings.  
🔒 **Key Restrictions** – Disables critical system keys to prevent interruptions.  
🔒 **Encryption & Authentication (Future Plan)** – Implementing cryptographic techniques for enhanced security.  
🔒 **Tamper-Evident Measures** – Strengthening the system’s integrity by tracking unauthorized modifications.  

## **Comparison with Other Voting Systems**  

| Feature            | VoteX (Offline)       | Online Voting Systems        |  
|-------------------|---------------------|------------------------------|  
| **Security**     | High (No network attacks) | Medium (Prone to cyber threats) |  
| **Accessibility** | Limited (On-site voting) | High (Remote voting possible) |  
| **Data Integrity** | High (Stored locally) | Medium (Network dependencies) |  
| **Transparency** | High (Audit logs) | Varies (Depends on platform) |  

## **Future Development Plans**  

🚀 **Enhanced Security Protocols** – Implementing **two-factor authentication** and **biometric verification**.  
🚀 **Audit Trail Expansion** – Strengthening tracking mechanisms for better accountability.  
🚀 **Web & Mobile Integration** – Exploring a hybrid system for broader accessibility.  

## **Troubleshooting Guide**  

| Issue                 | Possible Solution                                      |  
|----------------------|--------------------------------------------------|  
| App fails to start  | Ensure Python 3.x and dependencies are installed. |  
| CSV file not created | Check file path and user permissions.              |  
| Restricted keys not working | Verify that `keyboard` module is installed properly. |  

## **Screenshots**  

![VoteX Screenshot](https://github.com/yashnigam07/VoteX/blob/main/VoteX.png)  
 

## **License**  

This project is licensed under **yashnigam.co.in**.  

## **Contributors**  

- **Yash Nigam** – Developer (Department of Electronics, Sri Venkateswara College, DU)  

## **Key Improvements in This Version**  

✨ **Security Enhancements** – Added tamper-evident measures and cryptographic authentication plans.  
✨ **Audit Trails** – Emphasized their role in system transparency.  
✨ **Comparison Table** – Clearly differentiates VoteX from online systems.  
✨ **Future Development Roadmap** – Highlighted planned security features.  
✨ **Troubleshooting Section** – Provides solutions to common issues.  
✨ **Enhanced Readability** – Improved structure for better user experience.  
