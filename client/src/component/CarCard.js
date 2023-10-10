import React, { useState, useEffect } from 'react';
import AddReview from './AddReview';
import '../index.css';

function CarCard({ make, model, year, vin, price, engine, miles, image_url, id, user }) {
  const [reviews, setReviews] = useState([]);
  const [showReviews, setShowReviews] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (showReviews) {
      // Reset error and start loading
      setError(null);
      setIsLoading(true);

      // Fetch reviews for the car
      fetch(`/cars/${id}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to fetch reviews");
          }
          return response.json();
        })
        .then((car) => {
          setReviews(car.reviews);
        })
        .catch((error) => {
          console.error("Error fetching reviews:", error);
          setError("Failed to fetch reviews. Please try again later.");
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
    setShowReviews(!showReviews);
  };

  const cardClassName = `card ${showReviews ? 'highlighted-card' : ''}`;

  return (
    <div className="form-group">
      <p>Make: <b>{make}</b></p>
      <p>Model: <b>{model}</b></p>
      <p>Year: <b>{year}</b></p>
      <p>Price: <b>{price}</b></p>
      <p>VIN: <b>{vin}</b></p>
      <p>Engine: <b>{engine}</b></p>
      <p>Miles: <b>{miles}</b></p>
      <p>ID: <b>{id}</b></p>
      <p>Image URL: <b>{image_url}</b></p>

      <button onClick={toggleReviews}>
        {showReviews ? 'Hide Reviews' : 'Show Reviews'}
      </button>

      {showReviews && (
        <>
          <h4>Reviews:</h4>

          {isLoading ? (
            <p>Loading reviews...</p>
          ) : error ? (
            <p className="error">{error}</p> // Display error message with a CSS class
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

          {/* Pass necessary props to the AddReview component */}
          <AddReview user={user} carId={id} onAddReview={handleAddReview} />
        </>
      )}
    </div>
  );
}

export default CarCard;
