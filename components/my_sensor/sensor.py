import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, UNIT_CELSIUS, DEVICE_CLASS_TEMPERATURE

my_sensor_ns = cg.esphome_ns.namespace('my_sensor')
MySensor = my_sensor_ns.class_('MySensor', sensor.Sensor)

CONFIG_SCHEMA = sensor.sensor_schema(
    MySensor,
    unit_of_measurement=UNIT_CELSIUS,
    device_class=DEVICE_CLASS_TEMPERATURE
).extend({
    cv.GenerateID(): cv.declare_id(MySensor),
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await sensor.register_sensor(var, config)
