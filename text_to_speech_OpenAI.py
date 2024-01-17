import requests

# 输入你的文件路径和文件名
text_file_path = input("请输入你的文件路径和文件名: ")

# 输入你想要保存的.mp3文件的路径和文件名
mp3_file_path = input("请输入你想要保存的.mp3文件的路径和文件名: ")

# 读取文本文件内容
with open(text_file_path, 'r', encoding="utf-8") as file:
    input_text = file.read()

data = {
    "model": "tts-1-hd",
    "input": input_text,
    "voice": "fable"
}

headers = {
    "Authorization": "Bearer Your_API_Token",
    "Content-Type": "application/json"
}

response = requests.post('https://api.openai.com/v1/audio/speech', headers=headers, json=data)

# 保存你的.mp3文件到你指定的路径和文件名
with open(mp3_file_path, 'wb') as f:
    f.write(response.content)