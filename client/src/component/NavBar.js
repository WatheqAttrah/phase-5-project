import React from 'react'
import { NavLink } from 'react-router-dom'

function NavBar({ user, setUser }) {

    function handleLogoutClick() {
        fetch("/logout", { method: "DELETE" }).then((r) => {
            if (r.ok) {
                setUser(null)
            }
        });
    }
    return (
        <header>
            <div>
                {user ? (
                    <NavLink to="/logout" exact onClick={handleLogoutClick}>Logout</NavLink>
                ) : (
                    <>
                        <NavLink to="/" exact>Home</NavLink>
                        <NavLink to="/signup" exact>Logout</NavLink>
                        <NavLink to="/login" exact>Login</NavLink>

                    </>
                )}
            </div>
        </header>
    )
}

export default NavBar
