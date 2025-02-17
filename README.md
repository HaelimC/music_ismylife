## 🚀 My Role in the Project  

I contributed to this project as a **Data Engineer**, primarily focusing on **API integration, data extraction, and building automated data pipelines** to ensure seamless data processing and storage.  

### **Key Contributions:**  
- **Integrated External APIs** → Fetched and processed **music recommendation & playlist data** using **Spotify API**  
- **Developed Data Pipelines** → Built automated **ETL workflows** to collect, transform, and load data into **PostgreSQL**  
- **Optimized Database Schema** → Designed and managed **PostgreSQL tables** for structured storage and efficient queries  
- **Automated Data Processing** → Utilized **Apache Airflow** to schedule and manage daily data updates  
- **Ensured API-Django Compatibility** → Structured API responses to align with **Django backend requirements**  
- **Collaborated in System Architecture** → Worked closely with the team to design an efficient **data flow & system architecture**  

This role allowed me to **bridge the gap between API data sources and backend functionality**, ensuring **smooth integration and automated processing** within the system. 🚀

---

# Rooftop Playlist 🎧

## I. Project Background and Goals

### **🔍 Limitations of Existing Music Recommendation Features**

- Current music streaming platforms provide recommendations based only on their internal accumulated data.
- Finding recommended songs for a specific track across multiple platforms is difficult.

### **👤 Integrated Recommendation Utilizing Various Platforms**

- Combines the strengths of YouTube and Spotify to provide users with a **`comprehensive recommendation service beyond a single platform`**.
- Delivers an **`optimized recommendation experience`** by reflecting platform-specific features such as cover songs and professional curation.

---

## II. Technologies Used & Project Structure

| TASK | Technology | Notes |
| --- | --- | --- |
| Data Collection | Python, SQL | **`Spotify API`**, **`YouTube API`** usage |
| Data Preprocessing | Python, SQL | Transforming API data to match database structure |
| Data Warehouse (DB) | On-premise | **`PostgreSQL`** - Data storage through APIs |
| Visualization | Django | **`Web Page`** - Display search and recommendation results |
| Team Management | Notion, Discord, GitHub, VSCode | **`Notion`**: Project meetings and documentation
**`Discord`**: Real-time communication
**`GitHub`**: Version control
**`VSCode`**: Live code sharing and collaboration |

### ⚙ System Architecture

![System Architecture](https://github.com/HaelimC/music_ismylife/blob/main/img/architecture.jpg)

---

## III. Project Details

### **🔶 Entity-Relationship Diagram (ERD)**

![ERD](https://github.com/HaelimC/music_ismylife/blob/main/img/erd.png)

### **⚒ Development Process**

#### **Step 1: Data Collection and Preprocessing**

| Data Name | Source | Update Frequency | Description |
| --- | --- | --- | --- |
| spotify_playlist | Spotify API | Triggered via Django | Playlists containing the searched song |
| spotify_recommend | Spotify API | Triggered via Django | Songs recommended based on the searched song |
| search_youtube_playlist | YouTube API | Triggered via Django | YouTube playlists containing the searched song (filtered by 'music' keyword) |
| search_youtube_video | YouTube API | Triggered via Django | Videos recommended based on the searched song (filtered by 'music' keyword) |
| spotify_today_tracks | Spotify API | Daily at midnight | Top 10 tracks from Global Top 50 daily |
| spotify_today_playlists | Spotify API | Daily at midnight | Top 10 playlists containing the keyword 'top' |
| daily_youtube_video | YouTube API | Daily at midnight | Top 10 global trending music videos |

#### **Step 2: Data Storage**

📋 **Automated Data Ingestion Using Airflow DAGs**

- Data is stored in **PostgreSQL**, with DAGs handling the extraction, transformation, and loading process.
- Data is preprocessed into a **structured database schema**, categorizing recommendations into **daily trends** and **search-based results**.

#### **Step 3: Data Visualization and Web UI (Django)**

📊 **Features of Web UI**
- **Daily recommendations**: Displays trending songs and playlists from YouTube and Spotify.
- **Search-based recommendations**: Shows recommended tracks and playlists based on user queries.
- **Playlist and song playback support**: Allows users to play songs directly within the web interface.
- **Platform-based filtering**: Users can choose recommendations from either YouTube or Spotify.

---

## IV. Expected Impact

### 👍🏽 Benefits

1. **Time-saving through integrated search**
    - Previously, users had to search separately on YouTube and Spotify to find relevant music.
    - This project enables **`one-click access to comprehensive recommendations`** across both platforms.

2. **Diverse recommendation sources**
    - **YouTube**: Rich in user-generated content (e.g., covers, live performances).
    - **Spotify**: Provides expertly curated playlists.
    - **`Combining both platforms`** allows for **`a more extensive selection of recommendations`**.

3. **Immediate playback**
    - Recommended songs can be **`played directly on the web UI`**, eliminating the need to switch platforms.

4. **Playlist integration**
    - Users can **`add recommended playlists to their Spotify or YouTube accounts directly from the web UI`**.

### ☝🏽 Limitations & Future Improvements

1. **Limited personalization**
    - Currently, recommendations are based solely on search queries rather than personal listening history.

2. **Enhancing personalized recommendations**
    - Future updates could integrate user listening history, likes, and saved playlists for **`personalized recommendations`**.

3. **Expanding supported platforms**
    - Additional music streaming services could be integrated to broaden recommendation sources.

---
