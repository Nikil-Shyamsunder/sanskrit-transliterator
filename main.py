import streamlit as st
import pandas as pd
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
st.set_page_config(layout="wide", page_icon="🕉️", page_title="Sanskrit Transliterator")
st.title("Harvard–Kyōto → Devanāgarī + IAST")

# two-column layout
col1, col2 = st.columns([1, 2])

with col1:
    hk = st.text_area(
        "Enter text in Harvard–Kyōto",
        height=200,
        placeholder="e.g. karma, dharma, satya"
    )

# transliterate when there's input
if hk.strip():
    dev = transliterate(hk, sanscript.HK, sanscript.DEVANAGARI)
    iast = transliterate(hk, sanscript.HK, sanscript.IAST)
else:
    dev = ""
    iast = ""

with col2:
    st.text_area("Devanāgarī (Unicode)", value=dev, height=200)
    st.text_area("IAST",            value=iast, height=200)

# expandable conversion table
with st.expander("Show conversion table"):
    data = [
        ("a",  "a",     "अ"),
        ("A",  "ā",     "आ"),
        ("i",  "i",     "इ"),
        ("I",  "ī",     "ई"),
        ("u",  "u",     "उ"),
        ("U",  "ū",     "ऊ"),
        ("R",  "ṛ",     "ऋ"),
        ("e",  "e",     "ए"),
        ("ai", "ai",    "ऐ"),
        ("o",  "o",     "ओ"),
        ("au", "au",    "औ"),
        ("k",  "k",     "क"),
        ("kh", "kh",    "ख"),
        ("g",  "g",     "ग"),
        ("gh", "gh",    "घ"),
        ("N",  "ṇ",     "ङ"),
        ("etc.",  "etc.",     "etc."),
        # … add more as needed …
    ]
    df = pd.DataFrame(data, columns=["HK", "IAST", "Devanāgarī"])
    st.dataframe(df, use_container_width=True)
