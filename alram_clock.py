from datetime import datetime
# from playsound import playsound

Alram_time = input('Enter the time for alram:HH:MM:SS\n')
alram_hour = Alram_time[0:2]
alram_min = Alram_time[3:5]
alram_sec = Alram_time[6:8]
alram_period = Alram_time[9:11]

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime("%I")
    current_minute = current_time.strftime("%M")
    current_seconds = current_time.strftime("%S")
    current_period = current_time.strftime("%p")
    if current_hour == alram_hour and current_minute == alram_min and current_seconds == alram_sec and current_period == alram_period:
        print('Wake Up!!!')
        # playsound('audio.mp3')
        break


