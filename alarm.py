from gtts import gTTS
from pydub import AudioSegment

# Tạo giọng đọc
tts = gTTS("Đến giờ uống thuốc", lang="vi")
tts.save("alarm.mp3")

# Lặp lại để đủ 60 giây
sound = AudioSegment.from_mp3("alarm.mp3")
looped = sound
while len(looped) < 57500:  # 60 giây
    looped += sound

final = looped[:57500]  # cắt đúng 1 phút
final.export("alarm.wav", format="wav", parameters=["-ar", "44100"])
