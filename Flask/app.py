from flask import Flask, render_template, request
import pickle

with open('Datasets/popular_books.pkl', 'rb') as f:
    popular_books = pickle.load(f)
books = list(popular_books['Book-Title'].values)
authors = list(popular_books['Book-Author'].values)
image = list(popular_books['Image-URL-M'].values)
num_ratings = list(popular_books['num_ratings'].values)
avg_rating = list(popular_books['avg_rating'].values)

with open('Datasets/book_data.pkl', 'rb') as f:
    book_data = pickle.load(f)

book_pivot_table = book_data['book_pivot_table']
book_data = book_data['book_data']

with open('model/recommender_model.pkl', 'rb') as f:
    recommender = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('homepage.html', books=books,authors=authors,image=image,num_ratings=num_ratings,avg_rating=avg_rating)

@app.route('/recommend')
def recommend():
    book_name = request.args.get('book_name')
    return render_template('Recommend.html')

@app.route('/recommend_book', methods=['POST'])
def recommend_book():
    book_name = request.form.get('book_name')
    if book_name not in book_pivot_table.index:
        return render_template('BookNotFound.html')
    recommendations = []
    for i in recommender.kneighbors([book_pivot_table.loc[book_name]])[1][0][1:]:
        book = list(book_data[book_data['Book-Title'] == book_pivot_table.index[i]].drop_duplicates('Book-Title')[['Book-Title','Book-Author', 'Image-URL-M']].values[0])
        recommendations.extend([book])
    
    return render_template('Recommend.html', recommendations=recommendations)

if(__name__ == '__main__'):
    app.run()