import streamlit as st
import openai

# 初始化 OpenAI 客户端（推荐用 Streamlit Secret 管理 API KEY）
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI诗人 · 扬州主题")
st.write("输入与扬州有关的词语或意境，让AI为你生成一首诗吧！")

# 输入主题
theme = st.text_input("请输入主题或关键词：", "扬州")

# 选择诗歌类型
poem_type = st.selectbox("选择诗歌类型：", ["古诗", "现代诗"])

if st.button("生成诗歌"):
    with st.spinner("AI正在创作中，请稍候..."):
        # 构建 prompt
        prompt = f"请以“{theme}”为主题，创作一首{poem_type}，要求诗意优美，突出扬州特色。"
        try:
            # 调用 OpenAI GPT-3.5/4 接口
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # 你也可以用gpt-4
                messages=[
                    {"role": "system", "content": "你是一位中国诗人。"},
                    {"role": "user", "content": prompt}
                ]
            )
            poem = response.choices[0].message.content
            st.success("AI诗人创作完成：")
            st.write(poem)
        except Exception as e:
            st.error(f"出错了：{e}")

st.markdown("---")
st.markdown("由 Streamlit + OpenAI 驱动 · 祝你写诗愉快！")