#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace me_sensor {


class MySensor : public PollingComponent, public sensor::Sensor {
public:
    
    void setup() override {
        ESP_LOGD("my_sensor", "Inicjalizacja czujnika");
    }

    void update() override {
        float temperature = random(2000, 3000) / 100.0;  // Losowa temp. 20-30°C
        ESP_LOGD("my_sensor", "Nowa temperatura: %.2f°C", temperature);
        publish_state(temperature);
    }
};

}
}