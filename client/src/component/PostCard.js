import React from 'react'

function PostCard({ user, id, title, description }) {


  return (
    <div>
      <p>Id: <b>{id}</b></p>
      <p>Title: <b>{title}</b></p>
      <p>Description: <b>{description}</b></p>
    </div>
  )
}

export default PostCard
