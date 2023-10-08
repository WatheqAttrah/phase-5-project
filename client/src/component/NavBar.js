import React from 'react';
import { NavLink } from 'react-router-dom';



function NavBar({ user, setUser }) {
  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((response) => {
      if (response.ok) {
        setUser(null);
      }
    });
  }

  return (
    <header>
      <div>
        {user ? (
          <>
            <NavLink to="/home" exact>
              Home
            </NavLink>
            <NavLink to="/posts" exact>
              Posts
            </NavLink>
            <NavLink to="/logout" exact onClick={handleLogoutClick}>
              Logout
            </NavLink>
            <NavLink to="/Car" exact>
              Car
            </NavLink>
          </>
        ) : (
          <>
            <NavLink to="/" exact>
              Home
            </NavLink>
            <NavLink to="/signup" exact>
              Signup
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
