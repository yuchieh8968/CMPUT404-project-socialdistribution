import React, { useState, useEffect, useRef } from 'react';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import Badge from '@mui/material/Badge';
import NotificationsIcon from '@mui/icons-material/Notifications';
import { Button, Icon, IconButton } from '@mui/material';
import { Link } from 'react-router-dom';




export default function InboxNotificationDropdown() {
  const [data, setData] = React.useState(null);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(data);

  useEffect(() => {
      const fetchData = async () => {
          try {
                // fetch the current user's UUID
                const currentauthorResponse = await fetch ('/api/utils/me/', {
                    method: 'GET',
                    headers: {
                        'Authorization': 'Basic ' + btoa('team24:team24')
                    }
                });

                // create url to current user'
                const currentAuthor = await currentauthorResponse.json();
                
                const currentAuthorURL = "/api/authors/"+currentAuthor+"/inbox"
                const response = await fetch(currentAuthorURL, {
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


  const anchorRef = useRef(null);

  return (
      <IconButton>

          <Badge badgeContent={data && data.results.length} color="error">
              <NotificationsIcon
                  aria-label="show new notifications"
                  color="green"
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
                  // Update ***** multple obj
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
      </IconButton>
  );
}