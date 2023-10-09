import React, { useState, useEffect } from 'react';
import AddReview from './AddReview';
import '../index.css';

function CarCard({ make, model, year, vin, price, engine, miles, image_url, id, user }) {
  const [reviews, setReviews] = useState([]);
  const [showReviews, setShowReviews] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (showReviews) {
      setIsLoading(true);
      fetch(`/cars/${id}`)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Failed to fetch reviews");
          }
        })
        .then((car) => {
          setReviews(car.reviews);
        })
        .catch((error) => {
          console.error("Error fetching reviews:", error);
        })
        .finally(() => {
          setIsLoading(false);
        });
    }
  }, [showReviews, id]);

  function handleAddReview(newReview) {
    setReviews([...reviews, newReview]);
  }

  const toggleReviews = () => {
    if (showReviews) {
      setShowReviews(false);
    } else {
      setShowReviews(true);
    }
  };

  const cardClassName = `card ${showReviews ? 'highlighted-card' : ''}`;

  return (
    <div className={cardClassName}>
      {/* Car details */}
      {/* ... (Your existing car detail code) */}

      {/* Toggle reviews button */}
      <button onClick={toggleReviews}>
        {showReviews ? 'Hide Reviews' : 'Show Reviews'}
      </button>

      {/* Reviews section */}
      {showReviews && (
        <>
          <h4>Reviews:</h4>

          {isLoading ? (
            <p>Loading reviews...</p>
          ) : reviews.length > 0 ? (
            <ul>
              {reviews.map((review, index) => (
                <li key={index}>
                  {review.review} <small><i>Added by user: {review.user}</i></small>
                </li>
              ))}
            </ul>
          ) : (
            <p>No reviews available for this Car.</p>
          )}
          <AddReview user={user} carId={id} onAddReview={handleAddReview} />
        </>
      )}
    </div>
  );
}

export default CarCard;
