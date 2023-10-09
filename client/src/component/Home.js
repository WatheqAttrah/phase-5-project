import React from 'react'

function Home({ user }) {
    if (user) {
        return (
            <div>
                <h1>Welcome, {user.username} </h1>
                <h2>Cars List </h2>
            </div>
        )
    } else {
        return <h1>Please Login or Signup</h1>
    }
}

export default Home