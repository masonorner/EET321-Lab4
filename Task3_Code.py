import asyncio
from clickplc import ClickPLC
import pyvisa
import time

# get addresses of DMM and DC power supply
rm = pyvisa.ResourceManager()
print(rm.list_resources())

#usbs
# supply = rm.open_resource('USB0::0xF4EC::0x1430::SPD3XJEX6R3357::INSTR')
dmm = rm.open_resource('USB0::0xF4EC::0xEE38::SDM35GBC6R0490::INSTR')
# fungen = rm.open_resource('USB0::0xF4EC::0x1103::SDG1XDDX6R5079::INSTR')
# oscope = rm.open_resource('USB0::0xF4EC::0xEE38::SDSMMFCX6R5669::INSTR')

#make csv
dateString = time.strftime("%Y-%m-%d_%H-%M")
filepath = "./" + dateString + ".csv"

async def get(sp):
    async with ClickPLC('169.254.254.153')as plc:  #add your PLC ip address
        await plc.set('df3',sp)
        time.sleep(1)
        print(await plc.get('df3'))
        s = await plc.get('df3')
        time.sleep(1)
        float(s)
        file.write(f'{s},')

#write to csv
with open(filepath, "a") as file:
    for i in range(0, 21):
        asyncio.run(get(i * 5))
        m = dmm.query('MEAS:VOLT:DC?')
        print(m)
        float(m)
        file.write(f'{m}')
        time.sleep(0.5)