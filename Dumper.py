import subprocess


names = subprocess.check_output("netsh wlan show profile ").decode('UTF-8')

print(""" ▄     ▄ ▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄    ▄▄▄▄▄▄  ▄▄   ▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█ █ ▄ █ █   █       █   █  █      ██  █ █  █  █▄█  █       █       █   ▄  █  
█ ██ ██ █   █    ▄▄▄█   █  █  ▄    █  █ █  █       █    ▄  █    ▄▄▄█  █ █ █  
█       █   █   █▄▄▄█   █  █ █ █   █  █▄█  █       █   █▄█ █   █▄▄▄█   █▄▄█▄ 
█       █   █    ▄▄▄█   █  █ █▄█   █       █       █    ▄▄▄█    ▄▄▄█    ▄▄  █
█   ▄   █   █   █   █   █  █       █       █ ██▄██ █   █   █   █▄▄▄█   █  █ █
█▄▄█ █▄▄█▄▄▄█▄▄▄█   █▄▄▄█  █▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄█   █▄█▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█  █▄█
""")

print("Wifi names and passwords: ")

for x in names.splitlines():
    if x.__contains__("All"):
        name = x.strip("All User Profile     :")
        passwords = subprocess.check_output(f"netsh wlan show profile {name.strip()} key=clear").decode("UTF-8")
        for y in passwords.splitlines():
            if y.__contains__("Key Content"):

                password = y.strip("Key Content            : ")

                print(f"Password for {name} is " + password)
                with open("wifiInfo","a") as f:
                    f.write(f"\nPassword for {name} is " + password)

