import './App.css';
import React, { useState, useEffect } from 'react'
import { Route, Switch } from 'react-router-dom'
import NavBar from "./component/NavBar"
import Home from "./component/Home"
import Post from './component/Post'
import Login from './component/Login'
import Signup from './component/Signup'




function App() {
  const [user, setUser] = useState(null)


  useEffect(() => {
    fetch('/check_session')
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
        {user ? (
          <Switch>
            <Route path='/'>
              <Home user={user} />
              <Post user={user} />
            </Route>
          </Switch>
        ) : (
          <Switch>
            <Route path='/signup'>
              <Signup setUser={setUser} />
            </Route>
            <Route path='/login'>
              <Login setUser={setUser} />
            </Route>
            <Route NewPost='/Post'>
              <Home />
            </Route>
            <Route path='/'>
              <Home />
            </Route>
          </Switch>
        )
        }
      </main>
    </div>
  )
}

export default App
