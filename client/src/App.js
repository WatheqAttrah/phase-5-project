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
    // Check the user session on the server-side
    fetch("/check_session")
      .then((response) => {
        if (response.status === 200) {
          // Parse the JSON response
          return response.json();
        } else {
          // Handle non-200 status codes here (e.g., session expired)
          throw new Error("Session expired or server error");
        }
      })
      .then((user) => {
        // Set the user in the component's state
        setUser(user);
      })
      .catch((error) => {
        // Handle errors here (e.g., network issues, server errors)
        console.error(error);
      });
  }, []);

  return (
    <div>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
          <Route exact path='/' component={Home} />
          <Route path='/login' render={() => user ? <Redirect to='/' /> : <Login setUser={setUser} />} />
          <Route path='/signup' render={() => user ? <Redirect to='/' /> : <Signup setUser={setUser} />} />
          <Route path='/post' render={() => user ? <Post user={user} /> : <Redirect to='/login' />} />
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
