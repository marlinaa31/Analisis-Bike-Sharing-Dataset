import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sidebar with user information
st.sidebar.header("User Information")
st.sidebar.text("**Nama:** Marlina")
st.sidebar.text("**Email:** marlinausman31@gmail.com")
st.sidebar.text("**ID Dicoding:** theonlylina")

# Main content
st.title("Bike Sharing Analysis Dashboard")

# Tambahkan gambar di bawah judul
from PIL import Image
image = Image.open('img/bike.jpg')  # Ganti dengan path gambar Anda
st.image(image, caption='Bike Sharing Analysis', use_column_width=True)

# Data Information
st.header("Dataset Information")
st.markdown("""
This dataset is sourced from Kaggle and contains information on bike-sharing rentals collected on an hourly and daily basis in the Capital Bikeshare system in Washington, D.C. over two years (2011-2012). The dataset includes various attributes such as weather conditions, seasons, holidays, and weekdays that can influence the demand for bike rentals.

- **Source:** [Kaggle: Bike Sharing Dataset](https://www.kaggle.com/datasets/gauravduttakiit/bike-sharing)
""")

# Data Wrangling
## Gathering Data
# Read dataset
df_hour = pd.read_csv("Bike-sharing-dataset/hour.csv", delimiter=",")
df_day = pd.read_csv("Bike-sharing-dataset/day.csv", delimiter=",")

# Combine DataFrames
bike_sharing = df_day.merge(df_hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))

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

# Display correlation matrix
st.subheader("Correlation Matrix")
numerical_columns = [
    "holiday_daily", "weekday_daily", "workingday_daily", "weathersit_daily",
    "temp_daily", "atemp_daily", "season_daily", "windspeed_daily", "cnt_daily"
]
correlation = bike_sharing[numerical_columns].corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, ax=ax)
ax.set_title("Correlation Matrix")
st.pyplot(fig)

## Exploratory Data Analysis (EDA)
st.header("Exploratory Data Analysis (EDA)")

### Question 1: Relationship between Season and Daily Bike Rentals
st.subheader("Question 1: Relationship between Season and Daily Bike Rentals")

seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean().reindex(index=[1, 2, 3, 4])
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=season_names, y=seasonal_data, palette="viridis", ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Sewa Harian')
ax.set_title('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
st.pyplot(fig)
st.markdown("- Dari grafik, terlihat bahwa peminjaman sepeda mencapai puncaknya selama musim gugur (Fall).")

### Question 2: Patterns in Daily Bike Rentals over Time
st.subheader("Question 2: Patterns in Daily Bike Rentals over Time")

# Monthly pattern
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None, marker='o', color='skyblue', linestyle='-', linewidth=2, ax=ax)
ax.set_title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Hourly pattern
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, ci=None, marker='o', color='salmon', linestyle='-', linewidth=2, ax=ax)
ax.set_title("Pola Jumlah Sewa Sepeda Harian Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sewa Sepeda Harian")
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
st.markdown("- Aktivitas penyewaan sepeda mencapai puncaknya pada bulan Juni dan September.")
st.markdown("- Analisis jam menunjukkan peningkatan signifikan pada jam 8 pagi dan 5 - 6 sore.")
st.markdown("- Kesimpulan: Ada pola musiman yang terlihat dengan peminjaman sepeda yang lebih tinggi di bulan-bulan tertentu dan peningkatan selama jam sibuk di pagi dan sore hari.")

### Question 3: Weather Impact on Daily Bike Rentals
st.subheader("Question 3: Weather Impact on Daily Bike Rentals")

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x="weathersit_daily", y="cnt_daily", data=bike_sharing, palette="viridis", ax=ax)
ax.set_title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian", fontsize=14)
ax.set_xlabel("Weathersit", fontsize=12)
ax.set_ylabel("Jumlah Sewa Sepeda Harian", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
st.markdown("- Peminjaman sepeda meningkat pada kondisi cuaca cerah, sedikit berawan, atau berawan sebagian.")
st.markdown("- Kesimpulan: Cuaca yang lebih cerah atau berawan memiliki hubungan positif dengan permintaan sepeda harian.")

### Question 4: Difference in Daily Bike Rentals between Working Days and Holidays
st.subheader("Question 4: Difference in Daily Bike Rentals between Working Days and Holidays")

colors = sns.color_palette("Set2")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=bike_sharing, palette=colors, width=0.5, ax=ax)
ax.set_title("Perbedaan Jumlah Sewa Sepeda Harian antara Hari Kerja dan Hari Libur", fontsize=14)
ax.set_xlabel("Hari Kerja (1) dan Hari Libur (0)", fontsize=12)
ax.set_ylabel("Jumlah Sewa Sepeda Harian", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
st.markdown("- Dari boxplot, terlihat bahwa jumlah sewa sepeda cenderung lebih tinggi pada hari kerja dibandingkan hari libur.")
st.markdown("- Kesimpulan: Terdapat perbedaan signifikan dalam jumlah sewa sepeda harian antara hari kerja dan libur, dengan jumlah sewa sepeda lebih tinggi pada hari kerja.")

## Conclusion
st.header("Conclusion")

st.subheader("Conclusion for Question 1: Relationship between Season and Daily Bike Rentals")
st.markdown("- Dari grafik, terlihat bahwa peminjaman sepeda mencapai puncaknya selama musim gugur (Fall).")

st.subheader("Conclusion for Question 2: Patterns in Daily Bike Rentals over Time")
st.markdown("- Grafik bulan menunjukkan bahwa aktivitas penyewaan sepeda mencapai puncaknya pada bulan Juni dan September.")
st.markdown("- Analisis jam menunjukkan peningkatan signifikan pada jam 8 pagi dan 5 - 6 sore.")
st.markdown("- Kesimpulan: Ada pola musiman yang terlihat dengan peminjaman sepeda yang lebih tinggi di bulan-bulan tertentu dan peningkatan selama jam sibuk di pagi dan sore hari.")

st.subheader("Conclusion for Question 3: Weather Impact on Daily Bike Rentals")
st.markdown("- Peminjaman sepeda meningkat pada kondisi cuaca cerah, sedikit berawan, atau berawan sebagian.")
st.markdown("- Kesimpulan: Cuaca yang lebih cerah atau berawan memiliki hubungan positif dengan permintaan sepeda harian.")

st.subheader("Conclusion for Question 4: Difference in Daily Bike Rentals between Working Days and Holidays")
st.markdown("- Dari boxplot, terlihat bahwa jumlah sewa sepeda cenderung lebih tinggi pada hari kerja dibandingkan hari libur.")
st.markdown("- Kesimpulan: Terdapat perbedaan signifikan dalam jumlah sewa sepeda harian antara hari kerja dan libur, dengan jumlah sewa sepeda lebih tinggi pada hari kerja.")
