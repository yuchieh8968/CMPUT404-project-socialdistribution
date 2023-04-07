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
            const csrftoken = getCookie('csrftoken');
            // UPDATE ***** get rid of hardcode
            //   const response = await fetch('https://social-distro.herokuapp.com/api/authors/dc17b761-567e-4202-b79d-919ede05e420/inbox', {
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
            console.log(currentAuthor["id"])

            const currentAuthorURL = "/api/authors/"+currentAuthor["id"]+"/inbox"
            const response = await fetch(currentAuthorURL, {
                  method: 'GET',
                  headers: {
                    //   'Authorization': 'Basic ' + btoa('team24:team24'),
                      'X-CSRFToken': csrftoken,
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
                      {item.type === 'post' && (
                        <Link to={"https://social-distro.herokuapp.com/view/"+item.object}>You have received a new post</Link>
                      )}
                      {item.type === 'comment' && (
                        <Link to={item.object}>You have recieved a new comment</Link>
                      )}
                      {item.type === 'like' && (
                        <Link to={item.object}>You have recieved a new like</Link>
                      )}
                      {item.type === 'follow' && (
                        <Link to={item.object}>You have a new follow request</Link>
                      )}
                    </MenuItem>
                  </Link>
              ))}
          </Menu>
      </IconButton>
  );
}