import streamlit as st
import requests

st.set_page_config(page_title="AI诗人 · 扬州主题", page_icon=":scroll:", layout="centered")

st.title("AI诗人 · 扬州主题（硅基流动API）")
st.write(
    "输入与扬州相关的词语或意境，让AI为你生成一首诗吧！"
    "\n（本页面调用硅基流动API，无需魔法上网，需有效API密钥）"
)

# 你的硅基流动API密钥（一定要妥善保管！不要泄露）
API_KEY = "sk-hrsofgrwgmubckiaayfptkrrmyymptbczrabhiormhcfhdvj"  # 请替换为你的密钥！
topic = st.text_input("请输入主题或关键词：", "扬州")
poem_type = st.selectbox("选择诗歌类型：", ["古诗", "现代诗"])

if st.button("生成诗歌"):
    with st.spinner("AI正在写诗，请稍候..."):
        prompt = f"请用中文写一首与“{topic}”有关的{poem_type}，要求意境优美。"
        api_url = "https://api.siliconflow.cn/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",  # 请根据官方文档实际模型名填写
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = requests.post(api_url, headers=headers, json=data, timeout=60)
            if response.status_code == 200:
                result = response.json()
                poem = result["choices"][0]["message"]["content"]
                st.success(poem)
            else:
                st.error(f"API调用失败，状态码：{response.status_code}\n{response.text}")
        except Exception as e:
            st.error(f"请求出错：{e}")

st.caption("由 Streamlit + 硅基流动API 驱动 · 仅供学习体验 · 保护好你的API密钥！")