import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';


function NavBar({ user, setUser }) {
  const history = useHistory();

  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((response) => {
      if (response.ok) {
        setUser(null);
        history.push('/logout'); // Redirect to the logout route
      }
    });
  }

  return (
    <header>
      <div activeClassName="active" >
        {user ? (
          <>
            {/* User is logged in  */}

            <NavLink to="/home" exact>
              Home
            </NavLink>
            <NavLink to="/cars" activeClassName="active" exact>
              CarList
            </NavLink>
            <NavLink to="/logout" exact onClick={handleLogoutClick}>
              Logout
            </NavLink>
          </>
        ) : (
          <>
            {/* If user not logged in  */}
            <NavLink to="/" exact>
              Home
            </NavLink>
            <NavLink to="/signup" exact>
              SignUp
            </NavLink>
            <NavLink to="/login" exact>
              Login
            </NavLink>
          </>
        )}
      </div>

    </header>
  );
}

export default NavBar;
