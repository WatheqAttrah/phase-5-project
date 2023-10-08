import './App.css';
import React, { useState, useEffect } from 'react'
import { Route, Switch, Redirect } from 'react-router-dom'
import NavBar from "./component/NavBar"
import Home from "./component/Home"
import Post from './component/Post'
import Login from './component/Login'
import Signup from './component/Signup'
import Car from './component/Car';



function App() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    // Check the user session on server-side
    fetch("/check_session")
      .then((response) => {
        if (response.status === 200) {
          response.json().then((user) => setUser(user));
        }
      });
  }, [])

  return (
    <div>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
          <Route exact path='/' component={Home} />
          <Route path='/login' render={() => user ? <Redirect to='/' /> : <Login setUser={setUser} />} />
          <Route path='/signup' render={() => user ? <Redirect to='/' /> : <Signup setUser={setUser} />} />
          <Route path='/post' render={() => user ? <Post user={user} /> : <Redirect to='/login' />} />
          {/* <Route path='/newpost' component={NewPost} /> */}
          <Route path='/posts' component={Post} />
          <Route path='/Car' component={Car} />
          <Route path='/'>
            <Home user={user} />
          </Route>
        </Switch>
      </main>
    </div>
  )
}

export default App
