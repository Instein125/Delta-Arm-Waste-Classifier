#include <DeltaKinematics.h>
#include <FlexyStepper.h>
#include <Servo.h>

#define STEPS 400
#define SPEED 400
#define ACCELERATE 200

DeltaKinematics DK(91, 310, 40, 100);
//DK(Bicep, forearm, End effector Radius, base-platform Radius)
FlexyStepper stepper1;
FlexyStepper stepper2;
FlexyStepper stepper3;

Servo solenoid;
Servo motor;
void suction_on() {
  motor.write(180);   // motor On
  solenoid.write(0);  //close solenoid
  Serial.println("Suction ON");
  delay(1000);
}

void suction_off() {
  motor.write(0);       // motor off
  solenoid.write(180);  //open solenoid no suck either
}


void setup() {
  Serial.begin(115200);
  solenoid.attach(12);
  motor.attach(13);
  stepper1.connectToPins(2, 5);
  stepper2.connectToPins(3, 6);
  stepper3.connectToPins(4, 7);
  // stepper1.setStepsPerRevolution(STEPS);
  stepper1.setSpeedInStepsPerSecond(SPEED);
  stepper1.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
  // stepper2.setStepsPerRevolution(STEPS);
  stepper2.setSpeedInStepsPerSecond(SPEED);
  stepper2.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
  // stepper3.setStepsPerRevolution(STEPS);
  stepper3.setSpeedInStepsPerSecond(SPEED);
  stepper3.setAccelerationInStepsPerSecondPerSecond(ACCELERATE);
}

void loop() {

  // DK.a =  0;
  // DK.b =  0;
  // DK.c = 0;
  // DK.forward();
  // stepper1.moveToPositionInSteps(800);
  // delay(2000);
  // stepper1.moveToPositionInSteps(1600);
  // delay(2000);
  // stepper1.moveToPositionInSteps(0);
  // delay(2000);
  // Serial.println(String(DK.x)+","+String(DK.y)+","+String(DK.z));
  // Serial.println(String(DK.a)+","+String(DK.b)+","+String(DK.c));
  // Serial.println();
  // delay(3000);

  // DK.a = 0;
  // DK.b = 0;
  // DK.c= 0;
  // DK.forward();
  // Serial.println(String(DK.x)+","+String(DK.y)+","+String(DK.z));
  // Serial.println(String(DK.a)+","+String(DK.b)+","+String(DK.c));
  // delay(3000);
  // DK.x = 120;
  // DK.y = 120;
  // DK.z = -270;
  // DK.inverse();
  // stepper_movement(DK.a,DK.b,DK.c);
  // delay(2000);
  // DK.x = -120;
  // DK.y = -120;
  // DK.z = -270;
  // DK.inverse();
  // stepper_movement(DK.a,DK.b,DK.c);
  // delay(2000);
  // Serial.println("Enter the value of x-cordinate(-120 to 120)");
  // while (!Serial.available())
  //   ;
  // DK.x = Serial.readString().toFloat();
  // Serial.println(DK.x);
  // Serial.println("Enter the value of y-cordinate(-120 to 120)");
  // while (!Serial.available())
  //   ;
  // DK.y = Serial.readString().toFloat();
  // Serial.println(DK.y);
  // // Serial.println("Enter the value of z-cordinate(-428.939 to -189.673)");
  // while (!Serial.available())
  //   ;
  // float z = Serial.readString().toFloat();
  // Serial.println(DK.z);
  // DK.inverse();
  // Serial.println(String(DK.x) + "," + String(DK.y) + "," + String(DK.z));
  // Serial.println(String(DK.a) + "," + String(DK.b) + "," + String(DK.c));
  // stepper_movement(DK.a,DK.b,DK.c);
  float a = 0;
  Serial.println("Enter zero");
  while (!Serial.available())
    ;
  a = Serial.readString().toFloat();

  while (a == 0) {
    DK.x = 0;
    DK.y = 0;
    DK.z = -290;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    DK.x = 0;
    DK.y = 0;
    DK.z = -400;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    suction_on();
    delay(500);
    DK.x = 0;
    DK.y = 0;
    DK.z = -350;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    DK.x = 70;
    DK.y = 0;
    DK.z = -350;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    DK.x = 70;
    DK.y = 0;
    DK.z = -380;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    suction_off();
    delay(1000);
    DK.x = 70;
    DK.y = 0;
    DK.z = -350;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    DK.x = 70;
    DK.y = 0;
    DK.z = -400;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    suction_on();
    delay(1000);
    DK.x = 0;
    DK.y = 0;
    DK.z = -290;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    delay(1000);
    DK.x = 0;
    DK.y = 0;
    DK.z = -380;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    suction_off();
    delay(1000);
    DK.x = 0;
    DK.y = 0;
    DK.z = -290;
    DK.inverse();
    stepper_movement(DK.a, DK.b, DK.c);
    a = 4;
  }
  // DK.x=0;
  // DK.y=0;
  // DK.z=-290;
  // DK.inverse();
  // stepper_movement(DK.a,DK.b,DK.c);
  // delay(100);
  // DK.x=0;
  // DK.y=0;
  // DK.z=-360;
  // DK.inverse();
  // stepper_movement(DK.a,DK.b,DK.c);
  // DK.x=-30;
  // DK.y=-30;
  // DK.z=-290;
  // DK.inverse();
  // stepper_movement(DK.a,DK.b,DK.c);
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
