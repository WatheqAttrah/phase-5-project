import React, { useState } from 'react';

function AddReview({ carId, onAddReview, user, onAppendReview }) {
  const [showForm, setShowForm] = useState(false);
  const [reviewText, setReviewText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const closeForm = () => {
    setShowForm(false);
    setReviewText('');
  };

  const handleSubmitReview = () => {
    if (reviewText.trim() === '') {
      alert('Please enter a review.');
      return;
    }

    setIsLoading(true);

    const reviewData = {
      user_id: user.id,
      car_id: carId,
      review_text: reviewText,
    };

    fetch(`/cars/${carId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviewData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to add review');
        }
        return response.json();
      })
      .then((rev) => {
        onAddReview(rev);
        setReviewText('');
        setShowForm(false);
        onAppendReview(rev);
      })
      .catch((error) => {
        console.error('Error adding review:', error); 
      })
      .finally(() => {
        setIsLoading(false);
      });
  };

  return (
    <div>
      <button onClick={() => setShowForm(true)}>Add Review</button>
      {showForm && (
        <div>
          <textarea
            rows='4'
            cols='50'
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            placeholder='Enter your review'
          />
          <button
            onClick={handleSubmitReview}
            disabled={isLoading}
          >
            {isLoading ? 'Submitting...' : 'Submit'}
          </button>
          <button onClick={closeForm} disabled={isLoading}>
            Cancel
          </button>
        </div>
      )}
    </div>
  );
}
export default AddReview;