import tkinter
import customtkinter
from tkinter import filedialog
from PIL import Image
import sounddevice as sd
from scipy.io.wavfile import write
import pygame
pygame.mixer.init()

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

#define filter fx
def filter_input():
    # List of disallowed characters
    disallowed_chars = {'{'}

    # Check if the pressed key is in the disallowed characters
    if event.char in disallowed_chars:
        # Prevent the character from being inserted
        return "break"  # Return "break" to cancel the event

# Define the Record1 function
def Record1(duration):
    fs = 44100  # Sample rate
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('outp.wav', fs, myrecording)  # Save as WAV file

#transcription
def transcribing():
         import whisper

         model = whisper.load_model("tiny")
         result = model.transcribe("outp.wav")
         f=open('transcrib.txt','w')
         print(result["text"],file=f)
         f.close()



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initialize default values
        self.record_duration = 20  # Default duration
        self.transcription_model = "tiny"  # Default model

        #filter

        # Configure window
        self.title("ProComm.py")
        self.geometry(f"{1200}x{500}")
        self.configure(fg_color='#000000')

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color="#909090")
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ProComm", text_color='black', font=customtkinter.CTkFont('Product Sans', size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 20))
        
        my_image = customtkinter.CTkImage(light_image=Image.open('igotchucps.PNG'),
                                         dark_image=Image.open('igotchucps.PNG'),
                                         size=(150,150))
        my_label = customtkinter.CTkButton(self, text="", image=my_image)
        my_label.grid(row=0, column=0, padx=20, pady=(1,1))

        my_image1 = customtkinter.CTkImage(light_image=Image.open('settingicon.PNG'),
                                          dark_image=Image.open('settingicon.PNG'),
                                          size=(40,40))
        self.appearance_mode_optionemenu = customtkinter.CTkButton(self, text="", width=10, height=10, image=my_image1, fg_color='#909090', command=self.open_toplevel)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))

        aicomm = customtkinter.CTkLabel(self.sidebar_frame, text="AI Comm Tool", text_color='black', font=customtkinter.CTkFont('Product Sans', size=20, weight="bold"))
        aicomm.grid(row=8, column=0, padx=20, pady=(1, 1))

        # Create textboxes
        self.textbox = customtkinter.CTkTextbox(self, font=('Product Sans', 16), fg_color='#212121', wrap='word', width=300, height=300, state="normal")
        self.textbox.grid(row=0, column=3, padx=(20, 0), pady=(20, 0))

        self.textbox2 = customtkinter.CTkTextbox(self, font=('Product Sans',16), fg_color='#212121', wrap='word', width=300, height=300, state="normal")
        self.textbox2.grid(row=0, column=1, padx=(20, 0), pady=(20, 0))

        self.textbox2.bind(filter_input)

        self.lbl = customtkinter.CTkLabel(self, font=('Product Sans', 13), text_color='white', text="ProComm is an all in one, verbal communication skills development tool. Available to the members of Communication Professionals. This program is not to be distributed or sold")
        self.lbl.grid(row=1, column=1, columnspan=3, padx=(20,0), pady=(20,0))

        # Create tabview
        self.tabview = customtkinter.CTkTabview(self, width=350)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(0, 0))
        self.tabview.add("Audio Booth")
        self.tabview.tab("Audio Booth").grid_columnconfigure(0, weight=1)

        # Record button
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Audio Booth"), width=150, height=75,
                                                         text="Record",
                                                         font=('Product Sans',16),
                                                         command=self.record_action)
        self.string_input_button.grid(row=1, column=0, padx=20, pady=(10, 10))

        #Play Button
        self.play_button = customtkinter.CTkButton(self.tabview.tab("Audio Booth"), width=150, height=75,
                                                  text="Play Recording",
                                                  font=('Product Sans', 16),
                                                  command=self.play_recording)
        self.play_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        
        # Analyze button
        self.string_input_button2 = customtkinter.CTkButton(self.tabview.tab("Audio Booth"), width=150, height=75,
                                                          text="Analyse",
                                                          font=('Product Sans',16),
                                                          command=self.insert_analysis_output)
        self.string_input_button2.grid(row=3, column=0, padx=20, pady=(10, 10))

        # Speech To Text button
        self.string_input_button3 = customtkinter.CTkButton(self.tabview.tab("Audio Booth"), text="Speech To Text", width=150, height=75,
                                                          font=('Product Sans',16),
                                                          command=self.insert_analysis_output2)
        self.string_input_button3.grid(row=4, column=0, padx=20, pady=(10, 10))

        # Set default values
        self.textbox.insert("0.0", "                 Transcription Box")
        self.textbox2.insert("0.0", "              Speech Analysis Box")

    def open_toplevel(self):
        # Create a new instance of a CTk Toplevel window
        top = customtkinter.CTkToplevel()
        top.title("Settings")
        top.geometry("400x300")
        top.configure(fg_color='#212121')  # Consistent background color

        # Create a frame inside the new window for styling
        frame = customtkinter.CTkFrame(top, width=400, height=300, corner_radius=10, fg_color='#333333')
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Add a label and input for Speech Recording Duration
        duration_label = customtkinter.CTkLabel(frame, text="Speech Recording Duration (seconds):", text_color='white', font=customtkinter.CTkFont('Product Sans', 14))
        duration_label.pack(pady=(20, 5))
        self.duration_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter duration in seconds", width=300)
        self.duration_entry.pack(pady=(0, 20))

        # Add a label and input for Transcription Model Text
        model_label = customtkinter.CTkLabel(frame, text="Transcription Model:", text_color='white', font=customtkinter.CTkFont('Product Sans', 14))
        model_label.pack(pady=(10, 5))
        self.model_entry = customtkinter.CTkEntry(frame, placeholder_text="Enter model name (e.g., tiny)", width=300)
        self.model_entry.pack(pady=(0, 20))

        # Add a button to close the window or apply changes
        button = customtkinter.CTkButton(frame, text="Apply Changes", command=self.apply_changes, width=120)
        button.pack(pady=10)

        # Add a close button
        close_button = customtkinter.CTkButton(frame, text="Close", command=top.destroy, width=120)
        close_button.pack(pady=10)

    def apply_changes(self):
        # Get the user inputs and store them in instance variables
        try:
            self.record_duration = int(self.duration_entry.get())
        except ValueError:
            print("Invalid duration input. Using default value of 20 seconds.")
            self.record_duration = 20
        
        self.transcription_model = self.model_entry.get() or "tiny"
        print(f"Speech Recording Duration: {self.record_duration} seconds")
        print(f"Transcription Model: {self.transcription_model}")

    def record_action(self):
        self.string_input_button.configure(text="Recording...", fg_color='#FF8000')

        self.update_idletasks()
        # Use the stored duration when recording
        Record1(self.record_duration)
        # Add additional actions as needed
        self.string_input_button.configure(text="Record", fg_color='#0078D4')

    def play_recording(self):
        self.play_button.configure(text="Playing...", fg_color='#FF8000')

        self.update_idletasks()
        # Load and play the recorded audio
        try:
            pygame.mixer.music.load("outp.wav")
            pygame.mixer.music.play()
            print("Playing recording...")

            while pygame.mixer.music.get_busy():
                self.update()
                
        except pygame.error as e:
            print(f"Error playing sound: {e}")

        self.play_button.configure(text="Play Recording", fg_color='#0078D4')

    def insert_analysis_output2(self):
        self.string_input_button3.configure(text="Transcribing...", fg_color='#FF8000')

        self.update_idletasks()
        
        transcribing()
        file=open('transcrib.txt','r',encoding="utf-8")
        f=file
        read=file.readlines()
        self.textbox.delete("0.0", tkinter.END)
        self.textbox.insert("0.0", read)
        f.close()

        self.string_input_button3.configure(text="Speech To Text", fg_color='#0078D4')

    def insert_analysis_output(self):
        # Assume Analysis1 function uses self.transcription_model or other instance attributes
        mysp = __import__("my-voice-analysis")
        mysp.myspsr
        
        
        Analysis1()  # Call Analysis1 to get output
        file1 = open('myspsr.txt','r')
        file2 = open('mysppaus.txt','r')
        file3 = open('myspsyl.txt','r')
        file4 = open('myspst.txt','r')
        file5 = open('myspod.txt','r')
        file6 = open('myspbala.txt','r')
        file7 = open('mysppron.txt','r')
        file8 = open('myspgend.txt', 'r')
        
        read1=file1.readlines()
        read2=file2.readlines()
        read3=file3.readlines()
        read4=file4.readlines()
        read5=file5.readlines()
        read6=file6.readlines()
        read7=file7.readlines()
        read8=file8.readlines()

        
        self.textbox2.delete("0.0", tkinter.END)  # Clear existing content
        self.textbox2.insert("0.0", read1)

        self.textbox2.insert("2.0", read2)
      
        self.textbox2.insert("4.0", read3)
        
        self.textbox2.insert("6.0", read4)
        
        self.textbox2.insert("8.0", read5)
        
        self.textbox2.insert("10.0", read6)

        self.textbox2.insert("12.0", read7)# Insert new output into textbox2

        self.textbox2.insert("14.0", read8)
                
# Ensure this function uses self.transcription_model or other instance attributes
def Analysis1():
    mysp = __import__("my-voice-analysis")
    p = "outp"  # audio File title
    c = r"C:\Users\alric\Documents\work\Ultimate"  # Path to the Audio_File directory
    mysp.myspsr(p, c)
    mysp.mysppaus(p, c)
    mysp.myspsyl(p, c)
    mysp.myspst(p, c)
    mysp.myspod(p, c)
    mysp.myspbala(p, c)
    mysp.mysppron(p, c)
    mysp.myspgend(p, c)

if __name__ == "__main__":
    app = App()
    app.mainloop()
