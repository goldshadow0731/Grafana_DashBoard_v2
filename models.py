import datetime
import os

from dotenv import load_dotenv
from sqlalchemy import Column, Boolean, Integer, Float, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseTable():
    __table_args__ = {
        "mysql_charset": "utf8mb4"
    }
    Count_Log = Column(Integer, nullable=False, primary_key=True)
    Time_Stamp = Column(DateTime(timezone=False), nullable=False,
                        default=datetime.datetime.utcnow)


class DL303TC(BaseTable, Base):  # 溫度
    __tablename__ = "DL303_TC"
    Temp = Column(Float(5, 2), nullable=False)


class DL303RH(BaseTable, Base):  # 濕度
    __tablename__ = "DL303_RH"
    Humi = Column(Float(5, 2), nullable=False)


class DL303DC(BaseTable, Base):  # 露點溫度
    __tablename__ = "DL303_DC"
    Dew_Point = Column(Float(5, 2), nullable=False)


class DL303CO2(BaseTable, Base):  # CO2濃度
    __tablename__ = "DL303_CO2"
    Co2 = Column(Float(6, 2), nullable=False)


class ET7044(BaseTable, Base):  # ET7044 開關
    __tablename__ = "ET7044"
    SW1 = Column(Boolean, nullable=False)
    SW2 = Column(Boolean, nullable=False)
    SW3 = Column(Boolean, nullable=False)
    SW4 = Column(Boolean, nullable=False)
    SW5 = Column(Boolean, nullable=False)
    SW6 = Column(Boolean, nullable=False)
    SW7 = Column(Boolean, nullable=False)
    SW8 = Column(Boolean, nullable=False)


class AirCondictionA(BaseTable, Base):  # 冷氣A
    __tablename__ = "Air_Condiction_A"
    Temp = Column(Float(5, 2), nullable=False)
    Humi = Column(Float(5, 2), nullable=False)


class AirCondictionB(BaseTable, Base):  # 冷氣B
    __tablename__ = "Air_Condiction_B"
    Temp = Column(Float(5, 2), nullable=False)
    Humi = Column(Float(5, 2), nullable=False)


class UPSA(BaseTable, Base):  # UPS A
    __tablename__ = "UPS_A"
    Device_Locate = Column(String(40), nullable=False)
    Device_Life = Column(String(20), nullable=False)
    Input_Line = Column(Integer, nullable=False)
    Input_Volt = Column(Float(5, 2), nullable=False)
    Input_Freq = Column(Float(5, 2), nullable=False)
    Output_Line = Column(Integer, nullable=False)
    Output_Freq = Column(Float(5, 2), nullable=False)
    Output_Volt = Column(Float(5, 2), nullable=False)
    Output_Amp = Column(Float(6, 4), nullable=False)
    Output_Watt = Column(Float(5, 3), nullable=False)
    Output_Percent = Column(Integer, nullable=False)
    System_Mode = Column(String(20), nullable=False)
    Battery_Volt = Column(Integer, nullable=False)
    Battery_Remain_Percent = Column(Integer, nullable=False)
    Battery_Health = Column(String(20), nullable=False)
    Battery_Status = Column(String(20), nullable=False)
    Battery_Charge_Mode = Column(String(40), nullable=False)
    Battery_Temp = Column(Integer, nullable=False)
    Battery_Last_Change_Year = Column(Integer, nullable=False)
    Battery_Last_Change_Mon = Column(Integer, nullable=False)
    Battery_Last_Change_Day = Column(Integer, nullable=False)
    Battery_Next_Change_Year = Column(Integer, nullable=False)
    Battery_Next_Change_Mon = Column(Integer, nullable=False)
    Battery_Next_Change_Day = Column(Integer, nullable=False)


class UPSB(BaseTable, Base):  # UPS B
    __tablename__ = "UPS_B"
    Device_Locate = Column(String(40), nullable=False)
    Device_Life = Column(String(20), nullable=False)
    Input_Line = Column(Integer, nullable=False)
    Input_Volt = Column(Float(5, 2), nullable=False)
    Input_Freq = Column(Float(5, 2), nullable=False)
    Output_Line = Column(Integer, nullable=False)
    Output_Freq = Column(Float(5, 2), nullable=False)
    Output_Volt = Column(Float(5, 2), nullable=False)
    Output_Amp = Column(Float(6, 4), nullable=False)
    Output_Watt = Column(Float(5, 3), nullable=False)
    Output_Percent = Column(Integer, nullable=False)
    System_Mode = Column(String(20), nullable=False)
    Battery_Volt = Column(Integer, nullable=False)
    Battery_Remain_Percent = Column(Integer, nullable=False)
    Battery_Health = Column(String(20), nullable=False)
    Battery_Status = Column(String(20), nullable=False)
    Battery_Charge_Mode = Column(String(40), nullable=False)
    Battery_Temp = Column(Integer, nullable=False)
    Battery_Last_Change_Year = Column(Integer, nullable=False)
    Battery_Last_Change_Mon = Column(Integer, nullable=False)
    Battery_Last_Change_Day = Column(Integer, nullable=False)
    Battery_Next_Change_Year = Column(Integer, nullable=False)
    Battery_Next_Change_Mon = Column(Integer, nullable=False)
    Battery_Next_Change_Day = Column(Integer, nullable=False)


class PowerBoxA(BaseTable, Base):  # Power Box A
    __tablename__ = "Power_Box_A"
    In_A = Column(Float(5, 2), nullable=False)
    In_B = Column(Float(5, 2), nullable=False)
    Out_A = Column(Float(5, 2), nullable=False)
    Out_B = Column(Float(5, 2), nullable=False)
    Out_C = Column(Float(5, 2), nullable=False)
    Out_D = Column(Float(5, 2), nullable=False)
    Out_E = Column(Float(5, 2), nullable=False)


class PowerBoxB(BaseTable, Base):  # Power Box B
    __tablename__ = "Power_Box_B"
    In_A = Column(Float(5, 2), nullable=False)
    In_B = Column(Float(5, 2), nullable=False)
    Out_A = Column(Float(5, 2), nullable=False)
    Out_B = Column(Float(5, 2), nullable=False)
    Out_C = Column(Float(5, 2), nullable=False)
    Out_D = Column(Float(5, 2), nullable=False)
    Out_E = Column(Float(5, 2), nullable=False)


class PowerMeter(BaseTable, Base):  # 變電箱 功率
    __tablename__ = "Power_Meter"
    Temp = Column(Float(5, 2), nullable=False)
    Humi = Column(Float(5, 2), nullable=False)
    Current = Column(Float(5, 2), nullable=False)
    Current_A = Column(Float(5, 2), nullable=False)
    Current_B = Column(Float(5, 2), nullable=False)


class WaterTank(BaseTable, Base):  # 水塔 功率
    __tablename__ = "Water_Tank"
    Current = Column(Float(5, 2), nullable=False)


if __name__ == "__main__":
    # Load env variable
    dotenv_path = f"{os.path.dirname(os.path.abspath(__file__))}/.env"
    if os.path.exists(dotenv_path):
        load_dotenv(f"{os.path.dirname(os.path.abspath(__file__))}/.env")

    engine = create_engine(os.environ.get("SQL_SERVER"), echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
