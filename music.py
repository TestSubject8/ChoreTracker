import tones
import time

def play_song(pwm_out, notes, tempo=150):
	for n in notes:
		volume(pwm_out, 0.5)
		if n == 'P':
			volume(pwm_out, 0)
		else:
			freq = tones.tones[n]
			print(n, freq)
			pwm_out.frequency = freq
		time.sleep(60.0 / tempo)
	volume(pwm_out,0)

def volume(pwm_out, fraction):
	volume = fraction * (2**14 - 1)
	print(volume)
	pwm_out.duty_cycle = int(volume)

