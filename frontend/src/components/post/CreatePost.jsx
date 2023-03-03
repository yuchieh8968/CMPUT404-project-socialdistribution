import React, { useEffect, useState } from "react";
import Container from '@mui/material/Container';
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import ImageUploader from "../image/ImageUpload";
import { Button } from "@mui/material";


export default function CreatePost() {
    const [visibility, setVisibility] = React.useState("PUBLIC");

    // Exclusive Selection for Post's visibility
    // https://mui.com/material-ui/react-toggle-button/#exclusive-selection
    const handleChange = (event, newVisibility) => {
        setVisibility(newVisibility);
    };

    return (
        <Container maxWidth="md">
            <Typography variant="h5" aria-label="Create A Post">
                Create A Post
            </Typography>
        <form>
            <TextField fullWidth id="title" label="Post Title" variant="outlined"  margin="normal" aria-label="Title of Post"/>
            <TextField fullWidth multiline rows={8} id="description" label="Description" variant="outlined"  margin="normal" aria-label="Description of Post" />
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

        <Button> Submit </Button>

        </Container>
    );
}
