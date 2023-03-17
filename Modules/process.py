import subprocess



# Start the first script and wait for it to finish
print('*/*/*/*/*/*/*/*/*/* Starting Sudo User Creation Process *\*\*\*\*\*\*\*\*\*\*')
subprocess.run(['python', 'create_user.py'], check=True)
print('User Creation Complete')
print('-------------------------------')

# Start 2nd
print('Starting Update Process')
subprocess.run(['python', 'update.py'], check=True)
print('Update Process Complete')
print('------------------------')

# Start 3rd
print('installing Wget')
subprocess.run(['python', 'wget_inst.py'], check=True)
print('wget Installation Complete')
print('--------------------------')

# Start 4th script
print('installing Nano')
subprocess.run(['python', 'nano_inst.py'], check=True)
print('installing Nano Complete')
print('--------------------------')

# Start 5th script
print('installing OpenSSH')
subprocess.run(['python', 'openssh_inst.py'], check=True)
print('installing OpenSSH-- Complete')
print('-----------------------------')

# Start the 6th script
print('Starting OPEN SSH CONFIG')
subprocess.run(['python', 'openssh_conf.py'], check=True)
print(' OpenSSH Config --- Complete')
print('-----------------------------')


# Start the 7th script
print('Starting ASTROMIENR ISNTALL')
subprocess.run(['python', 'miner/astrominer.py'], check=True)
print(' ASTROMINER ISNTALATION --- Complete')
print('-----------------------------')

# Start the 8th script
print('Connecting To Pool with 1 Address')
subprocess.run(['python', 'Pool/1pool.py'], check=True)
print(' CONNECTED')
print('-----------------------------')

print("WHOLE PROCESS COMPLETE")
