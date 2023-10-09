import React, { useState } from 'react'

function AddReview({ car, onAddReview, user, onAppendReview }) {
  const [showForm, setShowForm] = useState(false)
  const [reviewText, setReviewText] = useState('')

  const closeForm = () => {
    setShowForm(false)
    setReviewText('')
    }
    
  //add a review to specific book reviews
  const handleSubmitReview = () => {
      if (reviewText.trim() === '') {
          alert('Please enter a review.')
          return
      }
      // data object
      const reviewData = {user_id: user.id, car_id: car.id, review_text: reviewText}

      fetch(`/cars/${car.id}`,{
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(reviewData),
      })
      .then(response=> response.json())
      .then((review)=> {
        onAddReview(review) 
        setReviewText('') //clear form
        setShowForm(false) //close form
        onAppendReview(review) // append review to reviews
      })
      .catch((error) => console.error('Error adding review:', error))
  }

  return (
    <div>
      <button onClick={()=> setShowForm(true)}>Add Review</button>
      {showForm && (
        <div>
          <textarea rows='4' cols='50' value={reviewText} onChange={e=> setReviewText(e.target.value)} placeholder='Enter your review'/>
          <button onClick={handleSubmitReview}>Submit</button>
          <button onClick={closeForm}>Cancel</button>
        </div>  
      )}
    </div>
  )
}


export default AddReview;

