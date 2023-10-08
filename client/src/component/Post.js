import React, { useState, useEffect } from 'react'
import PostCard from './PostCard'


function Post({ user }) {

  const [posts, setPosts] = useState([])

  useEffect(() => {
    fetch('/posts')
      .then(r => r.json())
      .then(post => setPosts(post))
  }, [])




  return (
    <div>
      <h1>Welcome to your </h1>
      {posts.map(post => (
        <PostCard user={user} key={post.id} id={post.id} title={post.title} description={post.description} />

      )
      )}

    </div>
  )
}

export default Post
