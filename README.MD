<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electronic Voting System (VoteX) - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        p, ul {
            color: #555;
        }
        code {
            background-color: #e0e0e0;
            padding: 2px 5px;
        }
        pre {
            background-color: #e0e0e0;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Electronic Voting System (VoteX)</h1>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#project-overview">Project Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#setup-instructions">Setup Instructions</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#security">Security</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contributors">Contributors</a></li>
        <li><a href="#future-plans">Future Development Plans</a></li>
    </ul>

    <h2 id="project-overview">Project Overview</h2>
    <p>The <strong>Electronic Voting System</strong> (VoteX) is a secure and user-friendly application that allows users to vote for candidates in various positions. It includes an admin mode for viewing results and managing the voting process. The system also ensures security by restricting certain keys and providing a lock screen feature.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li><strong>Voting System:</strong> Allows voters to choose candidates for multiple positions such as President, Vice President, Treasurer, and others.</li>
        <li><strong>Admin Mode:</strong> Admins can access results and manage votes by entering a secure password.</li>
        <li><strong>Security:</strong> Includes key restrictions to prevent unauthorized actions like closing or minimizing the application (e.g., Alt+F4, Win, Ctrl+Esc).</li>
        <li><strong>Lock Screen:</strong> Admins can lock the screen to prevent any interference during the voting process.</li>
        <li><strong>CSV Storage:</strong> All votes are saved in a CSV file for easy retrieval and management.</li>
        <li><strong>Anonymous Voting:</strong> Voters are assigned an anonymous ID to ensure privacy.</li>
    </ul>

    <h2 id="requirements">Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>tkinter</code> (for the GUI)</li>
        <li><code>ctypes</code> (for locking the screen)</li>
        <li><code>csv</code> (for saving votes)</li>
    </ul>

    <h2 id="setup-instructions">Setup Instructions</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/your-username/votex.git
cd votex</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install tkinter</code></pre>
        </li>
        <li><strong>Run the Application:</strong>
            <pre><code>python voting_app.py</code></pre>
        </li>
        <li><strong>CSV Data:</strong> All votes are stored in the <code>voting_data.csv</code> file. This file is created automatically when the first vote is submitted.</li>
    </ol>

    <h2 id="usage">Usage</h2>
    <ul>
        <li><strong>Voting:</strong> Voters need to enter their name, roll number, and select the duration before voting for candidates in different positions.</li>
        <li><strong>Admin Mode:</strong> Enter the admin password (<code>admin123</code>) to view results and manage the voting system. Admin can unlock restricted keys and exit fullscreen mode.</li>
        <li><strong>Lock Screen:</strong> Admins can lock the screen at any point using the "Lock Screen" button to secure the application.</li>
    </ul>

    <h2 id="security">Security</h2>
    <ul>
        <li><strong>Admin Authentication:</strong> Only authorized admins can view voting results and modify key restrictions using a password.</li>
        <li><strong>Key Restrictions:</strong> Critical system keys like <code>Alt+F4</code> and <code>Ctrl+Esc</code> are disabled during voting to prevent interference.</li>
    </ul>

    <h2 id="license">License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>

    <h2 id="contributors">Contributors</h2>
    <p><strong>Yash Nigam</strong>: Developer (Department of Electronics, Sri Venkateswara College, DU)</p>

    <h2 id="future-plans">Future Development Plans</h2>
    <p>Future enhancements include implementing more advanced security measures, such as encryption for sensitive data, and expanding the application to support more positions and features.</p>

    <h2>Additional Resources</h2>
    <p>For more detailed documentation and troubleshooting tips, please visit our <a href="https://your-wiki-link.com">Wiki</a>.</p>

</div>

</body>
</html>
