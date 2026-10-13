import streamlit as st
import pandas as pd

st.set_page_config(
page_title="MaçAnaliz AI",
page_icon="⚽",
layout="wide"
)

st.title("⚽🏀 MaçAnaliz AI")
st.caption("Futbol ve basketbol analiz merkezi")

st.warning(
"Demo sürümüdür. Takımlar ve veriler örnektir; "
"gerçek maç tahmini değildir."
)

spor = st.sidebar.selectbox(
"Spor dalı", ["Futbol", "Basketbol"]
)

if spor == "Futbol":
    takimlar = pd.DataFrame({
        "Takım": ["Örnek FC", "Örnek SK"],
        "Son 5 maç": ["G-G-B-G-M", "M-B-G-M-B"],
        "Gol ortalaması": [1.8, 1.1]
    })
else:
    takimlar = pd.DataFrame({
        "Takım": ["Örnek Basket A", "Örnek Basket B"],
        "Son 5 maç": ["G-G-M-G-G", "M-G-M-B-G"],
        "Sayı ortalaması": [86.4, 80.2]
    })

st.subheader(f"{spor} takım karşılaştırması")
st.dataframe(
takimlar,
use_container_width=True,
hide_index=True
)

st.subheader("Takım form grafiği")
grafik = takimlar.set_index("Takım").iloc[:, 2]
st.bar_chart(grafik)

st.divider()
st.subheader("Bahis oranı karşılaştırıcısı")

if spor == "Futbol":
ev = st.number_input(
"Ev sahibi oranı", 1.01, 100.0, 1.85
)
beraberlik = st.number_input(
"Beraberlik oranı", 1.01, 100.0, 3.40
)
dep = st.number_input(
"Deplasman oranı", 1.01, 100.0, 4.20
)
oranlar = {
"Ev sahibi": ev,
"Beraberlik": beraberlik,
"Deplasman": dep
}
else:
ev = st.number_input(
"Ev sahibi kazanır oranı", 1.01, 100.0, 1.62
)
dep = st.number_input(
"Deplasman kazanır oranı", 1.01, 100.0, 2.35
)
oranlar = {
"Ev sahibi": ev,
"Deplasman": dep
}

ham = {ad: 1 / oran for ad, oran in oranlar.items()}
toplam = sum(ham.values())

sonuc = pd.DataFrame({
"Sonuç": list(oranlar.keys()),
"Oran": list(oranlar.values()),
"Ham olasılık (%)": [
round(ham[ad] * 100, 2) for ad in oranlar
],
"Marj ayarlı yaklaşık olasılık (%)": [
round(ham[ad] / toplam * 100, 2)
for ad in oranlar
]
})

st.dataframe(
sonuc,
use_container_width=True,
hide_index=True
)

st.write(
"Yaklaşık bahis piyasası marjı:",
f"%{(toplam - 1) * 100:.2f}"
)

st.caption(
"Oranlardan hesaplanan olasılık, model tahmini değildir. "
"Bahis sonucu garanti edilemez."
)

st.title("⚽ 🏀 MaçAnaliz AI")
st.write("Futbol ve basketbol maç analiz platformu")

spor = st.sidebar.selectbox(
    "Spor Dalı Seç",
    ["Futbol", "Basketbol"]
)

st.subheader(f"{spor} Analizi")

takim1 = st.text_input("1. Takım")
takim2 = st.text_input("2. Takım")

if spor == "Futbol":
    st.write("Futbol analizleri")
    sut = st.number_input("Takımın maç başına şut ortalaması", min_value=0.0, step=0.1)
    gol = st.number_input("Takımın maç başına gol ortalaması", min_value=0.0, step=0.1)

else:
    st.write("Basketbol analizleri")
    sayi = st.number_input("Takımın maç başına sayı ortalaması", min_value=0.0, step=1.0)
    uc_luk = st.number_input("Maç başına üçlük sayısı ortalaması", min_value=0.0, step=0.1)

if st.button("Analizi Göster"):
    if takim1 and takim2:
        st.success(f"{takim1} - {takim2} analizi hazırlandı.")
        if spor == "Futbol":
            st.write(f"Şut ortalaması: {sut}")
            st.write(f"Gol ortalaması: {gol}")
        else:
            st.write(f"Sayı ortalaması: {sayi}")
            st.write(f"Üçlük ortalaması: {uc_luk}")
    else:
        st.warning("Lütfen iki takımın adını gir.")
