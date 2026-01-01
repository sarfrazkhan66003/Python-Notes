import os
print('type stop to end')
while True:
      a=input("enter your words here")
      if a=='stop':
            break

      command=f"  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{a}');\""
      os.system(command)
      break