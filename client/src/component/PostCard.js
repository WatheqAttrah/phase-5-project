import React from 'react';

function PostCard({ id, title, description }) {
  return (
    <div className="post-card">
      <h2 className="post-title">{title}</h2>
      <p className="post-description">{description}</p>
      <p className="post-id">ID: {id}</p>
    </div>
  );
}

export default PostCard;
