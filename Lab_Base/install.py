import os

print("[1]:[update && upgrade]")
os.system('sudo apt update && apt upgrade -y')

# ? ENV
print("[1.1]:[CREATING virtualenv]")
os.system('virtualenv venv')
print("[1.2]:[CREATING virtualenv lab_env]")
os.system('source lab_env/bin/activate')



# ? PIP
print("[2]:[INSTALLING SOME PIP REQUIMENTS]")
print("[(the rest should be preinstalled with your standard Kali Linux)]")
print("[2.1]:[pip install -r requirements.txt]")
os.system('pip install request')

# ? APT
print("\n[3]:[INSTALLING SOME APT REQUIMENTS]")
print("[3.1]:[sudo apt install subfinder]")
os.system('sudo apt install subfinder')
print("[3.2]:[sudo apt install amass]")
os.system('sudo apt install amass')
# ? GO-LANG
print("\n[4]:[INSTALLING SOME GO-LANG REQUIMENTS]")
print("[!]:[( if subfinder failed to install: run )]")
print("[go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest]")
#os.system('go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest')



print("[5]:[update && upgrade]")
os.system('sudo apt update && apt upgrade -y')


print("[!]:[ALL DONE]\n[(if anything doesn't work from lack of import.. just install it.. )]")




# gnome-terminal <- cmd for opening new terminal

