"""Constants for the Tuya integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
import logging

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import (
    CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
    CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
    CONCENTRATION_PARTS_PER_BILLION,
    CONCENTRATION_PARTS_PER_MILLION,
    LIGHT_LUX,
    PERCENTAGE,
    SIGNAL_STRENGTH_DECIBELS,
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    Platform,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfVolume,
    UnitOfVolumetricFlux,
)

DOMAIN = "tuya"
LOGGER = logging.getLogger(__package__)

CONF_APP_TYPE = "tuya_app_type"
CONF_ENDPOINT = "endpoint"
CONF_TERMINAL_ID = "terminal_id"
CONF_TOKEN_INFO = "token_info"
CONF_USER_CODE = "user_code"
CONF_USERNAME = "username"

TUYA_CLIENT_ID = "HA_3y9q4ak7g4ephrvke"
TUYA_SCHEMA = "haauthorize"

TUYA_DISCOVERY_NEW = "tuya_discovery_new"
TUYA_HA_SIGNAL_UPDATE_ENTITY = "tuya_entry_update"

TUYA_RESPONSE_CODE = "code"
TUYA_RESPONSE_MSG = "msg"
TUYA_RESPONSE_QR_CODE = "qrcode"
TUYA_RESPONSE_RESULT = "result"
TUYA_RESPONSE_SUCCESS = "success"

PLATFORMS = [
    Platform.ALARM_CONTROL_PANEL,
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.CAMERA,
    Platform.CLIMATE,
    Platform.COVER,
    Platform.EVENT,
    Platform.FAN,
    Platform.HUMIDIFIER,
    Platform.LIGHT,
    Platform.NUMBER,
    Platform.SCENE,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SIREN,
    Platform.SWITCH,
    Platform.VACUUM,
    Platform.VALVE,
]


class WorkMode(StrEnum):
    """Work modes."""

    COLOUR = "colour"
    MUSIC = "music"
    SCENE = "scene"
    WHITE = "white"


class DPType(StrEnum):
    """Data point types."""

    BITMAP = "Bitmap"
    BOOLEAN = "Boolean"
    ENUM = "Enum"
    INTEGER = "Integer"
    JSON = "Json"
    RAW = "Raw"
    STRING = "String"


class DeviceCategory(StrEnum):
    """Tuya device categories.

    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
    """

    AMY = "amy"
    """Massage chair"""
    BGL = "bgl"
    """Wall-hung boiler"""
    BH = "bh"
    """Smart kettle

    https://developer.tuya.com/en/docs/iot/fbh?id=K9gf484m21yq7
    """
    BX = "bx"
    """Refrigerator"""
    BXX = "bxx"
    """Safe box"""
    CJKG = "cjkg"
    """Scene switch"""
    CKMKZQ = "ckmkzq"
    """Garage door opener

    https://developer.tuya.com/en/docs/iot/categoryckmkzq?id=Kaiuz0ipcboee
    """
    CKQDKG = "ckqdkg"
    """Card switch"""
    CL = "cl"
    """Curtain

    https://developer.tuya.com/en/docs/iot/categorycl?id=Kaiuz1hnpo7df
    """
    CLKG = "clkg"
    """Curtain switch

    https://developer.tuya.com/en/docs/iot/category-clkg?id=Kaiuz0gitil39
    """
    CN = "cn"
    """Milk dispenser"""
    CO2BJ = "co2bj"
    """CO2 detector

    https://developer.tuya.com/en/docs/iot/categoryco2bj?id=Kaiuz3wes7yuy
    """
    COBJ = "cobj"
    """CO detector

    https://developer.tuya.com/en/docs/iot/categorycobj?id=Kaiuz3u1j6q1v
    """
    CS = "cs"
    """Dehumidifier

    https://developer.tuya.com/en/docs/iot/categorycs?id=Kaiuz1vcz4dha
    """
    CWTSWSQ = "cwtswsq"
    """Pet treat feeder"""
    CWWQFSQ = "cwwqfsq"
    """Pet ball thrower"""
    CWWSQ = "cwwsq"
    """Pet feeder

    https://developer.tuya.com/en/docs/iot/categorycwwsq?id=Kaiuz2b6vydld
    """
    CWYSJ = "cwysj"
    """Pet fountain

    https://developer.tuya.com/en/docs/iot/categorycwysj?id=Kaiuz2dfro0nd
    """
    CZ = "cz"
    """Socket"""
    DBL = "dbl"
    """Electric fireplace

    https://developer.tuya.com/en/docs/iot/electric-fireplace?id=Kaiuz2hz4iyp6
    """
    DC = "dc"
    """String lights

    # https://developer.tuya.com/en/docs/iot/dc?id=Kaof7taxmvadu
    """
    DCL = "dcl"
    """Induction cooker"""
    DD = "dd"
    """Strip lights

    https://developer.tuya.com/en/docs/iot/dd?id=Kaof804aibg2l
    """
    DGNBJ = "dgnbj"
    """Multi-functional alarm

    https://developer.tuya.com/en/docs/iot/categorydgnbj?id=Kaiuz3yorvzg3
    """
    DJ = "dj"
    """Light

    https://developer.tuya.com/en/docs/iot/categorydj?id=Kaiuyzy3eheyy
    """
    DLQ = "dlq"
    """Circuit breaker

    https://developer.tuya.com/en/docs/iot/dlq?id=Kb0kidk9enyh8
    """
    DR = "dr"
    """Electric blanket

    https://developer.tuya.com/en/docs/iot/categorydr?id=Kaiuz22dyc66p
    """
    DS = "ds"
    """TV set"""
    FS = "fs"
    """Fan

    https://developer.tuya.com/en/docs/iot/categoryfs?id=Kaiuz1xweel1c
    """
    FSD = "fsd"
    """Ceiling fan light

    https://developer.tuya.com/en/docs/iot/fsd?id=Kaof8eiei4c2v
    """
    FWD = "fwd"
    """Ambiance light

    https://developer.tuya.com/en/docs/iot/ambient-light?id=Kaiuz06amhe6g
    """
    GGQ = "ggq"
    """Irrigator

    https://developer.tuya.com/en/docs/iot/categoryggq?id=Kaiuz1qib7z0k
    """
    GYD = "gyd"
    """Motion sensor light

    https://developer.tuya.com/en/docs/iot/gyd?id=Kaof8a8hycfmy
    """
    GYMS = "gyms"
    """Business lock"""
    HOTELMS = "hotelms"
    """Hotel lock"""
    HPS = "hps"
    """Human presence sensor

    https://developer.tuya.com/en/docs/iot/categoryhps?id=Kaiuz42yhn1hs
    """
    JS = "js"
    """Water purifier"""
    JSQ = "jsq"
    """Humidifier

    https://developer.tuya.com/en/docs/iot/categoryjsq?id=Kaiuz1smr440b
    """
    JTMSBH = "jtmsbh"
    """Smart lock (keep alive)"""
    JTMSPRO = "jtmspro"
    """Residential lock pro"""
    JWBJ = "jwbj"
    """Methane detector

    https://developer.tuya.com/en/docs/iot/categoryjwbj?id=Kaiuz40u98lkm
    """
    KFJ = "kfj"
    """Coffee maker

    https://developer.tuya.com/en/docs/iot/categorykfj?id=Kaiuz2p12pc7f
    """
    KG = "kg"
    """Switch

    https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
    """
    KJ = "kj"
    """Air purifier

    https://developer.tuya.com/en/docs/iot/f?id=K9gf46h2s6dzm
    """
    KQZG = "kqzg"
    """Air fryer"""
    KT = "kt"
    """Air conditioner

    https://developer.tuya.com/en/docs/iot/categorykt?id=Kaiuz0z71ov2n
    """
    KTKZQ = "ktkzq"
    """Air conditioner controller"""
    LDCG = "ldcg"
    """Luminance sensor

    https://developer.tuya.com/en/docs/iot/categoryldcg?id=Kaiuz3n7u69l8
    """
    LILIAO = "liliao"
    """Physiotherapy product"""
    LYJ = "lyj"
    """Drying rack"""
    MAL = "mal"
    """Alarm host

    https://developer.tuya.com/en/docs/iot/categorymal?id=Kaiuz33clqxaf
    """
    MB = "mb"
    """Bread maker"""
    MC = "mc"
    """Door/window controller

    https://developer.tuya.com/en/docs/iot/s?id=K9gf48r5zjsy9
    """
    MCS = "mcs"
    """Contact sensor

    https://developer.tuya.com/en/docs/iot/s?id=K9gf48hm02l8m
    """
    MG = "mg"
    """Rice cabinet"""
    MJJ = "mjj"
    """Towel rack"""
    MK = "mk"
    """Access control

    https://developer.tuya.com/en/docs/iot/s?id=Kb0o2xhlkxbet
    """
    MS = "ms"
    """Residential lock"""
    MS_CATEGORY = "ms_category"
    """Lock accessories"""
    MSP = "msp"
    """Cat toilet

    https://developer.tuya.com/en/docs/iot/s?id=Kakg3srr4ora7
    """
    MZJ = "mzj"
    """Sous vide cooker

    https://developer.tuya.com/en/docs/iot/categorymzj?id=Kaiuz2vy130ux
    """
    NNQ = "nnq"
    """Bottle warmer"""
    NTQ = "ntq"
    """HVAC"""
    PC = "pc"
    """Power strip

    https://developer.tuya.com/en/docs/iot/s?id=K9gf7o5prgf7s
    """
    PHOTOLOCK = "photolock"
    """Audio and video lock"""
    PIR = "pir"
    """Human motion sensor

    https://developer.tuya.com/en/docs/iot/categorypir?id=Kaiuz3ss11b80
    """
    PM2_5 = "pm2.5"
    """PM2.5 detector

    https://developer.tuya.com/en/docs/iot/categorypm25?id=Kaiuz3qof3yfu
    """
    QN = "qn"
    """Heater

    https://developer.tuya.com/en/docs/iot/categoryqn?id=Kaiuz18kih0sm
    """
    RQBJ = "rqbj"
    """Gas alarm

    https://developer.tuya.com/en/docs/iot/categoryrqbj?id=Kaiuz3d162ubw
    """
    RS = "rs"
    """Water heater

    https://developer.tuya.com/en/docs/iot/categoryrs?id=Kaiuz0nfferyx
    """
    SB = "sb"
    """Watch/band"""
    SD = "sd"
    """Robot vacuum

    https://developer.tuya.com/en/docs/iot/fsd?id=K9gf487ck1tlo
    """
    SF = "sf"
    """Sofa"""
    SGBJ = "sgbj"
    """Siren alarm

    https://developer.tuya.com/en/docs/iot/categorysgbj?id=Kaiuz37tlpbnu
    """
    SJ = "sj"
    """Water leak detector

    https://developer.tuya.com/en/docs/iot/categorysj?id=Kaiuz3iub2sli
    """
    SOS = "sos"
    """Emergency button

    https://developer.tuya.com/en/docs/iot/categorysos?id=Kaiuz3oi6agjy
    """
    SP = "sp"
    """Smart camera

    https://developer.tuya.com/en/docs/iot/categorysp?id=Kaiuz35leyo12
    """
    SZ = "sz"
    """Smart indoor garden

    https://developer.tuya.com/en/docs/iot/categorysz?id=Kaiuz4e6h7up0
    """
    TGKG = "tgkg"
    """Dimmer switch

    https://developer.tuya.com/en/docs/iot/categorytgkg?id=Kaiuz0ktx7m0o
    """
    TGQ = "tgq"
    """Dimmer

    https://developer.tuya.com/en/docs/iot/categorytgkg?id=Kaiuz0ktx7m0o
    """
    TNQ = "tnq"
    """Smart milk kettle"""
    TRACKER = "tracker"
    """Tracker"""
    TS = "ts"
    """Smart jump rope"""
    TYNDJ = "tyndj"
    """Solar light

    https://developer.tuya.com/en/docs/iot/tynd?id=Kaof8j02e1t98
    """
    TYY = "tyy"
    """Projector"""
    TZC1 = "tzc1"
    """Body fat scale"""
    VIDEOLOCK = "videolock"
    """Lock with camera"""
    WK = "wk"
    """Thermostat

    https://developer.tuya.com/en/docs/iot/f?id=K9gf45ld5l0t9
    """
    WSDCG = "wsdcg"
    """Temperature and humidity sensor

    https://developer.tuya.com/en/docs/iot/categorywsdcg?id=Kaiuz3hinij34
    """
    XDD = "xdd"
    """Ceiling light

    https://developer.tuya.com/en/docs/iot/ceiling-light?id=Kaiuz03xxfc4r
    """
    XFJ = "xfj"
    """Ventilation system"""
    XXJ = "xxj"
    """Diffuser

    https://developer.tuya.com/en/docs/iot/categoryxxj?id=Kaiuz1f9mo6bl
    """
    XY = "xy"
    """Washing machine"""
    YB = "yb"
    """Bathroom heater"""
    YG = "yg"
    """Bathtub"""
    YKQ = "ykq"
    """Remote control

    https://developer.tuya.com/en/docs/iot/ykq?id=Kaof8ljn81aov
    """
    YLCG = "ylcg"
    """Pressure sensor

    https://developer.tuya.com/en/docs/iot/categoryylcg?id=Kaiuz3kc2e4gm
    """
    YWBJ = "ywbj"
    """Smoke alarm

    https://developer.tuya.com/en/docs/iot/categoryywbj?id=Kaiuz3f6sf952
    """
    ZD = "zd"
    """Vibration sensor

    https://developer.tuya.com/en/docs/iot/categoryzd?id=Kaiuz3a5vrzno
    """
    ZNDB = "zndb"
    """Smart electricity meter

    https://developer.tuya.com/en/docs/iot/smart-meter?id=Kaiuz4gv6ack7
    """
    ZNFH = "znfh"
    """Bento box"""
    ZNSB = "znsb"
    """Smart water meter"""
    ZNYH = "znyh"
    """Smart pill box"""

    # Undocumented
    AQCZ = "aqcz"
    """Single Phase power meter (undocumented)"""
    BZYD = "bzyd"
    """White noise machine (undocumented)"""
    CWJWQ = "cwjwq"
    """Smart Odor Eliminator-Pro (undocumented)

    see https://github.com/orgs/home-assistant/discussions/79
    """
    DGHSXJ = "dghsxj"
    """Smart Camera - Low power consumption camera (undocumented)

    see https://github.com/home-assistant/core/issues/132844
    """
    DSD = "dsd"
    """Filament Light

    Based on data from https://github.com/home-assistant/core/issues/106703
    Product category mentioned in https://developer.tuya.com/en/docs/iot/oemapp-light?id=Kb77kja5woao6
    As at 30/12/23 not documented in https://developer.tuya.com/en/docs/iot/lighting?id=Kaiuyzxq30wmc
    """
    FSKG = "fskg"
    """Fan wall switch (undocumented)"""
    HJJCY = "hjjcy"
    """Air Quality Monitor

    https://developer.tuya.com/en/docs/iot/hjjcy?id=Kbeoad8y1nnlv
    """
    HXD = "hxd"
    """Wake Up Light II (undocumented)"""
    JDCLJQR = "jdcljqr"
    """Curtain Robot (undocumented)"""
    JQBJ = "jqbj"
    """Formaldehyde Detector (undocumented)"""
    KS = "ks"
    """Tower fan (undocumented)

    See https://github.com/orgs/home-assistant/discussions/329
    """
    MBD = "mbd"
    """Unknown light product

    Found as VECINO RGBW as provided by diagnostics
    """
    QCCDZ = "qccdz"
    """AC charging (undocumented)"""
    QJDCZ = "qjdcz"
    """ Unknown product with light capabilities

    Found in some diffusers, plugs and PIR flood lights
    """
    QXJ = "qxj"
    """Temperature and Humidity Sensor with External Probe (undocumented)

    see https://github.com/home-assistant/core/issues/136472
    """
    SFKZQ = "sfkzq"
    """Smart Water Timer (undocumented)"""
    SJZ = "sjz"
    """Electric desk (undocumented)"""
    SZJCY = "szjcy"
    """Water tester (undocumented)"""
    SZJQR = "szjqr"
    """Fingerbot (undocumented)"""
    SWTZ = "swtz"
    """Cooking thermometer (undocumented)"""
    TDQ = "tdq"
    """Dimmer (undocumented)"""
    TYD = "tyd"
    """Outdoor flood light (undocumented)"""
    VOC = "voc"
    """Volatile Organic Compound Sensor (undocumented)"""
    WG2 = "wg2"  # Documented, but not in official list
    """Gateway control

    https://developer.tuya.com/en/docs/iot/wg?id=Kbcdadk79ejok
    """
    WKCZ = "wkcz"
    """Two-way temperature and humidity switch (undocumented)

    "MOES Temperature and Humidity Smart Switch Module MS-103"
    """
    WKF = "wkf"
    """Thermostatic Radiator Valve (undocumented)"""
    WNYKQ = "wnykq"
    """Smart WiFi IR Remote (undocumented)

    eMylo Smart WiFi IR Remote
    Air Conditioner Mate (Smart IR Socket)
    """
    WXKG = "wxkg"  # Documented, but not in official list
    """Wireless Switch

    https://developer.tuya.com/en/docs/iot/s?id=Kbeoa9fkv6brp
    """
    XNYJCN = "xnyjcn"
    """Micro Storage Inverter

        Energy storage and solar PV inverter system with monitoring capabilities
    """
    YWCGQ = "ywcgq"
    """Tank Level Sensor (undocumented)"""
    ZNNBQ = "znnbq"
    """VESKA-micro inverter (undocumented)"""
    ZWJCY = "zwjcy"
    """Soil sensor - plant monitor (undocumented)"""
    ZNJXS = "znjxs"
    """Hejhome whitelabel Fingerbot (undocumented)"""
    ZNRB = "znrb"
    """Pool HeatPump (undocumented)"""


class DPCode(StrEnum):
    """Data Point Codes used by Tuya.

    https://developer.tuya.com/en/docs/iot/standarddescription?id=K9i5ql6waswzq
    """

    ADD_ELE = "add_ele"  # energy
    AIR_QUALITY = "air_quality"
    AIR_QUALITY_INDEX = "air_quality_index"
    ALARM_DELAY_TIME = "alarm_delay_time"
    ALARM_MESSAGE = "alarm_message"
    ALARM_MSG = "alarm_msg"
    ALARM_SWITCH = "alarm_switch"  # Alarm switch
    ALARM_TIME = "alarm_time"  # Alarm time
    ALARM_VOLUME = "alarm_volume"  # Alarm volume
    ANGLE_HORIZONTAL = "angle_horizontal"
    ANGLE_VERTICAL = "angle_vertical"
    ANION = "anion"  # Ionizer unit
    ARM_DOWN_PERCENT = "arm_down_percent"
    ARM_UP_PERCENT = "arm_up_percent"
    ATMOSPHERIC_PRESSTURE = "atmospheric_pressture"  # Typo is in Tuya API
    BACKUP_RESERVE = "backup_reserve"
    BASIC_ANTI_FLICKER = "basic_anti_flicker"
    BASIC_DEVICE_VOLUME = "basic_device_volume"
    BASIC_FLIP = "basic_flip"
    BASIC_INDICATOR = "basic_indicator"
    BASIC_NIGHTVISION = "basic_nightvision"
    BASIC_OSD = "basic_osd"
    BASIC_PRIVATE = "basic_private"
    BASIC_WDR = "basic_wdr"
    BATTERY = "battery"  # Used by non-standard contact sensor implementations
    BATTERY_PERCENTAGE = "battery_percentage"  # Battery percentage
    BATTERY_POWER = "battery_power"
    BATTERY_STATE = "battery_state"  # Battery state
    BATTERY_VALUE = "battery_value"  # Battery value
    BRIGHT_CONTROLLER = "bright_controller"
    BRIGHT_STATE = "bright_state"  # Brightness status
    BRIGHT_VALUE = "bright_value"  # Brightness
    BRIGHT_VALUE_1 = "bright_value_1"
    BRIGHT_VALUE_2 = "bright_value_2"
    BRIGHT_VALUE_3 = "bright_value_3"
    BRIGHT_VALUE_V2 = "bright_value_v2"
    BRIGHTNESS_MAX_1 = "brightness_max_1"
    BRIGHTNESS_MAX_2 = "brightness_max_2"
    BRIGHTNESS_MAX_3 = "brightness_max_3"
    BRIGHTNESS_MIN_1 = "brightness_min_1"
    BRIGHTNESS_MIN_2 = "brightness_min_2"
    BRIGHTNESS_MIN_3 = "brightness_min_3"
    C_F = "c_f"  # Temperature unit switching
    CAT_WEIGHT = "cat_weight"
    CH2O_STATE = "ch2o_state"
    CH2O_VALUE = "ch2o_value"
    CH4_SENSOR_STATE = "ch4_sensor_state"
    CH4_SENSOR_VALUE = "ch4_sensor_value"
    CHARGE_STATE = "charge_state"
    CHILD_LOCK = "child_lock"  # Child lock
    CISTERN = "cistern"
    CLEAN_AREA = "clean_area"
    CLEAN_TIME = "clean_time"
    CLICK_SUSTAIN_TIME = "click_sustain_time"
    CLOSED_OPENED_KIT = "closed_opened_kit"
    CLOUD_RECIPE_NUMBER = "cloud_recipe_number"
    CO_STATE = "co_state"
    CO_STATUS = "co_status"
    CO_VALUE = "co_value"
    CO2_STATE = "co2_state"
    CO2_VALUE = "co2_value"  # CO2 concentration
    COLLECTION_MODE = "collection_mode"
    COLOR_DATA_V2 = "color_data_v2"
    COLOUR_DATA = "colour_data"  # Colored light mode
    COLOUR_DATA_HSV = "colour_data_hsv"  # Colored light mode
    COLOUR_DATA_V2 = "colour_data_v2"  # Colored light mode
    CONCENTRATION_SET = "concentration_set"  # Concentration setting
    CONTROL = "control"
    CONTROL_2 = "control_2"
    CONTROL_3 = "control_3"
    CONTROL_BACK = "control_back"
    CONTROL_BACK_MODE = "control_back_mode"
    COOK_TEMPERATURE = "cook_temperature"
    COOK_TEMPERATURE_2 = "cook_temperature_2"
    COOK_TIME = "cook_time"
    COUNTDOWN = "countdown"  # Countdown
    COUNTDOWN_1 = "countdown_1"
    COUNTDOWN_2 = "countdown_2"
    COUNTDOWN_3 = "countdown_3"
    COUNTDOWN_4 = "countdown_4"
    COUNTDOWN_5 = "countdown_5"
    COUNTDOWN_6 = "countdown_6"
    COUNTDOWN_7 = "countdown_7"
    COUNTDOWN_8 = "countdown_8"
    COUNTDOWN_LEFT = "countdown_left"
    COUNTDOWN_SET = "countdown_set"  # Countdown setting
    CRY_DETECTION_SWITCH = "cry_detection_switch"
    CUML_E_EXPORT_OFFGRID1 = "cuml_e_export_offgrid1"
    CUMULATIVE_ENERGY_CHARGED = "cumulative_energy_charged"
    CUMULATIVE_ENERGY_DISCHARGED = "cumulative_energy_discharged"
    CUMULATIVE_ENERGY_GENERATED_PV = "cumulative_energy_generated_pv"
    CUMULATIVE_ENERGY_OUTPUT_INV = "cumulative_energy_output_inv"
    CUP_NUMBER = "cup_number"  # NUmber of cups
    CUR_CURRENT = "cur_current"  # Actual current
    CUR_NEUTRAL = "cur_neutral"  # Total reverse energy
    CUR_POWER = "cur_power"  # Actual power
    CUR_VOLTAGE = "cur_voltage"  # Actual voltage
    CURRENT_SOC = "current_soc"
    DECIBEL_SENSITIVITY = "decibel_sensitivity"
    DECIBEL_SWITCH = "decibel_switch"
    DEHUMIDITY_SET_ENUM = "dehumidify_set_enum"
    DEHUMIDITY_SET_VALUE = "dehumidify_set_value"
    DELAY_SET = "delay_set"
    DISINFECTION = "disinfection"
    DO_NOT_DISTURB = "do_not_disturb"
    DOORCONTACT_STATE = "doorcontact_state"  # Status of door window sensor
    DOORCONTACT_STATE_2 = "doorcontact_state_2"
    DOORCONTACT_STATE_3 = "doorcontact_state_3"
    DUSTER_CLOTH = "duster_cloth"
    ECO2 = "eco2"
    EDGE_BRUSH = "edge_brush"
    ELECTRICITY_LEFT = "electricity_left"
    FAN_BEEP = "fan_beep"  # Sound
    FAN_COOL = "fan_cool"  # Cool wind
    FAN_DIRECTION = "fan_direction"  # Fan direction
    FAN_HORIZONTAL = "fan_horizontal"  # Horizontal swing flap angle
    FAN_MODE = "fan_mode"
    FAN_SPEED = "fan_speed"
    FAN_SPEED_ENUM = "fan_speed_enum"  # Speed mode
    FAN_SPEED_PERCENT = "fan_speed_percent"  # Stepless speed
    FAN_SWITCH = "fan_switch"
    FAN_VERTICAL = "fan_vertical"  # Vertical swing flap angle
    FAR_DETECTION = "far_detection"
    FAULT = "fault"
    FEED_REPORT = "feed_report"
    FEED_STATE = "feed_state"
    FEEDIN_POWER_LIMIT_ENABLE = "feedin_power_limit_enable"
    FILTER = "filter"
    FILTER_DURATION = "filter_life"  # Filter duration (hours)
    FILTER_LIFE = "filter"  # Filter life (percentage)
    FILTER_RESET = "filter_reset"  # Filter (cartridge) reset
    FLOODLIGHT_LIGHTNESS = "floodlight_lightness"
    FLOODLIGHT_SWITCH = "floodlight_switch"
    FORWARD_ENERGY_TOTAL = "forward_energy_total"
    FROST = "frost"  # Frost protection
    GAS_SENSOR_STATE = "gas_sensor_state"
    GAS_SENSOR_STATUS = "gas_sensor_status"
    GAS_SENSOR_VALUE = "gas_sensor_value"
    HUMIDIFIER = "humidifier"  # Humidification
    HUMIDITY = "humidity"  # Humidity
    HUMIDITY_CURRENT = "humidity_current"  # Current humidity
    HUMIDITY_INDOOR = "humidity_indoor"  # Indoor humidity
    HUMIDITY_OUTDOOR = "humidity_outdoor"  # Outdoor humidity
    HUMIDITY_OUTDOOR_1 = "humidity_outdoor_1"  # Outdoor humidity
    HUMIDITY_OUTDOOR_2 = "humidity_outdoor_2"  # Outdoor humidity
    HUMIDITY_OUTDOOR_3 = "humidity_outdoor_3"  # Outdoor humidity
    HUMIDITY_SET = "humidity_set"  # Humidity setting
    HUMIDITY_VALUE = "humidity_value"  # Humidity
    INSTALLATION_HEIGHT = "installation_height"
    INVERTER_OUTPUT_POWER = "inverter_output_power"
    IPC_WORK_MODE = "ipc_work_mode"
    LED_TYPE_1 = "led_type_1"
    LED_TYPE_2 = "led_type_2"
    LED_TYPE_3 = "led_type_3"
    LEVEL = "level"
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_CURRENT = "level_current"
    LIGHT = "light"  # Light
    LIGHT_MODE = "light_mode"
    LIQUID_DEPTH = "liquid_depth"
    LIQUID_DEPTH_MAX = "liquid_depth_max"
    LIQUID_LEVEL_PERCENT = "liquid_level_percent"
    LIQUID_STATE = "liquid_state"
    LOCK = "lock"  # Lock / Child lock
    MACH_OPERATE = "mach_operate"
    MANUAL_FEED = "manual_feed"
    MASTER_MODE = "master_mode"  # alarm mode
    MASTER_STATE = "master_state"  # alarm state
    MATERIAL = "material"  # Material
    MAX_SET = "max_set"
    MINI_SET = "mini_set"
    MODE = "mode"  # Working mode / Mode
    MOODLIGHTING = "moodlighting"  # Mood light
    MOTION_RECORD = "motion_record"
    MOTION_SENSITIVITY = "motion_sensitivity"
    MOTION_SWITCH = "motion_switch"  # Motion switch
    MOTION_TRACKING = "motion_tracking"
    MOVEMENT_DETECT_PIC = "movement_detect_pic"
    MUFFLING = "muffling"  # Muffling
    NEAR_DETECTION = "near_detection"
    OPPOSITE = "opposite"
    OUTPUT_POWER_LIMIT = "output_power_limit"
    OXYGEN = "oxygen"  # Oxygen bar
    PAUSE = "pause"
    PERCENT_CONTROL = "percent_control"
    PERCENT_CONTROL_2 = "percent_control_2"
    PERCENT_CONTROL_3 = "percent_control_3"
    PERCENT_STATE = "percent_state"
    PERCENT_STATE_2 = "percent_state_2"
    PERCENT_STATE_3 = "percent_state_3"
    PHASE_A = "phase_a"
    PHASE_B = "phase_b"
    PHASE_C = "phase_c"
    PIR = "pir"  # Motion sensor
    PM1 = "pm1"
    PM10 = "pm10"
    PM25 = "pm25"
    PM25_STATE = "pm25_state"
    PM25_VALUE = "pm25_value"
    POSITION = "position"
    POWDER_SET = "powder_set"  # Powder
    POWER = "power"
    POWER_GO = "power_go"
    POWER_TOTAL = "power_total"
    PREHEAT = "preheat"
    PREHEAT_1 = "preheat_1"
    PREHEAT_2 = "preheat_2"
    PRESENCE_STATE = "presence_state"
    PRESSURE_STATE = "pressure_state"
    PRESSURE_VALUE = "pressure_value"
    PRO_ADD_ELE = "pro_add_ele"  # Produce energy
    PUMP = "pump"
    PUMP_RESET = "pump_reset"  # Water pump reset
    PUMP_TIME = "pump_time"  # Water pump duration
    PV_POWER_CHANNEL_1 = "pv_power_channel_1"
    PV_POWER_CHANNEL_2 = "pv_power_channel_2"
    PV_POWER_TOTAL = "pv_power_total"
    RAIN_24H = "rain_24h"  # Total daily rainfall in mm
    RAIN_RATE = "rain_rate"  # Rain intensity in mm/h
    RECORD_MODE = "record_mode"
    RECORD_SWITCH = "record_switch"  # Recording switch
    RELAY_STATUS = "relay_status"
    REMAIN_TIME = "remain_time"
    RESET_DUSTER_CLOTH = "reset_duster_cloth"
    RESET_EDGE_BRUSH = "reset_edge_brush"
    RESET_FILTER = "reset_filter"
    RESET_MAP = "reset_map"
    RESET_ROLL_BRUSH = "reset_roll_brush"
    REVERSE_ENERGY_TOTAL = "reverse_energy_total"
    ROLL_BRUSH = "roll_brush"
    SEEK = "seek"
    SENSITIVITY = "sensitivity"  # Sensitivity
    SENSOR_HUMIDITY = "sensor_humidity"
    SENSOR_TEMPERATURE = "sensor_temperature"
    SHAKE = "shake"  # Oscillating
    SHOCK_STATE = "shock_state"  # Vibration status
    SIREN_SWITCH = "siren_switch"
    SITUATION_SET = "situation_set"
    SLEEP = "sleep"  # Sleep function
    SLOW_FEED = "slow_feed"
    SMOKE_SENSOR_STATE = "smoke_sensor_state"
    SMOKE_SENSOR_STATUS = "smoke_sensor_status"
    SMOKE_SENSOR_VALUE = "smoke_sensor_value"
    SNOOZE = "snooze"
    SOS = "sos"  # Emergency State
    SOS_STATE = "sos_state"  # Emergency mode
    SPEED = "speed"  # Speed level
    SPRAY_MODE = "spray_mode"  # Spraying mode
    START = "start"  # Start
    STATUS = "status"
    STERILIZATION = "sterilization"  # Sterilization
    SUCTION = "suction"
    SUPPLY_FREQUENCY = "supply_frequency"
    SWING = "swing"  # Swing mode
    SWITCH = "switch"  # Switch
    SWITCH_1 = "switch_1"  # Switch 1
    SWITCH_2 = "switch_2"  # Switch 2
    SWITCH_3 = "switch_3"  # Switch 3
    SWITCH_4 = "switch_4"  # Switch 4
    SWITCH_5 = "switch_5"  # Switch 5
    SWITCH_6 = "switch_6"  # Switch 6
    SWITCH_7 = "switch_7"  # Switch 7
    SWITCH_8 = "switch_8"  # Switch 8
    SWITCH_ALARM_LIGHT = "switch_alarm_light"
    SWITCH_ALARM_SOUND = "switch_alarm_sound"
    SWITCH_BACKLIGHT = "switch_backlight"  # Backlight switch
    SWITCH_CHARGE = "switch_charge"
    SWITCH_CONTROLLER = "switch_controller"
    SWITCH_DISTURB = "switch_disturb"
    SWITCH_FAN = "switch_fan"
    SWITCH_HORIZONTAL = "switch_horizontal"  # Horizontal swing flap switch
    SWITCH_LED = "switch_led"  # Switch
    SWITCH_LED_1 = "switch_led_1"
    SWITCH_LED_2 = "switch_led_2"
    SWITCH_LED_3 = "switch_led_3"
    SWITCH_MODE1 = "switch_mode1"
    SWITCH_MODE2 = "switch_mode2"
    SWITCH_MODE3 = "switch_mode3"
    SWITCH_MODE4 = "switch_mode4"
    SWITCH_MODE5 = "switch_mode5"
    SWITCH_MODE6 = "switch_mode6"
    SWITCH_MODE7 = "switch_mode7"
    SWITCH_MODE8 = "switch_mode8"
    SWITCH_MODE9 = "switch_mode9"
    SWITCH_MUSIC = "switch_music"
    SWITCH_NIGHT_LIGHT = "switch_night_light"
    SWITCH_SAVE_ENERGY = "switch_save_energy"
    SWITCH_SOUND = "switch_sound"  # Voice switch
    SWITCH_SPRAY = "switch_spray"  # Spraying switch
    SWITCH_USB1 = "switch_usb1"  # USB 1
    SWITCH_USB2 = "switch_usb2"  # USB 2
    SWITCH_USB3 = "switch_usb3"  # USB 3
    SWITCH_USB4 = "switch_usb4"  # USB 4
    SWITCH_USB5 = "switch_usb5"  # USB 5
    SWITCH_USB6 = "switch_usb6"  # USB 6
    SWITCH_VERTICAL = "switch_vertical"  # Vertical swing flap switch
    SWITCH_VOICE = "switch_voice"  # Voice switch
    TARGET_DIS_CLOSEST = "target_dis_closest"  # Closest target distance
    TDS_IN = "tds_in"  # Total dissolved solids
    TEMP = "temp"  # Temperature setting
    TEMP_BOILING_C = "temp_boiling_c"
    TEMP_BOILING_F = "temp_boiling_f"
    TEMP_CONTROLLER = "temp_controller"
    TEMP_CORRECTION = "temp_correction"
    TEMP_CURRENT = "temp_current"  # Current temperature in °C
    TEMP_CURRENT_2 = "temp_current_2"
    TEMP_CURRENT_EXTERNAL = (
        "temp_current_external"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_1 = (
        "temp_current_external_1"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_2 = (
        "temp_current_external_2"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_3 = (
        "temp_current_external_3"  # Current external temperature in Celsius
    )
    TEMP_CURRENT_EXTERNAL_F = (
        "temp_current_external_f"  # Current external temperature in Fahrenheit
    )
    TEMP_CURRENT_F = "temp_current_f"  # Current temperature in °F
    TEMP_INDOOR = "temp_indoor"  # Indoor temperature in °C
    TEMP_SET = "temp_set"  # Set the temperature in °C
    TEMP_SET_F = "temp_set_f"  # Set the temperature in °F
    TEMP_UNIT_CONVERT = "temp_unit_convert"  # Temperature unit switching
    TEMP_VALUE = "temp_value"  # Color temperature
    TEMP_VALUE_V2 = "temp_value_v2"
    TEMPER_ALARM = "temper_alarm"  # Tamper alarm
    TIME_TOTAL = "time_total"
    TIME_USE = "time_use"  # Total seconds of irrigation
    TOTAL_CLEAN_AREA = "total_clean_area"
    TOTAL_CLEAN_COUNT = "total_clean_count"
    TOTAL_CLEAN_TIME = "total_clean_time"
    TOTAL_FORWARD_ENERGY = "total_forward_energy"
    TOTAL_PM = "total_pm"
    TOTAL_POWER = "total_power"
    TOTAL_TIME = "total_time"
    TVOC = "tvoc"
    UP_DOWN = "up_down"
    UPPER_TEMP = "upper_temp"
    UPPER_TEMP_F = "upper_temp_f"
    UV = "uv"  # UV sterilization
    UV_INDEX = "uv_index"
    UV_RUNTIME = "uv_runtime"  # UV runtime
    VA_BATTERY = "va_battery"
    VA_HUMIDITY = "va_humidity"
    VA_TEMPERATURE = "va_temperature"
    VALVE_STATE = "valve_state"
    VOC_STATE = "voc_state"
    VOC_VALUE = "voc_value"
    VOICE_SWITCH = "voice_switch"
    VOICE_TIMES = "voice_times"
    VOLUME_SET = "volume_set"
    WARM = "warm"  # Heat preservation
    WARM_TIME = "warm_time"  # Heat preservation time
    WATER = "water"
    WATER_LEVEL = "water_level"
    WATER_RESET = "water_reset"  # Resetting of water usage days
    WATER_SET = "water_set"  # Water level
    WATER_TIME = "water_time"  # Water usage duration
    WATERSENSOR_STATE = "watersensor_state"
    WEATHER_DELAY = "weather_delay"
    WET = "wet"  # Humidification
    WINDOW_CHECK = "window_check"
    WINDOW_STATE = "window_state"
    WINDSPEED = "windspeed"
    WINDSPEED_AVG = "windspeed_avg"
    WIND_DIRECT = "wind_direct"
    WIRELESS_BATTERYLOCK = "wireless_batterylock"
    WIRELESS_ELECTRICITY = "wireless_electricity"
    WORK_MODE = "work_mode"  # Working mode
    WORK_POWER = "work_power"
    WORK_STATE_E = "work_state_e"


@dataclass
class UnitOfMeasurement:
    """Describes a unit of measurement."""

    unit: str
    device_classes: set[str]

    aliases: set[str] = field(default_factory=set)


# A tuple of available units of measurements we can work with.
# Tuya's devices aren't consistent in UOM use, thus this provides
# a list of aliases for units and possible conversions we can do
# to make them compatible with our model.
UNITS = (
    UnitOfMeasurement(
        unit="",
        aliases={" "},
        device_classes={
            SensorDeviceClass.AQI,
            SensorDeviceClass.DATE,
            SensorDeviceClass.MONETARY,
            SensorDeviceClass.TIMESTAMP,
        },
    ),
    UnitOfMeasurement(
        unit=PERCENTAGE,
        aliases={"pct", "percent", "% RH"},
        device_classes={
            SensorDeviceClass.BATTERY,
            SensorDeviceClass.HUMIDITY,
            SensorDeviceClass.POWER_FACTOR,
        },
    ),
    UnitOfMeasurement(
        unit=CONCENTRATION_PARTS_PER_MILLION,
        device_classes={
            SensorDeviceClass.CO,
            SensorDeviceClass.CO2,
        },
    ),
    UnitOfMeasurement(
        unit=CONCENTRATION_PARTS_PER_BILLION,
        device_classes={
            SensorDeviceClass.CO,
            SensorDeviceClass.CO2,
        },
    ),
    UnitOfMeasurement(
        unit=UnitOfElectricCurrent.AMPERE,
        aliases={"a", "ampere"},
        device_classes={SensorDeviceClass.CURRENT},
    ),
    UnitOfMeasurement(
        unit=UnitOfElectricCurrent.MILLIAMPERE,
        aliases={"ma", "milliampere"},
        device_classes={SensorDeviceClass.CURRENT},
    ),
    UnitOfMeasurement(
        unit=UnitOfEnergy.WATT_HOUR,
        aliases={"wh", "watthour"},
        device_classes={SensorDeviceClass.ENERGY},
    ),
    UnitOfMeasurement(
        unit=UnitOfEnergy.KILO_WATT_HOUR,
        aliases={"kwh", "kilowatt-hour", "kW·h", "kW.h"},
        device_classes={SensorDeviceClass.ENERGY},
    ),
    UnitOfMeasurement(
        unit=UnitOfVolume.CUBIC_FEET,
        aliases={"ft3"},
        device_classes={SensorDeviceClass.GAS},
    ),
    UnitOfMeasurement(
        unit=UnitOfVolume.CUBIC_METERS,
        aliases={"m3"},
        device_classes={SensorDeviceClass.GAS},
    ),
    UnitOfMeasurement(
        unit=UnitOfVolumetricFlux.MILLIMETERS_PER_HOUR,
        aliases={"mm"},
        device_classes={SensorDeviceClass.PRECIPITATION_INTENSITY},
    ),
    UnitOfMeasurement(
        unit=LIGHT_LUX,
        aliases={"lux"},
        device_classes={SensorDeviceClass.ILLUMINANCE},
    ),
    UnitOfMeasurement(
        unit=CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        # The μ-char has 2 unicode variants \u00b5 and \u03bc
        # The \u03bc variant (Greek Mu char) is recommended
        aliases={"ug/m3", "\u03bcg/m3", "\u00b5g/m3", "ug/m³"},
        device_classes={
            SensorDeviceClass.NITROGEN_DIOXIDE,
            SensorDeviceClass.NITROGEN_MONOXIDE,
            SensorDeviceClass.NITROUS_OXIDE,
            SensorDeviceClass.OZONE,
            SensorDeviceClass.PM1,
            SensorDeviceClass.PM25,
            SensorDeviceClass.PM10,
            SensorDeviceClass.SULPHUR_DIOXIDE,
            SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
        },
    ),
    UnitOfMeasurement(
        unit=CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        aliases={"mg/m3"},
        device_classes={
            SensorDeviceClass.NITROGEN_DIOXIDE,
            SensorDeviceClass.NITROGEN_MONOXIDE,
            SensorDeviceClass.NITROUS_OXIDE,
            SensorDeviceClass.OZONE,
            SensorDeviceClass.PM1,
            SensorDeviceClass.PM25,
            SensorDeviceClass.PM10,
            SensorDeviceClass.SULPHUR_DIOXIDE,
            SensorDeviceClass.VOLATILE_ORGANIC_COMPOUNDS,
        },
    ),
    UnitOfMeasurement(
        unit=UnitOfPower.WATT,
        aliases={"watt"},
        device_classes={SensorDeviceClass.POWER},
    ),
    UnitOfMeasurement(
        unit=UnitOfPower.KILO_WATT,
        aliases={"kilowatt"},
        device_classes={SensorDeviceClass.POWER},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.BAR,
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.MBAR,
        aliases={"millibar"},
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.HPA,
        aliases={"hpa", "hectopascal"},
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.INHG,
        aliases={"inhg"},
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.PSI,
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfPressure.PA,
        device_classes={SensorDeviceClass.PRESSURE},
    ),
    UnitOfMeasurement(
        unit=SIGNAL_STRENGTH_DECIBELS,
        aliases={"db"},
        device_classes={SensorDeviceClass.SIGNAL_STRENGTH},
    ),
    UnitOfMeasurement(
        unit=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        aliases={"dbm"},
        device_classes={SensorDeviceClass.SIGNAL_STRENGTH},
    ),
    UnitOfMeasurement(
        unit=UnitOfTemperature.CELSIUS,
        aliases={"°c", "c", "celsius", "℃"},
        device_classes={SensorDeviceClass.TEMPERATURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfTemperature.FAHRENHEIT,
        aliases={"°f", "f", "fahrenheit"},
        device_classes={SensorDeviceClass.TEMPERATURE},
    ),
    UnitOfMeasurement(
        unit=UnitOfElectricPotential.VOLT,
        aliases={"volt"},
        device_classes={SensorDeviceClass.VOLTAGE},
    ),
    UnitOfMeasurement(
        unit=UnitOfElectricPotential.MILLIVOLT,
        aliases={"mv", "millivolt"},
        device_classes={SensorDeviceClass.VOLTAGE},
    ),
)


DEVICE_CLASS_UNITS: dict[str, dict[str, UnitOfMeasurement]] = {}
for uom in UNITS:
    for device_class in uom.device_classes:
        DEVICE_CLASS_UNITS.setdefault(device_class, {})[uom.unit] = uom
        for unit_alias in uom.aliases:
            DEVICE_CLASS_UNITS[device_class][unit_alias] = uom
