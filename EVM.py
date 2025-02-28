import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import random
import string
import ctypes
import keyboard

# 🔹 Constants
ADMIN_PASSWORD = "admin123"
CSV_FILENAME = "voting_data.csv"
POSITIONS = {
    "President": ["Candidate 1", "Candidate 2", "Candidate 3"],
    "Vice President": ["Candidate A", "Candidate B", "Candidate C"],
    "Treasurer": ["Candidate X", "Candidate Y", "Candidate Z"],
    "Secretary": ["Candidate I", "Candidate II", "Candidate III"],
    "Joint Treasurer": ["Candidate JT1", "Candidate JT2", "Candidate JT3"],
    "Joint Secretary": ["Candidate JS1", "Candidate JS2", "Candidate JS3"],
    "Creative Head": ["Candidate CH1", "Candidate CH2", "Candidate CH3"],
    "Documentation Head": ["Candidate DH1", "Candidate DH2", "Candidate DH3"],
}
YEAR_OPTIONS = ["1 year", "2 years", "3 years"]

# 🔹 Load & Save Votes
def load_votes_from_csv():
    try:
        with open(CSV_FILENAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_votes_to_csv(votes):
    with open(CSV_FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["voter_name", "roll_number", "year", "selected_positions", "anonymous_id"])
        writer.writeheader()
        writer.writerows(votes)

# 🔹 Block Unauthorized Keys
def block_keys():
    """Disables all restricted keys."""
    keyboard.add_hotkey("alt+f4", lambda: None, suppress=True)
    keyboard.add_hotkey("win", lambda: None, suppress=True)
    keyboard.add_hotkey("win+tab", lambda: None, suppress=True)
    keyboard.add_hotkey("win+d", lambda: None, suppress=True)
    keyboard.add_hotkey("ctrl+esc", lambda: None, suppress=True)
    keyboard.add_hotkey("alt+tab", lambda: None, suppress=True)
    keyboard.add_hotkey("ctrl+shift+esc", lambda: None, suppress=True)

def unblock_keys():
    """Enables all restricted keys (for admin)."""
    keyboard.unhook_all_hotkeys()

# 🔹 Lock Screen
def lock_screen():
    ctypes.windll.user32.LockWorkStation()

# 🔹 Voting App Class
class VotingApp:
    def __init__(self, root):
        self.root = root
        self.votes = load_votes_from_csv()
        self.setup_gui()
        self.is_fullscreen = True
        self.is_admin_mode = False  # Track admin mode
        block_keys()

    def setup_gui(self):
        """Setup UI"""
        self.root.title("🗳️ E")
        self.root.attributes('-fullscreen', True)

        # 🔹 Header
        header_frame = tk.Frame(self.root, bg="#222", height=70)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="VoteX", bg="#222", fg="white", font=("Arial", 20)).pack(pady=10)

        # 🔹 Main Content
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=20)

        tk.Label(main_frame, text="Enter your name:").pack()
        self.voter_name_entry = tk.Entry(main_frame)
        self.voter_name_entry.pack()

        tk.Label(main_frame, text="Enter your roll number:").pack()
        self.roll_number_entry = tk.Entry(main_frame)
        self.roll_number_entry.pack()

        tk.Label(main_frame, text="Select Duration:").pack()
        self.year_combobox = ttk.Combobox(main_frame, values=YEAR_OPTIONS)
        self.year_combobox.pack()

        # 🔹 Position Selection
        self.position_comboboxes = {}
        frame_positions = tk.Frame(main_frame)
        frame_positions.pack()

        for pos, candidates in POSITIONS.items():
            frame = tk.Frame(frame_positions)
            frame.pack(fill="x", padx=10, pady=2)
            tk.Label(frame, text=pos).pack(side="left")
            combobox = ttk.Combobox(frame, values=candidates)
            combobox.pack(side="right")
            self.position_comboboxes[pos] = combobox

        # 🔹 Vote Button
        tk.Button(main_frame, text="🗳️ Submit Vote", command=self.submit_vote).pack(pady=5)

        # 🔹 Admin Section
        tk.Label(main_frame, text="Enter Admin Password:").pack()
        self.admin_password_entry = tk.Entry(main_frame, show="*")
        self.admin_password_entry.pack()

        tk.Button(main_frame, text="📊 Show Results (Admin Only)", command=self.show_results).pack(pady=5)
        tk.Button(main_frame, text="🔒 Lock Screen", command=lock_screen).pack(pady=5)

        # 🔹 Footer
        footer_frame = tk.Frame(self.root, bg="#222", height=50)
        footer_frame.pack(fill="x", side="bottom")
        tk.Label(footer_frame, text="Developed By Yash Nigam, Department Of Electronics, Sri Venkateswara College (DU)", bg="#222", fg="white", font=("Arial", 10)).pack(pady=10)

        # Bind Escape key for admin access & F11 to restore lock
        self.root.bind("<Escape>", self.check_admin_password)
        self.root.bind("<F11>", self.restore_restrictions)

    def submit_vote(self):
        """Submit Vote Function."""
        voter_name = self.voter_name_entry.get()
        roll_number = self.roll_number_entry.get()
        year = self.year_combobox.get()
        selected_positions = {pos: combobox.get() for pos, combobox in self.position_comboboxes.items()}

        if not all([voter_name, roll_number, year]):
            messagebox.showwarning("⚠️ Incomplete Information", "Please fill all details.")
            return

        if any(vote["roll_number"] == roll_number for vote in self.votes):
            messagebox.showwarning("⚠️ Duplicate Vote", "You have already voted.")
            return

        anonymous_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        vote_record = {
            "voter_name": voter_name,
            "roll_number": roll_number,
            "year": year,
            "selected_positions": str(selected_positions),
            "anonymous_id": anonymous_id,
        }
        self.votes.append(vote_record)
        save_votes_to_csv(self.votes)
        messagebox.showinfo("✅ Success", "Your vote has been recorded!")

        # Clear fields
        self.voter_name_entry.delete(0, tk.END)
        self.roll_number_entry.delete(0, tk.END)
        self.year_combobox.set("")
        for combobox in self.position_comboboxes.values():
            combobox.set("")

    def show_results(self):
        """Show Results (Admin Only)."""
        if self.admin_password_entry.get() != ADMIN_PASSWORD:
            messagebox.showerror("⛔ Access Denied", "Invalid password.")
            self.admin_password_entry.delete(0, tk.END)
            return
        
        result_text = "📊 Voting Results:\n\n"
        for position, candidates in POSITIONS.items():
            result_text += f"{position}:\n"
            position_votes = {candidate: 0 for candidate in candidates}

            for vote in self.votes:
                selected_candidate = eval(vote["selected_positions"]).get(position, None)
                if selected_candidate in position_votes:
                    position_votes[selected_candidate] += 1

            for candidate, votes in position_votes.items():
                result_text += f"   {candidate}: {votes} votes\n"
            result_text += "\n"

        messagebox.showinfo("📊 Results", result_text)
        self.admin_password_entry.delete(0, tk.END)

    def check_admin_password(self, event=None):
        """Grant Admin Full Access (Unblock Keys & Exit Fullscreen)."""
        password = simpledialog.askstring("🔐 Admin Authentication", "Enter Admin Password:", show="*")
        if password == ADMIN_PASSWORD:
            self.root.attributes('-fullscreen', False)
            self.is_fullscreen = False
            unblock_keys()
            self.is_admin_mode = True

    def restore_restrictions(self, event=None):
        """Re-enable Key Restrictions (If Admin Disabled Them)."""
        if self.is_admin_mode:
            self.root.attributes('-fullscreen', True)
            block_keys()
            self.is_admin_mode = False

# Run Application
root = tk.Tk()
app = VotingApp(root)
root.mainloop()
