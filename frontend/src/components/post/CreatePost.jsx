import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import Badge from '@mui/material/Badge';
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import ImageUploader from "../image/ImageUpload";
import Button from "@mui/material/Button";
import PublishIcon from '@mui/icons-material/Publish';
import CancelIcon from '@mui/icons-material/Cancel';
import CreateIcon from '@mui/icons-material/Create';
import { Dialog, Icon, IconButton } from "@mui/material";

export default function CreatePost() {
    const [titleInput, setTitleInput] = useState('');
    const [bodyInput, setBodyInput] = useState('');
    const [visibility, setVisibility] = React.useState("PUBLIC");
    const [open, setOpen] = React.useState(false);

    // TO DO AXIOS API CALL
    const handleSubmit = () => {
        console.log("Title " + titleInput);
        console.log("Body " + bodyInput);
        console.log("Visibility " + visibility);
    }

    const handleTitleInput = event => {
        setTitleInput(event.target.value);
    };

    const handleBodyInput = event => {
        setBodyInput(event.target.value);
    };

    const handleChange = (event, newVisibility) => {
        if (newVisibility !== null){
            setVisibility(newVisibility);
        }
    };

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = (event, reason) => {
        if (reason && reason == "backdropClick") {
            return;
        }
        setOpen(false);
    };


    return (
        <>
            <IconButton size="large" color="inherit">
                    <Badge>
                        <CreateIcon onClick={handleClickOpen} />
                    </Badge>
                </IconButton>

            <Box sx={{ flexGrow: 1 }}>
                <Dialog
                open={open}
                onClose={handleClose}
                fullWidth={true}
                maxWidth={'md'}
                >
                    <Container maxWidth="md">
                        <Typography sx={{paddingTop: 2, paddingBottom:2}} variant="h5" aria-label="Create A Post">
                            Create A Post
                        </Typography>
                        <form>
                            <TextField
                                fullWidth
                                id="title"
                                label="Post Title"
                                variant="outlined"
                                margin="normal"
                                aria-label="Title of Post"
                                value= {titleInput}
                                onChange= {handleTitleInput}
                                inputProps={{ maxLength: 50 }}
                            />
                            <TextField
                                fullWidth
                                multiline
                                rows={4}
                                id="description"
                                label="Description"
                                variant="outlined"
                                margin="normal"
                                aria-label="Body of Post"
                                value= {bodyInput}
                                onChange= {handleBodyInput}
                                inputProps={{ maxLength: 250 }}
                            />
                            <ToggleButtonGroup
                                color="primary"
                                value={visibility}
                                exclusive
                                onChange={handleChange}
                                aria-label="Post's Visibility Choices"
                                sx={{paddingTop: 2, paddingBottom:2}}
                            >
                                <ToggleButton value="PUBLIC">Public </ToggleButton>
                                <ToggleButton value="PRIVATE">Private</ToggleButton>
                            </ToggleButtonGroup>
                        </form>

                        <ImageUploader />
                        <Box  sx={{paddingTop: 2, paddingBottom:2}}>
                            <Button sx={{marginRight: 2}} onClick={handleSubmit} variant="contained" endIcon={<PublishIcon />}>
                                    Publish
                            </Button>
                            <Button onClick={handleClose} variant="contained" endIcon={<CancelIcon />}>
                                    Cancel
                            </Button>
                        </Box>
                    </Container>
                </Dialog>
            </Box>
        </>
    );
}
