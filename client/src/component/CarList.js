import React, { useState, useEffect } from 'react';
import CarCard from './CarCard';

function CarList({ user }) {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    fetch('/cars')
      .then(response => response.json())
      .then(cars => setCars(cars));
  }, []);

  return (
    <div>
      {cars.map(car => (
        <CarCard
          user={user}
          key={car.id} // Use car.id as the key
          id={car.id}
          make={car.make}
          model={car.model}
          year={car.year}
          vin={car.vin}
          engine={car.engine}
          price={car.price}
          image_url={car.image_url} // Use image_url to match the prop name
        />
      ))}
    </div>
  );
}

export default CarList;
