# dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# Import the data
df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv", delimiter=",")
df_day = pd.read_csv("Bike-sharing-dataset/day.csv", delimiter=",")

# Combine DataFrames
bike_sharing = df_day.merge(df_hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

# Sidebar with user information
st.sidebar.header("User Information")
st.sidebar.text(f"**Nama:** Marlina")
st.sidebar.text(f"**Email:** marlinausman31@gmail.com")
st.sidebar.text(f"**ID Dicoding:** theonlylina")

# Main content
st.title("Bike Sharing Analysis Dashboard")

# Data Overview
st.header("Data Overview")

# Display the first few rows of the data
st.subheader("Preview of the Bike Sharing Dataset")
st.write(bike_sharing.head())

# Display summary statistics
st.subheader("Summary Statistics of the Bike Sharing Dataset")
st.write(bike_sharing.describe())

# Display information about the dataset
st.subheader("Information about the Bike Sharing Dataset")
st.markdown("Dataset ini berisi data jumlah sepeda yang disewa secara per jam dan per hari antara tahun 2011 dan 2012 dalam sistem sewa sepeda berbagi di ibu kota, dengan informasi cuaca dan musiman yang sesuai.")

st.subheader("Shape of the merged DataFrame:")
st.write(bike_sharing.shape)

st.subheader("Sample of the Merged DataFrame:")
st.write(bike_sharing.head())

### Plot 1: Relationship between Season and Daily Bike Rentals
st.subheader("Plot 1: Relationship between Season and Daily Bike Rentals")
# Your code for Plot 1
seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean().reindex(index=[1, 2, 3, 4])
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
plt.figure(figsize=(10, 6))
sns.barplot(x=season_names, y=seasonal_data, palette="viridis")
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Sewa Harian')
plt.title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
st.pyplot()

### Plot 2: Patterns in Daily Bike Rentals over Time (Month and Hour)
st.subheader("Plot 2: Patterns in Daily Bike Rentals over Time (Month and Hour)")
# Your code for Plot 2
plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None, marker='o', color='skyblue', linestyle='-', linewidth=2)
plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

plt.figure(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, ci=None, marker='o', color='salmon', linestyle='-', linewidth=2)
plt.title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Jam")
plt.xlabel("Jam")
plt.ylabel("Jumlah Sewa Sepeda Harian")
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

### Plot 3: Weather Impact on Daily Bike Rentals
st.subheader("Plot 3: Weather Impact on Daily Bike Rentals")
# Your code for Plot 3
plt.figure(figsize=(10, 6))
sns.boxplot(x="weathersit_daily", y="cnt_daily", data=bike_sharing, palette="viridis")
plt.title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian", fontsize=14)
plt.xlabel("Weathersit", fontsize=12)
plt.ylabel("Jumlah Sewa Sepeda Harian", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

### Plot 4: Difference in Daily Bike Rentals between Working Days and Holidays
st.subheader("Plot 4: Difference in Daily Bike Rentals between Working Days and Holidays")
# Your code for Plot 4
colors = sns.color_palette("Set2")
plt.figure(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing, palette=colors, width=0.5)
plt.title("Perbedaan Jumlah Sewa Sepeda Harian antara Hari Kerja dan Hari Libur", fontsize=14)
plt.xlabel("Hari Kerja (1) dan Hari Libur (0)", fontsize=12)
plt.ylabel("Jumlah Sewa Sepeda Harian", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot()

# Conclusion
st.header("Conclusion")

### Conclusion for Question 1
st.subheader("Conclusion for Question 1: Relationship between Season and Daily Bike Rentals")
st.markdown("- Dari grafik, terlihat bahwa peminjaman sepeda mencapai puncaknya selama musim gugur (Fall).")

### Conclusion for Question 2
st.subheader("Conclusion for Question 2: Patterns in Daily Bike Rentals over Time")
st.markdown("- Grafik bulan menunjukkan bahwa aktivitas penyewaan sepeda mencapai puncaknya pada bulan Juni dan September.")
st.markdown("- Analisis jam menunjukkan peningkatan signifikan pada jam 8 pagi dan 5 - 6 sore.")
st.markdown("- Kesimpulan: Ada pola musiman yang terlihat dengan peminjaman sepeda yang lebih tinggi di bulan-bulan tertentu dan peningkatan selama jam sibuk di pagi dan sore hari.")

### Conclusion for Question 3
st.subheader("Conclusion for Question 3: Weather Impact on Daily Bike Rentals")
st.markdown("- Peminjaman sepeda meningkat pada kondisi cuaca cerah, sedikit berawan, atau berawan sebagian.")
st.markdown("- Kesimpulan: Cuaca yang lebih cerah atau berawan memiliki hubungan positif dengan permintaan sepeda harian.")

### Conclusion for Question 4
st.subheader("Conclusion for Question 4: Difference in Daily Bike Rentals between Working Days and Holidays")
st.markdown("- Dari boxplot, terlihat bahwa jumlah sewa sepeda cenderung lebih tinggi pada hari kerja dibandingkan hari libur.")
st.markdown("- Kesimpulan: Terdapat perbedaan signifikan dalam jumlah sewa sepeda harian antara hari kerja dan libur, dengan jumlah sewa sepeda lebih tinggi pada hari kerja.")


