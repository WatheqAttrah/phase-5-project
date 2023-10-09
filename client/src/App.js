import React, { useState, useEffect } from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import NavBar from "./component/NavBar";
import Home from "./component/Home";
import Login from './component/Login';
import Signup from './component/Signup';
import CarList from './component/CarList';

function App() {
  const [user, setUser] = useState(null);

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
          <Route path='/cars/<inst:id>' render={() => user ? <Redirect to='/' /> : <Home setUser={setUser} />} />
          {/* Define the Route for CarList */}
          <Route path="/cars">
            <CarList user={user} />
          </Route>
        </Switch>
      </main>
    </div>
  );
}

export default App;
