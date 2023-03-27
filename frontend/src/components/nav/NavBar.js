import * as React from 'react';
import { useNavigate } from "react-router-dom";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Badge from '@mui/material/Badge';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import Avatar from '@mui/material/Avatar';
import MailIcon from '@mui/icons-material/Mail';
import InboxIcon from '@mui/icons-material/Inbox';
import LogoDevIcon from '@mui/icons-material/LogoDev';
import CreateIcon from '@mui/icons-material/Create';
import BottomNavigation from '@mui/material/BottomNavigation';
import Paper from '@mui/material/Paper';
import CreatePost from "../post/CreatePost";

export default function NavBar() {
// Following this source code: https://github.com/mui/material-ui/blob/v5.11.14/docs/data/material/components/app-bar/PrimarySearchAppBar.js
// From this doc: https://mui.com/material-ui/react-app-bar/

    const navigate = useNavigate();

    // TO DO, USE API CALLS TO GET THE NUMBER OF NEW COMMENTS AND LIKES IN INBOX
    const [inboxNotification, setInboxNotification] = React.useState(15);
    // TO DO, USE API CALLS TO GET THE NUMBER OF NEW PRIVATE POSTS IN INBOX
    const [postNotification, setPostNotification] = React.useState(6);

    const [anchorEl, setAnchorEl] = React.useState(null);
    const [mobileMoreAnchorEl, setMobileMoreAnchorEl] = React.useState(null);

    const isMenuOpen = Boolean(anchorEl);

    const handleProfileMenuOpen = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMobileMenuClose = () => {
        setMobileMoreAnchorEl(null);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
        handleMobileMenuClose();
    };

    const handleProfileClick = () => {
        let path = '/Profile';
        navigate(path);
    }

    const handleLogOutClick = () => {
        // TO DO: LOG OUT USER
        let path = '/Login';
        navigate(path);
    }

    const handleMobileMenuOpen = (event) => {
        setMobileMoreAnchorEl(event.currentTarget);
    };

    const menuId = 'accountMenu';
    const renderMenu = (
        <Menu
            anchorEl={anchorEl}
            anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
            }}
            id={menuId}
            keepMounted
            transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
            }}
            open={isMenuOpen}
            onClose={handleMenuClose}
            >
            <MenuItem onClick={handleProfileClick}>Profile</MenuItem>
            <MenuItem onClick={handleLogOutClick}>Log Out</MenuItem>
        </Menu>
    );
    return (
        <>
            <Box sx={{ flexGrow: 1}}>
                <AppBar sx={{ pl: 10, pr: 10, pt: 1, pb: 1, backgroundColor: "#086C96" }} position="static">
                    <Toolbar>
                        <LogoDevIcon sx={{ fontSize: 60, display: { xs: 'none', md: 'flex' }, mr: 1 }} />
                        <Typography
                            variant="h6"
                            noWrap
                            component="a"
                            href="/Home"
                            sx={{
                            mr: 2,
                            display: { xs: 'none', md: 'flex' },
                            fontFamily: 'monospace',
                            fontWeight: 700,
                            letterSpacing: '.3rem',
                            color: 'inherit',
                            textDecoration: 'none',
                            }}
                        >
                            Team 24
                        </Typography>

                        <Box id="Spacer" sx={{ flexGrow: 1 }} />

                        <Box sx={{ display: { xs: 'none', md: 'flex' }}}>
                            <IconButton size="large" aria-label="show new comments and likes" color="inherit">
                                <Badge badgeContent={inboxNotification} color="error">
                                    <InboxIcon />
                                </Badge>
                            </IconButton>

                            <IconButton size="large" aria-label="show new private post" color="inherit">
                                <Badge badgeContent={postNotification} color="error">
                                    <MailIcon />
                                </Badge>
                            </IconButton>

                            <CreatePost/>

                            <IconButton
                                size="large"
                                edge="end"
                                aria-label="account of current user"
                                aria-controls={menuId}
                                aria-haspopup="true"
                                onClick={handleProfileMenuOpen}
                                color="inherit"
                                >
                                <Avatar sx={{bgcolor: "#CC2614"}}> N </Avatar>
                            </IconButton>
                        </Box>
                    </Toolbar>
                </AppBar>
                {renderMenu}
            </Box>
            <Box>
                <Paper sx={{ position: 'fixed', bottom: 0, left: 0, right: 0 }}>
                    <BottomNavigation sx={{ pl: 10, pr: 10, pt: 1, pb: 1, backgroundColor: "#086C96" }} />
                </Paper>
            </Box>
        </>
    );
}
