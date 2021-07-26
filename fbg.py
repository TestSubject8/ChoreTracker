import subprocess, signal

proc_id = None

def call_display(prog_name):
    global proc_id
    # proc_id = subprocess.call(['sh', 'flash_image', prog_name])
    proc_id = subprocess.Popen('sh', 'flash_image', prog_name)


def stop_display():
    proc_id.send_signal(signal.SIG_INT)