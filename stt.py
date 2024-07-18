#py310
import wenet

model = wenet.load_model('chinese')
result = model.transcribe(
    '/home/xinying/Speaker2/Qwen-AIpendant/seperated/out2.wav'
    )
print(result['text'])