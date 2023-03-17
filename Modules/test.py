import subprocess


# Start the fifth script


print('Starting ASTROMIENR ISNTALL')
subprocess.run(['python', 'miner/astrominer.py'], check=True)
print(' ASTROMINER ISNTALATION --- Complete')
print('-----------------------------')


# Start the fifth script
print('Connecting To Pool with 1 Address')
subprocess.run(['python', 'Pool/1pool.py'], check=True)
print(' CONNECTED')
print('-----------------------------')

print("WHOLE PROCESS COMPLETE")
