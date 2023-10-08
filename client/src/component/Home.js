import React from 'react'

function Home({ user }) {
    if (user) {
        return (
            <div>
                <h1>Homepage</h1>
                <h2>Welcome to </h2>
            </div>
        )
    } else {
        return <h1>Please Login or Signup</h1>
    }
}

export default Home