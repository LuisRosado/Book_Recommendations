from flask import Flask, render_template, request, jsonify, redirect, url_for
from recommendation import get_recommendations
import uuid

app = Flask(__name__)

# Almacén temporal para las recomendaciones
recommendations_store = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    book_title = request.form['book_title']
    recommended_books = get_recommendations(book_title)
    
    if recommended_books:
        # Generar un ID único para esta recomendación
        recommendation_id = str(uuid.uuid4())
        recommendations_store[recommendation_id] = recommended_books
        return jsonify({'id': recommendation_id, 'books': recommended_books})
    else:
        return jsonify({'error': 'No se encontraron recomendaciones para este libro.'}), 404

@app.route('/recommendations', methods=['GET'])
def show_recommendations():
    recommendation_id = request.args.get('id')
    if recommendation_id in recommendations_store:
        recommended_books = recommendations_store[recommendation_id]
        return render_template('recommendations.html', books=recommended_books)
    else:
        return redirect(url_for('index'))

@app.route('/get_recommendations', methods=['GET'])
def get_recommendations_json():
    recommendation_id = request.args.get('id')
    if recommendation_id in recommendations_store:
        return jsonify(recommendations_store[recommendation_id])
    else:
        return jsonify({'error': 'No se encontraron recomendaciones para este ID.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
