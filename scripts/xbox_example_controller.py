import RPi.GPIO as GPIO
import math
import xbox
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__ == '__main__':
	joy = xbox.Joystick()

	while not joy.Back():
		#Left stick
		leftStickX, leftStickY = joy.leftStick()

		leftStickX = leftStickX * 255
		leftStickY = leftStickY * 255

		leftStickX = int(leftStickX)
		leftStickY = int(leftStickY)

		#Right stick
		rightStickX, rightStickY = joy.rightStick()

		rightStickX = rightStickX * 255
		rightStickY = rightStickY * 255

		rightStickX = int(rightStickX)
		rightStickY = int(rightStickY)


		#Buttons
		buttonA = joy.A()
		buttonB = joy.B()
		buttonX = joy.X()
		buttonY = joy.Y()

		buttonLB = joy.leftBumper()
		buttonRB = joy.rightBumper()

		#Left Trigger
		leftTrigger = joy.leftTrigger()

		leftTrigger = leftTrigger * 255

		leftTrigger = int(leftTrigger)

		#Right Trigger
		rightTrigger = joy.rightTrigger()

		rightTrigger = rightTrigger * 255

		rightTrigger = int(rightTrigger)


		print ("LS X:", leftStickX, "LS Y:", leftStickY, "     |     ", "RS X:", rightStickX, "RS Y:", rightStickY,  "     |     ", "LT:", leftTrigger, "RT:", rightTrigger, "     |     ", "A:", buttonA, "B:", buttonB, "X:", buttonX, "Y:", buttonY,  "     |     ", "LB:", buttonLB, "RB:", buttonRB)

		time.sleep(0.01)

	joy.close()
