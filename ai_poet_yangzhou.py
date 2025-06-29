import streamlit as st
import requests

st.set_page_config(page_title="AI诗人 · 扬州主题", page_icon=":scroll:", layout="centered")

st.title("AI诗人 · 扬州主题")
st.write("输入与扬州相关的词语或意境，让AI为你生成一首诗吧！（基于 Qwen2-7B-Chat，永久免费，无需API key）")

topic = st.text_input("请输入主题或关键词：", "扬州")
poem_type = st.selectbox("选择诗歌类型：", ["古诗", "现代诗"])

if st.button("生成诗歌"):
    with st.spinner("AI正在写诗，请稍候..."):
        # 构造提示词
        prompt = f"请用中文写一首与“{topic}”有关的{poem_type}，要求意境优美。"
        api_url = ("https://qwen1-5-7b-chat.hf.space/run/predict")
        try:
            response = requests.post(api_url, json={"data": [prompt]}, timeout=60)
            if response.status_code == 200:
                result = response.json()
                poem = result["data"][0]
                st.success(poem)
            else:
                st.error(f"API调用失败，状态码：{response.status_code}")
        except Exception as e:
            st.error(f"请求出错：{e}")

st.caption("由 Streamlit + Qwen2-7B-Chat 驱动 · 完全免费 · 祝你写诗愉快！")