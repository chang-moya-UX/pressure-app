import streamlit as st

# ページの設定
st.set_page_config(page_title="圧力単位変換 (MPa / psi / kg/cm²)", page_icon="⚙️", layout="centered")

st.title("圧力単位変換 ")
st.write("MPaとPSIとkg/cm²を変換する")

# 1 Pa を基準とした換算辞書 (1 unit = 何 Pa か)
pa_coefficients = {
    "MPa (メガパスカル)": 1000000.0,
    "psi (ポンド/平方インチ)": 6894.757,
    "kg/cm² (キログラム毎平方センチメートル)": 98066.5
}

# --- メイン機能：単位変換 ---
st.markdown("### 🔄 単位を選択して変換")

col1, col2, col3 = st.columns(3)

with col1:
    # 初期値を None にして、未入力時は空っぽにする
    input_value = st.number_input("圧力計の数値を入力", value=None, placeholder="数値を入力...", format="%.4f")

with col2:
    from_unit = st.selectbox("変換前", list(pa_coefficients.keys()), index=0)

with col3:
    to_unit = st.selectbox("変換後", list(pa_coefficients.keys()), index=1)

# --- 計算と表示（入力されたときだけ実行する） ---
if input_value is not None:
    # 計算ロジック（一度Paに直してから目的の単位へ）
    value_in_pa = input_value * pa_coefficients[from_unit]
    result = value_in_pa / pa_coefficients[to_unit]

    # 変換元の単位名と変換先の単位名（略称）を取得
    from_name = from_unit.split(" ")[0]
    to_name = to_unit.split(" ")[0]

    # 変換結果の表示
    st.info(f"💡 **変換結果:**\n### {input_value} {from_name} = **{result:,.4f}** {to_name}")

    # --- べんり機能：3大単位の一括換算表 ---
    st.markdown("---")
    st.markdown("### 📋 この数値の3大単位一覧")
    st.write(f"入力された **{input_value} {from_name}** をすべての単位に直した一覧です：")

    # 各単位への変換結果をまとめて計算
    all_results = {}
    for unit, coeff in pa_coefficients.items():
        converted = value_in_pa / coeff
        short_name = unit.split(" ")[0]
        all_results[short_name] = f"{converted:,.4f}"

    # 綺麗なテーブルで表示
    st.table(all_results)
else:
    # 何も入力されていないときは、案内を表示しておく
    st.warning("⚠️ 上のボックスに圧力計の数値を入力してください。")