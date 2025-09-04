from esphome.const import CONF_ID
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.core import CORE
from esphome.components import sensor   # NEW

CODEOWNERS = ["@aquaticus"]

DEPENDENCIES = ["wifi"]

snmp_ns = cg.esphome_ns.namespace("snmp")
SNMPComponent = snmp_ns.class_("SNMPComponent", cg.Component)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SNMPComponent),
            cv.Optional("contact", default=""): cv.string_strict,
            cv.Optional("location", default=""): cv.string_strict,
            cv.Optional("read_community", default="public"): cv.string,
            cv.Optional("write_community", default="private"): cv.string,
            cv.Optional("temperature"): cv.use_id(sensor.Sensor), 
            cv.Optional("humidity"): cv.use_id(sensor.Sensor),     
        }
    ),
    cv.only_with_arduino,
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    cg.add(var.set_location(config["location"]))
    cg.add(var.set_contact(config["contact"]))
    cg.add(var.set_read_community(config["read_community"]))
    cg.add(var.set_write_community(config["write_community"]))

    await cg.register_component(var, config)

    if "temperature" in config:
        sens = await cg.get_variable(config["temperature"])
        cg.add(var.set_temperature_sensor(sens))

    if "humidity" in config:
        sens = await cg.get_variable(config["humidity"])
        cg.add(var.set_humidity_sensor(sens))

    if CORE.is_esp8266 or CORE.is_esp32:
        cg.add_library(r"https://github.com/aquaticus/Arduino_SNMP.git", "2.1.0")
