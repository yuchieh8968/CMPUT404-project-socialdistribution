import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import Comment from "./Comment";
import './Post.css';

export default function Post({key, obj}) {


    return (
        <div class="row">
            <div class="column post">
                <h2>Public Posts Section</h2>
                <Box sx={{border: "1px solid #333333" }}>
                    <h1>{obj.title}</h1>
                    <p>{obj.description}</p>
                </Box>
            </div>
            <div class="column comment">
                <h2>Comments Section</h2>
                <p> When you click on a post, comments appear here</p>
                <Comment postobj={obj} />
            </div>
        </div>
    );
}