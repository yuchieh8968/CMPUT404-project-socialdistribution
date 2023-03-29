import React, { useState, useEffect } from 'react';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import InboxIcon from '@mui/icons-material/Inbox';
import Badge from '@mui/material/Badge';
import NotificationsIcon from '@mui/icons-material/Notifications';

export default function InboxNotificationDropdown() {
    const [data, setData] = React.useState(null);
    const open = Boolean(data);

    const fetchData = async () => {
        const response = await fetch('/api/inbox-data/');
        const json = await response.json();
        setData(json);
      }

    useEffect(() => {
        fetch('http://localhost:8000/api/get_post_data/')
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

    console.log(data)

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
    );
}

