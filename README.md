# Book_recommendation_system

In this repo, I will build a Book Recommendation System. From writing logic and training an AI model to creating a web page to actually demonstrate the output instead of running the program on the terminal. For building this project, I am taking guidance from the following YouTube video: https://www.youtube.com/watch?v=1YoD0fg3_EM&amp;t=283s

<pre>
Types of recommendation system:
      __________________________________________________________________________________
      |                        |                        |                              |
Popularity based        Content based      Collaborative filtering based      Hybrid recommender system
</pre>

In this project, I will cover Popularity-based and Collaborative-filtering-based recommender systems.

Dataset used: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download

**Popularity-Based Recommender System**: From the dataset, we will calculate the average rating per book and then identify books that have been rated by more than 250 users. By sorting them in descending order of average rating, the top 50 books will be recommended.

**Collaborative-filtering-based recommender system**: For this type of recommender system, the approach used in the video is very similar to the approach I used for building a recommender system previously [https://github.com/sarthak-geek/Book-Recommendation-Engine-using-NearsetNeighbour.git].

The difference is that, in the video, `cosine_similarity` was used for calculating the distances between books from the pivot table and then, through filtering, the nearest books to the target book were acquired. However, in the Book-Recommendation-Engine-using-NearsetNeighbour project, I used scikit-learn's `NearestNeighbour` model, which feeds on the pivot table, takes the book name as input, and returns the nearest books and their distances to the target.

For this project, I will use the approach from the Book-Recommendation-Engine-using-NearsetNeighbour project instead of following the one used in the video.

The notebooks include the dataset visualization part, and dataset modification and model training parts for each type of recommender system.

The modified dataset and trained model have already been uploaded in the respective folders, so there is no need to run the notebooks and download the dataset and model. However, you can still take reference from these notebooks to understand how the model was created and how the dataset was modified accordingly.

Python version used: **3.13.14**

To run the Flask application, install the required modules using `requirements.txt` and run:

```bash
python Flask/app.py
```
