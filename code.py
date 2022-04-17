import board, digitalio, time, analogio, pwmio
import music

# LED setup
#led = digitalio.DigitalInOut(board.GP27)
#led.direction = digitalio.Direction.OUTPUT

# PWM buzzer out 
pwm_buzzer = pwmio.PWMOut(board.GP16, frequency=500, variable_frequency = True)

# PWM led out 
pwm_led = pwmio.PWMOut(board.GP27, frequency=500, variable_frequency = True)

# Inbuilt board LED setup
#led = digitalio.DigitalInOut(board.LED)
#led.direction = digitalio.Direction.OUTPUT

# Button setup
button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT
button.switch_to_input(pull=digitalio.Pull.DOWN)

def volume(pwm_out, fraction):
	volume = fraction * (2**14 - 1)
	print(volume)
	pwm_out.duty_cycle = int(volume)

def siren(pwm_out, reps, seq=None):
	volume(pwm_out, 0.8)
	if not seq:
		cycle = [2**10, 0, 2**9, 0]
	else:
		cycle = [2**s for s in seq]
	gap = 0.5
	for i in range(reps):
		for level in cycle:
			pwm_out.duty_cycle = level
			# print(level)
			time.sleep(gap)
	volume(pwm_out, 0)

def decr_siren(pwm_out, reps, bounds=[11,10]):
	for dev in pwm_out:
		volume(dev, 0.7)
	gap = 0.001
	for i in range(reps):
		for level in range(2**bounds[1], 2**bounds[0],3):
			for dev in pwm_out:
				dev.duty_cycle = level
			time.sleep(gap)

		for dev in pwm_out:
			dev.duty_cycle = 0 
		time.sleep(gap)

		for level in range(2**bounds[0], 2**bounds[1],-3):
			for dev in pwm_out:
				dev.duty_cycle = level
			time.sleep(gap)

		for dev in pwm_out:
			dev.duty_cycle = 0 
		time.sleep(gap)

	for dev in pwm_out:
		volume(dev, 0)


while True:
	if button.value:
		print("Pressed")
		#siren(pwm_led, 3, [15,13])
		siren(pwm_buzzer, 2, [11,10,9,8])
		#decr_siren([pwm_buzzer, pwm_led], 2, [12,10])
		music.play_song(pwm_buzzer, ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"])

# while True:
#
#	pwm_led.duty_cycle = cycle_high
#	print(high_exp, cycle_high)
#	time.sleep(2)
#
#	pwm_led.duty_cycle = 0
#	time.sleep(
#
#	pwm_led.duty_cycle = cycle_low
#	print(low_exp, cycle_low)
#	time.sleep(2)
#
#while True:
#    led.value = True
#    print("On")
#    time.sleep(2)
##    led.duty_cycle = 0
#    led.value = False
#    print("Off")
#    time.sleep(2)
