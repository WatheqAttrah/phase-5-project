import React from 'react';
import CarList from './CarList';

function Home({ user }) {
  if (user) {
    return (
      <div>
        <h1>Welcome, {user.username}</h1>
        <h2>Cars List</h2>
        {/* Render the CarList component and pass the user prop */}
        <CarList user={user} />
      </div>
    );
  } else {
    return <h1>Please Login or Signup</h1>;
  }
}

export default Home;
