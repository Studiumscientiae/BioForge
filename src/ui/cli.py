"""
ui/cli.py

Graphical user interface for BioForge.

Responsibilities:
- Display the application window.
- Collect user input.
- Send user input to the application controller.
- Display results and error messages.

Does not perform:
- Sequence validation
- Sequence creation
- Biological analysis
- File parsing
"""

import customtkinter as ctk
from src.main import process_sequence

class BioForgeApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("BioForge")
        self.geometry("1200x700")
        self.minsize(900,600)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar= ctk.CTkFrame(self)
        self.sidebar.grid(row=0, column=0 , sticky="ns")

        self.main_frame= ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.validation_button = None
        self.name_entry = None
        self.sequence_text= None
        self.process_button= None
        self.result_box= None

        self.create_sidebar()
        self.create_main_frame()

    def create_sidebar(self):
        """ Create the application sidebar. """
        title_label= ctk.CTkLabel(self.sidebar,
                                  text="BioForge",
                                  font=("Arial", 24, "bold"))
        title_label.pack(pady=(20,30))

        self.validation_button= ctk.CTkButton(self.sidebar,
                                              text="Sequence Validation")
        self.validation_button.pack(fill="x",padx=10,pady=5)

    def create_main_frame(self):
        """ Create the main content area."""

        title_label= ctk.CTkLabel(self.main_frame,
                                  text="Sequence Validation",
                                  font=("Arial", 24, "bold"))
        title_label.pack(pady=(20,10))

        name_label= ctk.CTkLabel(self.main_frame,
                                 text="Sequence Name")

        name_label.pack(anchor="w",padx=20)

        self.name_entry= ctk.CTkEntry(self.main_frame,
                                      placeholder_text="Enter sequence name")

        self.name_entry.pack(fill="x", padx=20, pady=(0,15))

        sequence_label= ctk.CTkLabel(self.main_frame,
                                     text="DNA Sequence")

        sequence_label.pack(anchor="w",padx=20)

        self.sequence_text= ctk.CTkTextbox(self.main_frame,
                                         height= 180)

        self.sequence_text.pack(fill="both", expand=True, padx=20, pady=(0,20))

        self.process_button= ctk.CTkButton(self.main_frame,
                                           text="Process Sequence",
                                           command= self.process_input)

        self.process_button.pack(padx=20,pady=10)

        self.result_box = ctk.CTkTextbox(self.main_frame,
                                         height=120)

        self.result_box.pack(fill="both", padx=20, pady=(0,20))

    def process_input(self):
        """ Process the user's input. """

        name=self.name_entry.get()
        sequence=self.sequence_text.get("1.0","end-1c")

        try:
            result=process_sequence(name, sequence)

            self.result_box.delete("1.0","end")
            self.result_box.insert("1.0",str(result))

        except ValueError as error:
            self.result_box.delete("1.0", "end")
            self.result_box.insert("1.0", str(error))


if __name__ == "__main__":
    app = BioForgeApp()
    app.mainloop()