# 🎬 MovieMate — Movie Recommendation System
project link: https://moviemate-movierecommendersystem-ejzfrntdcgwoq5uwjsfrbn.streamlit.app/

**Discover your next favorite movie with MovieMate!**

MovieMate is a Python-based movie recommendation web application built with Streamlit. It recommends movies similar to a user's selected movie using a precomputed similarity matrix, helping users discover films they may enjoy.

## ✨ Features

- 🎥 **Movie Recommendations:** Discover five movies similar to your selected movie.
- 🔎 **Movie Selection:** Choose a movie from the available movie database.
- 🖼️ **Movie Posters:** View movie posters alongside recommendations.
- 🎨 **Clean UI:** Minimal, modern light-themed interface.
- ⚡ **Interactive Experience:** Get recommendations with a simple button click.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Movie data handling |
| Pickle | Loading saved movie data and similarity matrix |
| Scikit-learn | Machine learning utilities, if used in model preparation |
| TMDB API | Movie poster retrieval, if configured |

## 🧠 How It Works

1. The application loads the prepared movie dataset.
2. The user selects a movie from the dropdown menu.
3. The system retrieves the selected movie's similarity scores.
4. It ranks movies by similarity and selects the top five recommendations, excluding the selected movie itself.
5. The recommended movie titles and posters are displayed in the application.

## 📸 Application Preview



![MovieMate Home Page](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3aaa1107-10cf-4b15-a839-bdbab689de32" />
)

![Movie Recommendations](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/131cddeb-0dcb-4e7f-9871-d30d2dc51de0" />
)

## 📂 Project Structure

```text
Recommender-System/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md│
└── venv/
```


## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <[YOUR_GITHUB_REPOSITORY_UR](https://github.com/RasikaSondkar/MovieMate-Movie_Recommender_System)L>
cd Recommender-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```



## 📦 Required Files

Ensure that the repository includes the required prepared data files:

- `movies.pkl` — processed movie dataset.
- `similarity.pkl` — precomputed movie similarity matrix.

If these files are not included in the repository, generate them using your data-preparation notebook or provide instructions for obtaining them.

## 🚀 Future Improvements

- Display movie genres, ratings, and release years.
- Add movie search and filtering.
- Improve recommendation quality with additional movie metadata.
- Add a watchlist and favorites feature.
- Enhance the interface for mobile devices.
- Add multilingual support.

## 🎯 Project Objective

The objective of MovieMate is to demonstrate how Python, machine learning concepts, and an interactive web interface can work together to build a personalized movie discovery experience.

## 👩‍💻 Author

**Rasika Sondkar**

GitHub: https://github.com/RasikaSondkar



