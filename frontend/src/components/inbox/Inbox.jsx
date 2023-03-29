import React, { useState, useEffect } from 'react';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import InboxIcon from '@mui/icons-material/Inbox';
import Badge from '@mui/material/Badge';
import NotificationsIcon from '@mui/icons-material/Notifications';
import { Button } from '@mui/material';

export default function InboxNotificationDropdown() {
    const [data, setData] = React.useState(null);
    const open = Boolean(data);

    const fetchData = async () => {
        const response = await fetch('/api/authors/<str:author_id>/inbox');
        const json = await response.json();
        setData(json);
      }

    console.log(data); // print the response data to the console

    useEffect(() => {
      fetch('http://127.0.0.1:8000/api/authors/7427ff62-5d48-4bb9-91b3-3816a4487afe/posts/de3bc74a-a1a3-4a49-ba5b-d63875d6a027')
          .then(response => response.json())
          .then(data => {
          console.log(data); // print the response data to the console
          setData(data); // set the post data state variable to the response data
          });
  }, []);

    const handleClick = (event) => {
        setData(event.currentTarget);
    };

    const handleClose = () => {
        setData(null);
    };

    return (
        
      <>
          <InboxIcon
          aria-label="show new notifications"
          color="inherit"
          onClick={handleClick}
          size="large" 
          >

          
          <Badge badgeContent={4} color="error">
              <NotificationsIcon />
          </Badge>
          </InboxIcon>
          <Menu
          data={data}
          open={open}
          onClose={handleClose}
          MenuListProps={{
              'aria-labelledby': 'basic-button',
          }}
          >
          <MenuItem onClick={handleClose}>
            You received a like 
          </MenuItem>
          <MenuItem onClick={handleClose}>
            You received a new comment
          </MenuItem>
          <MenuItem onClick={handleClose}>
            You received a post 
          </MenuItem>
          </Menu>
      </>
  )
  
}

