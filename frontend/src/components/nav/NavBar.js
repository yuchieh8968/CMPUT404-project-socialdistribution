import React from 'react';
import { Link } from "react-router-dom";
import "./NavBar.css";
import CreatePost from "../post/CreatePost";

const NavBar= () =>{
    return (
        <div>
            <nav>
                    <Link to='/home' className="Home"> Home </Link>
                    <Link to="/profile" className="Profile"> Profile </Link>
                    <Link to="/login" className="Login"> Log Out </Link>
                    <CreatePost />
            </nav>
        </div>
      );
}
export default NavBar;