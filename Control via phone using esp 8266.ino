#define BLYNK_PRINT Serial
#define BLYNK_TEMPLATE_ID           "TMPL36VGmwsE7"
#define BLYNK_TEMPLATE_NAME         "sih"
#define BLYNK_AUTH_TOKEN "eribvlkKj0UGAt7x7GUwujw0icBqiY6C"
#define MOTOR_ENABLE1 D0 // Continuous power for Motor 1
#define MOTOR_ENABLE2 D5 // Continuous power for Motor 2
#define MOTOR1_FORWARD D1 // Motor 1 Forward
#define MOTOR1_BACKWARD D2 // Motor 1 Backward
#define MOTOR2_FORWARD D3 // Motor 2 Forward
#define MOTOR2_BACKWARD D4 // Motor 2 Backward

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266_SSL.h>

// Your WiFi credentials
char ssid[] = "Eshank"; // Replace with your WiFi SSID
char pass[] = "12345678"; // Replace with your WiFi password

void setup() {
  Serial.begin(115200);
  
  // Set motor control pins as outputs
  pinMode(MOTOR_ENABLE1, OUTPUT);
  pinMode(MOTOR_ENABLE2, OUTPUT);
  pinMode(MOTOR1_FORWARD, OUTPUT);
  pinMode(MOTOR1_BACKWARD, OUTPUT);
  pinMode(MOTOR2_FORWARD, OUTPUT);
  pinMode(MOTOR2_BACKWARD, OUTPUT);
  
  // Set motor enable pins to HIGH for continuous power
  digitalWrite(MOTOR_ENABLE1, HIGH);
  digitalWrite(MOTOR_ENABLE2, HIGH);
  
  // Connect to Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop() {
  Blynk.run();
}

// Blynk button handlers
BLYNK_WRITE(V1) { // Forward
  int value = param.asInt();
  if (value == 1) {
    forward();
  } else {
    stop();
  }
}

BLYNK_WRITE(V2) { // Backward
  int value = param.asInt();
  if (value == 1) {
    backward();
  } else {
    stop();
  }
}

BLYNK_WRITE(V3) { // Left
  int value = param.asInt();
  if (value == 1) {
    left();
  } else {
    stop();
  }
}

BLYNK_WRITE(V4) { // Right
  int value = param.asInt();
  if (value == 1) {
    right();
  } else {
    stop();
  }
}

// Control functions
void forward() {
  digitalWrite(MOTOR1_FORWARD, HIGH);
  digitalWrite(MOTOR1_BACKWARD, LOW);
  digitalWrite(MOTOR2_FORWARD, HIGH);
  digitalWrite(MOTOR2_BACKWARD, LOW);
  Serial.println("Moving Forward");
}

void backward() {
  digitalWrite(MOTOR1_FORWARD, LOW);
  digitalWrite(MOTOR1_BACKWARD, HIGH);
  digitalWrite(MOTOR2_FORWARD, LOW);
  digitalWrite(MOTOR2_BACKWARD, HIGH);
  Serial.println("Moving Backward");
}

void left() {
  digitalWrite(MOTOR1_FORWARD, LOW);
  digitalWrite(MOTOR1_BACKWARD, HIGH); // Reverse left motor
  digitalWrite(MOTOR2_FORWARD, HIGH);
  digitalWrite(MOTOR2_BACKWARD, LOW); // Move right motor forward
  Serial.println("Turning Left");
}

void right() {
  digitalWrite(MOTOR1_FORWARD, HIGH);
  digitalWrite(MOTOR1_BACKWARD, LOW); // Move left motor forward
  digitalWrite(MOTOR2_FORWARD, LOW);
  digitalWrite(MOTOR2_BACKWARD, HIGH); // Reverse right motor
  Serial.println("Turning Right");
}

void stop() {
  digitalWrite(MOTOR1_FORWARD, LOW);
  digitalWrite(MOTOR1_BACKWARD, LOW);
  digitalWrite(MOTOR2_FORWARD, LOW);
  digitalWrite(MOTOR2_BACKWARD, LOW);
  Serial.println("Stopped");
}
