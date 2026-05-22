import streamlit as st

st.title("簡單計算機")

num1 = st.number_input("第一個數字", value=0.0)
num2 = st.number_input("第二個數字", value=0.0)

operation = st.selectbox(
    "選擇運算",
    ["加法", "減法", "乘法", "除法"]
)

if st.button("開始計算"):

    if operation == "加法":
        result = num1 + num2

    elif operation == "減法":
        result = num1 - num2

    elif operation == "乘法":
        result = num1 * num2

    else:
        if num2 == 0:
            st.error("不能除以 0")
            st.stop()

        result = num1 / num2

    st.success(f"結果：{result}")
