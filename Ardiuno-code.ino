const int tempPin = A0;
const int phPin = A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int tempRaw = analogRead(tempPin);
  float voltage = tempRaw * (5.0 / 1023.0);
  float temperature = voltage * 100;  // LM35 sensor logic

  int phRaw = analogRead(phPin);
  float phVoltage = phRaw * (5.0 / 1023.0);
  float ph = 7 + ((2.5 - phVoltage) / 0.18);  // Basic calibration

  Serial.print(temperature);
  Serial.print(",");
  Serial.println(ph);

  delay(1000);  // send data every 1 second
}
// This code reads temperature from an LM35 sensor and pH from a pH sensor,
// converting the analog readings to temperature in Celsius and pH value.