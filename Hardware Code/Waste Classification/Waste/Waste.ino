#include <ArduinoJson.h>
#include <DeltaKinematics.h>
#include <FlexyStepper.h>
#include <Servo.h>

#define STEPS 400
#define SPEED 800
#define ACCELERATE 400

DeltaKinematics DK(91, 310, 40, 100);
//DK(Bicep, forearm, End effector Radius, base-platform Radius)


FlexyStepper stepper1;
FlexyStepper stepper2;
FlexyStepper stepper3;

Servo motor;
Servo solenoid;

String cmd;
float cor[3];
String label;
char *token;

void suction_on() {
  motor.write(180);   // motor On
  solenoid.write(0);  //close solenoid
}

void suction_off() {
  motor.write(0);       // motor off
  solenoid.write(180);  //open solenoid no suck either
}

void setup() {
  Serial.begin(115200);
  motor.attach(13);
  solenoid.attach(12);
  stepper1.connectToPins(2, 5);
  stepper2.connectToPins(3, 6);
  stepper3.connectToPins(4, 7);
  stepper1.setSpeedInStepsPerSecond(SPEED);
  stepper1.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
  stepper2.setSpeedInStepsPerSecond(SPEED);
  stepper2.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
  stepper3.setSpeedInStepsPerSecond(SPEED);
  stepper3.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
}

void loop() {
  if (Serial.available() > 0) {
    cmd = Serial.readStringUntil('\r');
    token = strtok(cmd.c_str(), ",");
    for (int i = 0; i < 3; i++) {
      cor[i] = atof(token);
      token = strtok(NULL, ",");
    }
    label = token;
    DK.x = cor[0];
    DK.y = cor[1];
    DK.z = cor[2];
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    if (label == "none") {
      DK.x = 0;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
    } else if (label == "0") {
      // Coordinate to store = 0, 140
      suction_on();
      delay(1000);
      DK.x = 0;
      DK.y = 140;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
      suction_off();
      delay(500);
      DK.x = 0;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
    } else if (label == "1") {
      // metal
      suction_on();
      delay(1000);
      DK.x = 0;
      DK.y = -140;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
      suction_off();
      delay(500);
      DK.x = 0;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
    } else if (label == "2") {
      suction_on();
      delay(1000);
      DK.x = -140;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
      suction_off();
      delay(500);
      DK.x = 0;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
    }

    else if (label == "3") {
      suction_on();
      delay(1000);
      DK.x = 140;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
      suction_off();
      delay(500);
      DK.x = 0;
      DK.y = 0;
      DK.z = -290;
      DK.inverse();
      stepper_movement(DK.a, DK.b, DK.c);
      delay(1000);
    }
  }
}

void stepper_movement(float theta1, float theta2, float theta3) {
  int steps1 = (theta1 * STEPS) / 360;
  int steps2 = (theta2 * STEPS) / 360;
  int steps3 = (theta3 * STEPS) / 360;
  stepper1.setTargetPositionInSteps(steps1);
  stepper2.setTargetPositionInSteps(steps2);
  stepper3.setTargetPositionInSteps(steps3);
  while ((!stepper1.motionComplete()) || (!stepper2.motionComplete()) || (!stepper3.motionComplete())) {
    stepper1.processMovement();
    stepper2.processMovement();
    stepper3.processMovement();
  }
  //   stepper1.moveRelativeInSteps(steps1);
  // stepper2.moveRelativeInSteps(steps2);
  // stepper3.moveRelativeInSteps(steps3);
}