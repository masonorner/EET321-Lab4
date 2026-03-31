# Imports of import
from install import install

# Holds the names of libraries to be installed
libraries = ["pyvisa", "asyncio", "clickplc", "numpy", "pandas", "openpyxl", "matplotlib", "seaborn", "jupyter"]

# Following code loops the install function to download all requested libraries.
for i in range(len(libraries)):
    install(libraries[i])

# Imports of Import
import asyncio
from clickplc import ClickPLC
from detect_Instruments import detect_instruments
import openpyxl
import pandas as pd
import pyvisa
import time

# Set up the instruments
[supply, fungen, dmm, oscope] = detect_instruments()

# Necessary variables
input      = []
output     = []
resistance = 100

# Set up the definition for the async get function
async def get(sp):
    async with ClickPLC('169.254.13.11') as plc: # add your PLC ip address
        await plc.set('df3',sp)
        time.sleep(1)
        print(await plc.get('df3'))
        s = await plc.get('df3')
        time.sleep(1)
        input.append(s)

# Use the async function to grab the output.
for i in range(2, 11):
    asyncio.run(get(i * 5))
    m = dmm.query('MEAS:VOLT:DC?')
    out = 1000*float(m)/resistance
    print(out)
    output.append(out)
    time.sleep(0.5)

# Take the lists and add them to a dataframe by making them series first.
Ser1 = pd.Series(input,name="Input")
Ser2 = pd.Series(output,name="Output")

# Then use concat to make a dataframe out of them.
measurements = pd.concat([Ser1,Ser2],axis=1)
print(measurements)
measurements.to_excel("Lab4Group3Task4Data.xlsx",index=False)