import React, { useState, useEffect, useRef } from 'react';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import InboxIcon from '@mui/icons-material/Inbox';
import Badge from '@mui/material/Badge';
import NotificationsIcon from '@mui/icons-material/Notifications';
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';




export default function InboxNotificationDropdown() {
  const [data, setData] = React.useState(null);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(data);

  const fetchData = async () => {
      const response = await fetch('/api/authors/<str:author_id>/inbox');
      const json = await response.json();
      setData(json);
  }

  useEffect(() => {
      const fetchData = async () => {
          try {
            // UPDATE ***** get rid of hardcode
              const response = await fetch('http://127.0.0.1:8000/api/authors/6f48a898-82b9-49ff-b0fb-6a965545b1b6/inbox', {
                  method: 'GET',
                  headers: {
                      'Authorization': 'Basic ' + btoa('team24:team24')
                  }
              });
              const data = await response.json();
              setData(data);
          } catch (error) {
              console.error(error);
          }
      };
      fetchData();
  }, []);

  const handleClick = (event) => {
      setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
      setAnchorEl(null);
  };

  console.log(data);

  const anchorRef = useRef(null);

  return (
      <>
          <Badge badgeContent={data && data.results.length} color="secondary">
              <NotificationsIcon
                  aria-label="show new notifications"
                  color="inherit"
                  onClick={handleClick}
                  size="large"
                  ref={anchorRef}
              >
              </NotificationsIcon>
          </Badge>
          <Menu
              data={data}
              anchorEl={anchorEl}
              open={Boolean(anchorEl)}
              onClose={handleClose}
              anchorReference="anchorEl"
              anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'center',
              }}
              transformOrigin={{
                  vertical: 'top',
                  horizontal: 'center',
              }}
          >
              {data && data.results.map((item) => (
                  // Update ***** to check item type and multple 
                  <Link to={item.object}>
                  <MenuItem key={item.object}>
                    {item.type === 'Post' && (
                      <Link to={item.object}>You have received a new post</Link>
                    )}
                    {item.type === 'Comment' && (
                      <Link to={item.object}>You have recieved a new comment</Link>
                    )}
                    {item.type === 'Like' && (
                      <Link to={item.object}>You have recieved a new like</Link>
                    )}
                    {item.type === 'FollowRequest' && (
                      <Link to={item.object}>You have a new follow request</Link>
                    )}
                  </MenuItem>
                </Link>
              ))}
          </Menu>
      </>
  );
}