// Car.js
import React, { useState, useEffect } from 'react';

function Car() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    // Fetch all cars from the server
    fetch('/cars')
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        throw new Error('Failed to fetch cars');
      })
      .then((data) => {
        setCars(data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>All Cars</h1>
      {cars.length === 0 ? (
        <p>No cars available.</p>
      ) : (
        <ul>
          {cars.map((car) => (
            <li key={car.id}>
              <h2>Car Information</h2>
              <p>Make: {car.make}</p>
              <p>model: {car.model}</p>
              <p>Price: {car.price}</p>
              <p>Miles: {car.miles}</p>
              <p>VIN: {car.vin}</p>
              <p>Engine: {car.engine}</p>
              <p>Year: {car.year}</p>
              <img src={car.image} alt={`${car.make} ${car.model}`} />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Car;
