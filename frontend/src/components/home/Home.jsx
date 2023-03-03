import React, { useEffect, useState } from "react"
import NavBar from "../nav/NavBar";
import CreatePost from "../post/CreatePost";

export default function Home() {

    return (
        <div>
            <NavBar />
            <h2> WELCOME </h2>
            <CreatePost />
        </div>
    );
}
