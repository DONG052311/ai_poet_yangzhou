import streamlit as st
import openai

st.set_page_config(page_title="AI诗人 · 扬州主题", page_icon=":scroll:", layout="centered")

st.title("AI诗人 · 扬州主题（OpenAI GPT-3.5/4）")
st.write(
    "输入与扬州相关的词语或意境，让AI为你生成一首诗吧！"
    "\n（本地运行，无需魔法上网，需有效OpenAI API密钥）"
)

# 让用户在页面上输入自己的 OpenAI API 密钥
api_key = st.text_input("请输入你的 OpenAI API 密钥（sk-...）", type="password")

topic = st.text_input("请输入主题或关键词：", "扬州")
poem_type = st.selectbox("选择诗歌类型：", ["古诗", "现代诗"])
model = st.selectbox("选择模型：", ["gpt-3.5-turbo", "gpt-4o", "gpt-4"])

if st.button("生成诗歌"):
    if not api_key:
        st.warning("请先输入你的 OpenAI API 密钥")
    else:
        prompt = f"请用中文写一首与“{topic}”有关的{poem_type}，要求意境优美。"
        with st.spinner("AI正在写诗，请稍候..."):
            try:
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "你是一位中国诗人。"},
                        {"role": "user", "content": prompt}
                    ]
                )
                poem = response.choices[0].message.content.strip()
                st.success(poem)
            except Exception as e:
                st.error(f"API调用失败：{e}")

st.caption("由 Streamlit + OpenAI 驱动 · 仅供学习体验 · 请保护好你的API密钥！")