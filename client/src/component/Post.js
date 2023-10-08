import React, { useState, useEffect } from 'react';
import PostCard from './PostCard';

function Post() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // Fetch all posts from the server
    fetch('/posts')
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        throw new Error('Failed to fetch posts');
      })
      .then((data) => {
        setPosts(data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>All Posts</h1>
      {posts.length === 0 ? (
        <p>No posts available.</p>
      ) : (
        <div>
          {posts.map((post) => (
            <PostCard
              title={post.title}
              description={post.description}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Post;
