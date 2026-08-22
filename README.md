# Book_recommendation_system
In this repo, I will build a Book Recommendation System. From writing logic and training an ai model to creating a web page to actually demonstrate the output instead of running program on terminal. For building this project i am taking guidance of following YouTube video:  https://www.youtube.com/watch?v=1YoD0fg3_EM&amp;t=283s
<pre>
Types of recommendation system:
      __________________________________________________________________________________
      |                        |                        |                              |
Popularity based        Content based      Collaborative filtering based      Hybrid recommender system
</pre>

Dataset used : https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset?resource=download

**Popularity Based Recommender system**: From the dataset, we will calculate average rating per book and then identify books which have been rated by more than 250 users. By sorting them in descending order of average rating, the top 50 books will be recommended.


**Collaborative filtering based recommender system**: For this type of recommender system, the approach used in the video is very similar to approach i used for building a recommender system previously [ https://github.com/sarthak-geek/Book-Recommendation-Engine-using-NearsetNeighbour.git ].
The difference is, in the video cosine_similarity was used for calculating the distances between books from pivot table and then through filtering the nearest books to the target book were acquiered. However in the Book-Recommendation-Engine-using-NearsetNeighbour project, I used scikit learn modue's NearestNeighbour model which feed on pivot table, take book name as input and returns the the nearest books and distance to the tsrget.
For this project, I will use the approach from Book-Recommendation-Engine-using-NearsetNeighbour project instead of folowing the one used in video.
