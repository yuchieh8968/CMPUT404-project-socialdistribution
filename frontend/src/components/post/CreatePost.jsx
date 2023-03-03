import React, { useEffect, useState } from "react";
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import ImageUploader from "../image/ImageUpload";
import Button from "@mui/material/Button";
import PublishIcon from '@mui/icons-material/Publish';
import CancelIcon from '@mui/icons-material/Cancel';
import { Dialog } from "@mui/material";

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

    // Exclusive Selection for Post's visibility
    // https://mui.com/material-ui/react-toggle-button/#exclusive-selection
    // FIX THIS IT CAN BE NULL WHEN YOU CLICK AGAIN ON THE BUTTON HIGHLIGHTED
    const handleChange = (event, newVisibility) => {
        setVisibility(newVisibility);
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

    const submitButton = {
        backgroundColor: "#2b2b2b",
        color: "white"
    };

    return (
        <>
            <Button variant="outlined" onClick={handleClickOpen} style={submitButton} >
                CREATE A POST
            </Button>
            <Dialog
            open={open}
            onClose={handleClose}
            fullWidth={true}
            maxWidth={'md'}
            >
                <Container maxWidth="md">
                    <Typography variant="h5" aria-label="Create A Post">
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
                        />
                        <TextField
                            fullWidth
                            multiline
                            rows={8}
                            id="description"
                            label="Description"
                            variant="outlined"
                            margin="normal"
                            aria-label="Body of Post"
                            value= {bodyInput}
                            onChange= {handleBodyInput}

                        />
                        <ToggleButtonGroup
                            color="primary"
                            value={visibility}
                            exclusive
                            onChange={handleChange}
                            aria-label="Post's Visibility Choices"
                        >
                            <ToggleButton value="PUBLIC">Public </ToggleButton>
                            <ToggleButton value="PRIVATE">Private</ToggleButton>
                        </ToggleButtonGroup>
                    </form>

                    <ImageUploader />

                    <Button onClick={handleSubmit} variant="contained" endIcon={<PublishIcon />}>
                            Publish
                    </Button>
                    <Button onClick={handleClose} variant="contained" endIcon={<CancelIcon />}>
                            Cancel
                    </Button>
                </Container>
            </Dialog>
        </>
    );
}
