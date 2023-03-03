import React from 'react';
import { Link } from "react-router-dom";
import "./NavBar.css";

const NavBar= () =>{
    return (
        <div>
            <nav>
                    <Link to='/home' className="Home"> Home </Link>
                    <Link to="/inbox" className="Inbox"> Inbox </Link>
                    <Link to="/login" className="Login"> Log Out </Link>
            </nav>
        </div>
      );
}
export default NavBar;