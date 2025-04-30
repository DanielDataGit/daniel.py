# The purpose of this program is to help investors trade like Warren Buffett. It uses his investing principles to value
# the stock in question. It also offers a short put strike price. Run it and have a go.

# API support libraries
# pip install certifi
import certifi
import ssl
from urllib.request import urlopen
import json

# GUI support libraries
# pip install customtkinter
import customtkinter
import tkinter

# DATA support libraries
import pandas as pd
from sympy import symbols, Eq, solve


def get_jsonparsed_data(url):
    """Code from FMP to get/parse data from their JSON"""
    context = ssl.create_default_context(cafile=certifi.where())
    response = urlopen(url, context=context)
    data = response.read().decode("utf-8")
    return json.loads(data)


# initialize customtkinter window
customtkinter.set_appearance_mode("system")
root = customtkinter.CTk()
root.geometry("960 x 540")

# Display all column and initialize empty dataframe
pd.set_option('display.max_columns', None)
x = pd.DataFrame()


def stockVal():
    """function that calculates and appends valuation data to dataframe"""
    ticker = entry1.get() # get user input from gui
    url = (f"https://financialmodelingprep.com/api/v3/discounted-cash-flow/{ticker}?apikey"
           f"=wcwrVLVMhYICGRP7RXBx0fVE1Gi8oC0y")
    # retrieves API data as dictionary
    response_data = get_jsonparsed_data(url)
    # Checks data is present
    if response_data:
        # Converts to dataframe
        data = pd.DataFrame(response_data)
        # Calculate Margin of Safety and rounds to 2 places
        data['Margin of Safety'] = round((data['dcf'] - data['Stock Price']) / abs(data['dcf']) * 100, 2)

        # Sets Buffet's Approval based on Margin of Safety
        y = int(entry2.get()) # get user input from gui
        if data['Margin of Safety'].iloc[0] >= y:
            data["Buffett Approves"] = "Yes"
        else:
            data["Buffett Approves"] = "No"

        # Calculates strike price and rounds to 2 places
        z = symbols('z')
        equation = Eq((data["dcf"].iloc[0] - z) / abs(data["dcf"].iloc[0]) * 100, int(entry2.get()))
        answer = solve(equation, z)
        rounded_answer = [round(float(a), 2) for a in answer]
        data["Strike Price"] = rounded_answer

        # concatenates data to dataframe
        global x
        x = pd.concat([x, data], ignore_index=True)

        stockResult.insert("1.0", data.to_string(index=False) + "\n")
        entry1.delete(0, tkinter.END)

        return data
    else:
        stockResult.insert("1.0", "No data returned from the API or out of API requests. Check Spelling." + "\n")


# creates frame to hold widgets
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
# creates title label
label = customtkinter.CTkLabel(master=frame, text="Warren Buffett Stock Screener")
label.pack(pady=10, padx=10)
# creates frame to hold entry widgets
entry_frame = customtkinter.CTkFrame(master=frame)
entry_frame.pack(pady=10, padx=10)
# entry widget for ticker symbol
entry1 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Ticker Symbol", justify="center")
entry1.pack(side=tkinter.LEFT, padx=5, pady=10)
# entry widget for margin of safety value, set at 30
entry2 = customtkinter.CTkEntry(master=entry_frame, placeholder_text="Margin of Safety", justify="center")
entry2.pack(side=tkinter.LEFT, padx=5, pady=10)
entry2.insert(0, "30")
# triggers stockVal function
button = customtkinter.CTkButton(master=frame, text="Search", command=stockVal)
button.pack(pady=10, padx=10)
# text display for results
stockResult = tkinter.Text(master=frame, height=10, width=100, background="gray")
stockResult.pack(pady=10, padx=10)
# label to display description
description_label = customtkinter.CTkLabel(master=frame,
                                           text="This widget is a stock screener inspired by Warren Buffett's "
                                                "principles.\n"
                                                "Enter a ticker symbol to see the margin of safety at 30% (Or modify "
                                                "to your likeness)"
                                                " and recommended short put strike price.\n"
                                                "Data is sourced from Financial Modeling Prep. The creator of this "
                                                "program is not liable for any financial losses incurred by its use")
description_label.pack(pady=10, padx=10)
# tkinter loop
root.mainloop()