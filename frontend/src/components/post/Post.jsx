import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import Comment from "./Comment";
import './Post.css';

export default function Post({key, obj}) {
    const [data, setData] = React.useState(null);
    const [authorData, setAuthorData] = React.useState(null);
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(data);
  
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }


    useEffect(() => {


        const csrftoken = getCookie('csrftoken');
        const fetchData = async () => {
            try {
                // fetch the current user's UUID
                const currentauthorResponse = await fetch ('/api/utils/me/', {
                    method: 'GET',
                    headers: {
                        // 'Authorization': 'Basic ' + btoa('team24:team24'),
                        'X-CSRFToken': csrftoken,
                    }
                });

                // create url to current user'
                const currentAuthor = await currentauthorResponse.json();
                console.log("CURRENT AUTHOR: "+currentAuthor["id"]);
                
                // const currentAuthorPostURL = "http://127.0.0.1:8000/api/authors/"+currentAuthor+"/posts"
                const currentAuthorPostURL = '/api/utils/posts/'

                // this gets the current logged in author's posts
                const response = await fetch(data === null ? currentAuthorPostURL : data.next, {
                    method: 'GET',
                    headers: {
                        // 'Authorization': 'Basic ' + btoa('team24:team24'),
                        'X-CSRFToken': csrftoken,
                    }
                });
                const newData = await response.json();

                let a_data = {}
                for (var i = 0; i < newData.results.length; i++) {
                    if (!(newData.results[i].author in a_data)) {
                        // this gets the name of the poster 
                        let authorResponse = await fetch(newData.results[i].author, {
                            method: 'GET',
                            headers: {
                                // 'Authorization': 'Basic ' + btoa('team24:team24'),
                                'X-CSRFToken': csrftoken,
                            }
                        });

                        let newauthordata = await authorResponse.json();

                        a_data[newData.results[i].author] = newauthordata.displayName;
                    }
                }



                // const newAuthorData = await authorResponse.json();
                if (data === null) {
                    setAuthorData(a_data);
                    setData(newData);
                } else {
                    setAuthorData({...authorData, ...a_data});
                    setData({...data, ...newData, results: [...data.results, ...newData.results]});
                }

            } catch (error) {
                console.error(error);
            }
        };
        fetchData();

        const intervalId = setInterval(() => {
            fetchData();
        }, 1500);

        return () => clearInterval(intervalId);
    }, [data, authorData]);
    

    return (
        <div className="row" style={{display: "flex", gap: "0"}}>
            {data?.results.map((post) => (
                <div className="post" key={post.id}>
                    <a href={"/view/"+post.id} style={{ textDecoration: "none" }}>
                        <Box sx={{border: "1px solid #333333", color: "black", margin:10}}>
                            {/* <p class="authorName">{authorData.displayName}</p> */}
                            {/* <p class="authorName">{post.author}</p> */}
                            <p class="authorName">{authorData[post.author]}</p>
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