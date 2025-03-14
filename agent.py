import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载秘钥
load_dotenv()
client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"  # 智谱专属入口
)

def chat(prompt):
    response = client.chat.completions.create(
        model="glm-4",  # 最新国产大模型
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        question = input("你：")
        print("AI：", chat(question))