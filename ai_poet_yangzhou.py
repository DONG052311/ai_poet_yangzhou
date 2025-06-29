import streamlit as st
import openai

# 设定你的OpenAI API密钥
openai.api_key = "你的API密钥"  # 请替换为你的真实API Key
st.title("AI诗人 · 扬州主题")
st.write("输入与扬州有关的词语或意境，让AI为你生成一首诗吧！")

# 输入框
theme = st.text_input("请输入主题或关键词：", "瘦西湖")

# 选择诗歌类型
poem_type = st.selectbox("选择诗歌类型：", ["古诗", "现代诗"])

if st.button("生成诗歌"):
    with st.spinner("AI正在创作中，请稍等..."):
        prompt = f"请以“{theme}”为主题，创作一首{poem_type}，要求诗意浓郁，突出扬州特色。"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 你可以用"gpt-4"如果有权限
                messages=[
                    {"role": "system", "content": "你是一位中国古代/现代诗人，非常擅长写诗。"},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.8,
                max_tokens=200,
                n=1
            )
            poem = response.choices[0].message['content']
            st.success("AI诗人创作完成：")
            st.write(poem)
        except Exception as e:
            st.error(f"出错了：{e}")

st.markdown("---")
st.markdown("**提示**: 你可以尝试如'扬州烟花三月'、'瘦西湖春色'、'扬州盐商'等主题。")