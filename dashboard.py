import pandas as pd
import streamlit as st
import seaborn as sns
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
merged_data = pd.read_csv("merged_data.csv")

# Title
st.title('Dashboard Analisis Data E-commerce')

# Subtitle
st.subheader('Perbandingan Kinerja Seller dari Berbagai Kota (10 kota teratas)')

# Ambil 10 kota teratas berdasarkan jumlah seller
top_cities = merged_data['seller_city'].value_counts().head(10).index

# Filter data hanya untuk kota-kota teratas
filtered_data = merged_data[merged_data['seller_city'].isin(top_cities)]

# Visualisasi perbandingan jumlah seller dari 10 kota teratas
st.bar_chart(filtered_data['seller_city'].value_counts())

# Copyright
st.caption("© 2024 Bayu Puspito Aji. All rights reserved.")

# Subtitle
st.subheader('Perbandingan Kinerja Seller dari Berbagai Negara Bagian')

# Visualisasi perbandingan jumlah seller dari berbagai negara bagian
st.bar_chart(merged_data['seller_state'].value_counts())

# Copyright
st.caption("© 2024 Bayu Puspito Aji. All rights reserved.")

# Subtitle
st.subheader('Kelompok Seller yang Menonjol dalam Hal Jumlah Penjualan')

# Visualisasi top 10 seller berdasarkan jumlah penjualan
st.bar_chart(merged_data['seller_id'].value_counts().head(10))

# Copyright
st.caption("© 2024 Bayu Puspito Aji. All rights reserved.")
