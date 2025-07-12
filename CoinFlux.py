import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # API key (in a real app, this should be secured)
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        
        # Variables
        self.from_currency = StringVar()
        self.to_currency = StringVar()
        self.amount = DoubleVar()
        self.converted_amount = StringVar()
        
        # Initialize currencies (common ones)
        self.currencies = [
            "USD", "EUR", "GBP", "JPY", "AUD", 
            "CAD", "CHF", "CNY", "SEK", "NZD"
        ]
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        Label(self.root, text="Currency Converter", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Frame for inputs
        frame = Frame(self.root)
        frame.pack(pady=20)
        
        # From currency
        Label(frame, text="From:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        from_combobox = ttk.Combobox(frame, textvariable=self.from_currency, values=self.currencies, state="readonly")
        from_combobox.grid(row=0, column=1, padx=5, pady=5)
        from_combobox.set("USD")
        
        # To currency
        Label(frame, text="To:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        to_combobox = ttk.Combobox(frame, textvariable=self.to_currency, values=self.currencies, state="readonly")
        to_combobox.grid(row=1, column=1, padx=5, pady=5)
        to_combobox.set("EUR")
        
        # Amount
        Label(frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
        Entry(frame, textvariable=self.amount).grid(row=2, column=1, padx=5, pady=5)
        
        # Convert button
        Button(frame, text="Convert", command=self.convert).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result
        Label(self.root, text="Converted Amount:", font=("Arial", 12)).pack(pady=5)
        Label(self.root, textvariable=self.converted_amount, font=("Arial", 14, "bold")).pack()
        
        # Info label
        Label(self.root, text="Rates update when converting", font=("Arial", 8), fg="gray").pack(side=BOTTOM, pady=5)
    
    def get_exchange_rate(self, from_curr, to_curr):
        try:
            # In a real application, you would use the API key here
            # response = requests.get(f"{self.base_url}{from_curr}?api_key={self.api_key}")
            
            # For demonstration, we'll use a free API without key
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_curr}")
            data = response.json()
            
            if response.status_code == 200:
                return data['rates'].get(to_curr, 0)
            else:
                messagebox.showerror("Error", "Failed to fetch exchange rates")
                return None
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return None
    
    def convert(self):
        try:
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            amount = self.amount.get()
            
            if not from_curr or not to_curr:
                messagebox.showwarning("Warning", "Please select both currencies")
                return
            
            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be greater than 0")
                return
            
            rate = self.get_exchange_rate(from_curr, to_curr)
            
            if rate is not None:
                converted = round(amount * rate, 2)
                self.converted_amount.set(f"{converted} {to_curr}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverter(root)
    root.mainloop()