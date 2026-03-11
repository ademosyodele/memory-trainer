import tkinter as tk
from tkinter import ttk
import random
import time

class ActiveWorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Active Workout Mode")
        self.root.geometry("600x450")
        
        # Word bank for the 'Words' mode
        self.word_bank = [
            "Sprint", "Jump", "Squat", "Lunge", "Plank", "Crunch", "Pushup", 
            "Burpee", "Row", "Press", "Curl", "Dip", "Hold", "Run", "Walk", 
            "Stretch", "Lift", "Throw", "Catch", "Swing", "Pedal", "Climb"
        ]

        # Timer state variables
        self.running = False
        self.start_timestamp = 0
        
        self.setup_ui()

    def setup_ui(self):
        # 1. Main Layout Container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 2. Dropdown Menu Logic
        # Allow the user to select "Numbers" or "Words"
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)

        ttk.Label(control_frame, text="Select Mode:", font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 10))
        
        self.mode_var = tk.StringVar(value="Numbers")
        mode_combo = ttk.Combobox(control_frame, textvariable=self.mode_var, state="readonly", font=("Arial", 11))
        mode_combo['values'] = ("Numbers", "Words")
        mode_combo.pack(side=tk.LEFT)

        # 3. Stopwatch Timer Display
        self.timer_label = ttk.Label(main_frame, text="00:00:00", font=("Helvetica", 48, "bold"))
        self.timer_label.pack(pady=30)

        # 4. Large Text Display Area
        # Used to display the generated string
        self.display_text = tk.Text(main_frame, height=4, width=40, font=("Helvetica", 20), wrap=tk.WORD, bg="#f0f0f0")
        self.display_text.pack(pady=10, fill=tk.BOTH, expand=True)
        self.display_text.config(state=tk.DISABLED) # Read-only initially

        # 5. Control Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)

        # Start Button
        self.start_btn = tk.Button(btn_frame, text="START", bg="#4CAF50", fg="white", 
                                   font=("Arial", 12, "bold"), command=self.start_workout)
        self.start_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Reveal Answers Button
        self.reveal_btn = tk.Button(btn_frame, text="REVEAL ANSWERS", bg="#2196F3", fg="white", 
                                    font=("Arial", 12, "bold"), command=self.stop_workout, state=tk.DISABLED)
        self.reveal_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

    def generate_content(self):
        """
        Generation Logic: Generates a random 10-digit number OR 10-word string.
        (Note: Equivalent to the requested Dart function logic, adapted for Python)
        """
        mode = self.mode_var.get()
        
        if mode == "Numbers":
            # Generate 10 random digits
            # Logic: Create a list of 10 random ints (0-9) and join them
            return "".join([str(random.randint(0, 9)) for _ in range(10)])
        else:
            # Generate 10 random words
            # Logic: Sample 10 items from the word_bank
            return " ".join(random.choices(self.word_bank, k=10))

    def start_workout(self):
        """
        Timer Logic: Starts timer on 'Start' and generates content.
        """
        if self.running:
            return

        # Generate and display content
        content = self.generate_content()
        
        self.display_text.config(state=tk.NORMAL, bg="white")
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, content)
        self.display_text.config(state=tk.DISABLED)

        # Handle Timer State
        self.running = True
        self.start_timestamp = time.time()
        
        # Toggle Button States
        self.start_btn.config(state=tk.DISABLED, bg="#a5d6a7") # Dim start button
        self.reveal_btn.config(state=tk.NORMAL, bg="#2196F3") # Enable reveal button
        
        # Begin Timer Loop
        self.update_timer()

    def stop_workout(self):
        """
        Timer Logic: Stops timer when the user clicks 'Reveal Answers'.
        """
        if not self.running:
            return

        self.running = False
        
        # Toggle Button States
        self.start_btn.config(state=tk.NORMAL, bg="#4CAF50")
        self.reveal_btn.config(state=tk.DISABLED, bg="#90caf9")

    def update_timer(self):
        """
        Updates the timer label every 50ms while running.
        """
        if self.running:
            elapsed = time.time() - self.start_timestamp
            
            # Format time as MM:SS:MS
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            centiseconds = int((elapsed * 100) % 100)
            
            time_str = f"{minutes:02}:{seconds:02}:{centiseconds:02}"
            self.timer_label.config(text=time_str)
            
            # Schedule next update in 50ms
            self.root.after(50, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = ActiveWorkoutApp(root)
    root.mainloop()
