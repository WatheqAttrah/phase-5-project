import React, { useState } from 'react';

function AddReview({ carId, onAddReview, user, onAppendReview }) {
  const [reviewData, setReviewData] = useState({
    showForm: false,
    reviewText: '',
    isLoading: false,
  });

  const closeForm = () => {
    setReviewData({ ...reviewData, showForm: false, reviewText: '' });
  };

  const handleChangeReviewText = (e) => {
    setReviewData({ ...reviewData, reviewText: e.target.value });
  };

  const handleSubmitReview = () => {
    const { reviewText } = reviewData;

    if (reviewText.trim() === '') {
      alert('Please enter a review.');
      return;
    }

    setReviewData({ ...reviewData, isLoading: true });

    const newReview = {
      user_id: user.id,
      car_id: carId,
      review_text: reviewText,
    };

    fetch(`/cars/${carId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newReview),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to add review');
        }
        return response.json();
      })
      .then((rev) => {
        onAddReview(rev);
        setReviewData({ ...reviewData, reviewText: '', showForm: false });
        onAppendReview(rev);
      })
      .catch((error) => {
        console.error('Error adding review:', error);
        alert('Failed to add review. Please try again later.');
      })
      .finally(() => {
        setReviewData({ ...reviewData, isLoading: false });
      });
  };

  return (
    <div>
      <button onClick={() => setReviewData({ ...reviewData, showForm: true })}>Add Review</button>
      {reviewData.showForm && (
        <div>
          <textarea
            rows='4'
            cols='50'
            value={reviewData.reviewText}
            onChange={handleChangeReviewText}
            placeholder='Enter your review'
          />
          <button
            onClick={handleSubmitReview}
            disabled={reviewData.isLoading}
          >
            {reviewData.isLoading ? 'Submitting...' : 'Submit'}
          </button>
          <button onClick={closeForm} disabled={reviewData.isLoading}>
            Cancel
          </button>
        </div>
      )}
    </div>
  );
}

export default AddReview;
