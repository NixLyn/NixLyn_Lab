import os

print("[1]:[update && upgrade]")
os.system('sudo apt update && apt upgrade -y')

# ? PIP
print("[2]:[INSTALLING SOME PIP REQUIMENTS]")
print("[(the rest should be preinstalled with your standard Kali Linux)]")
print("[2.1]:[pip install request]")
os.system('pip install request')
print("[2.2]:[pip install torrequest]")
os.system('pip install torrequest')
# ? APT
print("\n[3]:[INSTALLING SOME APT REQUIMENTS]")
print("[3.1]:[sudo apt install gobuster]")
os.system('sudo apt install gobuster')
print("[3.2]:[sudo apt install amass]")
os.system('sudo apt install amass')
# ? GO-LANG
print("\n[4]:[INSTALLING SOME GO-LANG REQUIMENTS]")
print("[!]:[check the docs for your system configuration]\n ~ ~ ~ ~ [4.1]:[go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest]")
# os.system('go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest')



print("[5]:[update && upgrade]")
os.system('sudo apt update && apt upgrade -y')


print("[!]:[ALL DONE]\n[(if anything doesn't work from lack of import.. just install it.. )]")




# gnome-terminal <- cmd for opening new terminal

