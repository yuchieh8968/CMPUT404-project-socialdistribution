import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import Comment from "./Comment";
import './Post.css';

export default function Post({key, obj}) {
    const [data, setData] = React.useState(null);
    const [authorData, setAuthorData] = React.useState(null);
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(data);
  
    useEffect(() => {
      if (data === null) {
        const fetchData = async () => {
          try {
            const response = await fetch('http://127.0.0.1:8000/api/authors/26e38fc5-abf2-468a-ad9b-e91699dc89dc/posts', {
              method: 'GET',
              headers: {
                'Authorization': 'Basic ' + btoa('jeff:pw')
              }
            });
            const data = await response.json();
            setData(data);
            // fetch the author data
            const authorResponse = await fetch(data.author, {
              method: 'GET',
              headers: {
                'Authorization': 'Basic ' + btoa('jeff:pw')
              }
            });
            const authorData = await authorResponse.json();
            setAuthorData(authorData);
          } catch (error) {
            console.error(error);
          }
        };
        fetchData();
      }
    }, [data]);

    return (
        <div class="row">
            {data?.results.map((post) => (
                <div className="column post" key={post.id}>
                    <a href={post.id} style={{ textDecoration: "none" }}>
                        <Box sx={{border: "1px solid #333333", color: "black"}}>
                            <p>{post.author}</p>
                            <h1>{post.title}</h1>
                            <p>{post.content}</p>
                            <p>{new Date(post.published).toLocaleString()}</p>
                        </Box>
                    </a>
                </div>
            ))}
        </div>
    );
}