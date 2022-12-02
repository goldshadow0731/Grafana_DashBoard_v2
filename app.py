import datetime
import json
import os

from dotenv import load_dotenv
from paho.mqtt import client as MQTT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (
    DL303TC, DL303RH, DL303DC, DL303CO2, ET7044,
    AirCondictionA, AirCondictionB, UPSA, UPSB,
    PowerBoxA, PowerBoxB, PowerMeter, WaterTank
)


# Timezone setting
tz_delta = datetime.timedelta(hours=8)
tz = datetime.timezone(tz_delta)
# Load env variable
dotenv_path = f"{os.path.dirname(os.path.abspath(__file__))}/.env"
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# DataBase
engine = create_engine(os.environ.get("SQL_SERVER"), echo=True)
Session = sessionmaker(bind=engine)

# MQTT
client = MQTT.Client()


@client.connect_callback()
def on_connect(client, userdata, flags, rresult):
    print(f"=============== {'Connect':^15} ===============")
    client.subscribe("DL303/TC")
    client.subscribe("DL303/RH")
    client.subscribe("DL303/DC")
    client.subscribe("DL303/CO2")
    client.subscribe("ET7044/DOstatus")
    client.subscribe("UPS/A/Monitor")
    client.subscribe("UPS/B/Monitor")
    client.subscribe("air_condiction/A")
    client.subscribe("air_condiction/B")
    client.subscribe("cabinet_A")
    client.subscribe("cabinet_B")
    client.subscribe("current")
    client.subscribe("waterTank")


@client.message_callback()
def on_message(client, userdata, msg):
    data = msg.payload.decode('utf-8')
    print(f"{msg.topic} - {data}")
    with Session.begin() as session:
        if msg.topic == "DL303/TC":
            session.add(DL303TC(
                Temp=data
            ))
        elif msg.topic == "DL303/RH":
            session.add(DL303RH(
                Humi=data
            ))
        elif msg.topic == "DL303/DC":
            session.add(DL303DC(
                Dew_Point=data
            ))
        elif msg.topic == "DL303/CO2":
            session.add(DL303CO2(
                Co2=data
            ))
        elif msg.topic == "ET7044/DOstatus":
            payload = json.loads(data)
            session.add(ET7044(
                SW1=payload[0],
                SW2=payload[1],
                SW3=payload[2],
                SW4=payload[3],
                SW5=payload[4],
                SW6=payload[5],
                SW7=payload[6],
                SW8=payload[7]
            ))
        elif msg.topic == "air_condiction/A":
            payload = json.loads(data)
            session.add(AirCondictionA(
                Temp=payload["temp"],
                Humi=payload["humi"]
            ))
        elif msg.topic == "air_condiction/B":
            payload = json.loads(data)
            session.add(AirCondictionB(
                Temp=payload["temp"],
                Humi=payload["humi"]
            ))
        elif msg.topic == "UPS/A/Monitor":
            payload = json.loads(data)
            session.add(UPSA(
                Device_Locate="/dev/ttyUSB0 (牆壁)",
                Device_Life="onLine(在線)",
                Input_Line=payload["input"]["line"],
                Input_Volt=payload["input"]["volt"],
                Input_Freq=payload["input"]["freq"],
                Output_Line=payload["output"]["line"],
                Output_Freq=payload["output"]["freq"],
                Output_Volt=payload["output"]["volt"],
                Output_Amp=payload["output"]["amp"],
                Output_Watt=payload["output"]["percent"],
                Output_Percent=payload["output"]["watt"],
                System_Mode=payload["output"]["mode"].split(" ")[0],
                Battery_Volt=payload["battery"]["status"]["volt"],
                Battery_Remain_Percent=payload["battery"]["status"]["remainPercent"],
                Battery_Health=payload["battery"]["status"]["health"],
                Battery_Status=payload["battery"]["status"]["status"],
                Battery_Charge_Mode=payload["battery"]["status"]["chargeMode"],
                Battery_Temp=payload["temp"],
                Battery_Last_Change_Year=payload["battery"]["lastChange"]["year"],
                Battery_Last_Change_Mon=payload["battery"]["lastChange"]["month"],
                Battery_Last_Change_Day=payload["battery"]["lastChange"]["day"],
                Battery_Next_Change_Year=payload["battery"]["nextChange"]["year"],
                Battery_Next_Change_Mon=payload["battery"]["nextChange"]["month"],
                Battery_Next_Change_Day=payload["battery"]["nextChange"]["day"]
            ))
        elif msg.topic == "UPS/B/Monitor":
            payload = json.loads(data)
            session.add(UPSB(
                Device_Locate="/dev/ttyUSB1 (窗戶)",
                Device_Life="onLine(在線)",
                Input_Line=payload["input"]["line"],
                Input_Volt=payload["input"]["volt"],
                Input_Freq=payload["input"]["freq"],
                Output_Line=payload["output"]["line"],
                Output_Freq=payload["output"]["freq"],
                Output_Volt=payload["output"]["volt"],
                Output_Amp=payload["output"]["amp"],
                Output_Watt=payload["output"]["percent"],
                Output_Percent=payload["output"]["watt"],
                System_Mode=payload["output"]["mode"].split(" ")[0],
                Battery_Volt=payload["battery"]["status"]["volt"],
                Battery_Remain_Percent=payload["battery"]["status"]["remainPercent"],
                Battery_Health=payload["battery"]["status"]["health"],
                Battery_Status=payload["battery"]["status"]["status"],
                Battery_Charge_Mode=payload["battery"]["status"]["chargeMode"],
                Battery_Temp=payload["temp"],
                Battery_Last_Change_Year=payload["battery"]["lastChange"]["year"],
                Battery_Last_Change_Mon=payload["battery"]["lastChange"]["month"],
                Battery_Last_Change_Day=payload["battery"]["lastChange"]["day"],
                Battery_Next_Change_Year=payload["battery"]["nextChange"]["year"],
                Battery_Next_Change_Mon=payload["battery"]["nextChange"]["month"],
                Battery_Next_Change_Day=payload["battery"]["nextChange"]["day"]
            ))
        elif msg.topic == "cabinet_A":
            payload = json.loads(data)
            session.add(PowerBoxA(
                In_A=payload["IN_V110_A"],
                In_B=payload["IN_V110_B"],
                Out_A=payload["OUT_V110_A"],
                Out_B=payload["OUT_V110_B"],
                Out_C=payload["OUT_V110_C"],
                Out_D=payload["OUT_V110_D"],
                Out_E=payload["OUT_V110_E"]
            ))
        elif msg.topic == "cabinet_B":
            payload = json.loads(data)
            session.add(PowerBoxB(
                In_A=payload["IN_V110_A"],
                In_B=payload["IN_V110_B"],
                Out_A=payload["OUT_V110_A"],
                Out_B=payload["OUT_V110_B"],
                Out_C=payload["OUT_V110_C"],
                Out_D=payload["OUT_V110_D"],
                Out_E=payload["OUT_V110_E"]
            ))
        elif msg.topic == "current":
            payload = json.loads(data)
            session.add(PowerMeter(
                Temp=payload["Temperature"],
                Humi=payload["Humidity"],
                Current=payload["currents"],
                Current_A=payload["current_a"],
                Current_B=payload["current_b"]
            ))
        elif msg.topic == "waterTank":
            payload = json.loads(data)
            session.add(WaterTank(
                Current=payload["current"]
            ))


if __name__ == "__main__":
    client.connect(os.environ.get("MQTT_IP"),
                   int(os.environ.get("MQTT_PORT")))
    client.loop_forever()
