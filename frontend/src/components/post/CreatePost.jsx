import React, { useRef, useEffect, useState } from "react";
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
import { Cancel, Tag } from "@mui/icons-material";
import { FormControl, Stack} from "@mui/material";
import axios from "axios";


///https://blog.theashishmaurya.me/how-to-create-a-tag-input-feature-in-reactjs-and-material-ui///
const Tags = ({ data, handleDelete }) => {
  return (
    <Box
      sx={{
        background: "#283240",
        height: "100%",
        display: "flex",
        padding: "0.4rem",
        margin: "0 0.5rem 0 0",
        justifyContent: "center",
        alignContent: "center",
        color: "#ffffff",
      }}
    >
      <Stack direction='row' gap={1}>
        <Typography>{data}</Typography>
        <Cancel
          sx={{ cursor: "pointer" }}
          onClick={() => {
            handleDelete(data);
          }}
        />
      </Stack>
    </Box>
  );
};

export default function CreatePost() {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [contentType, setContentType] = useState('text/plain');
    const [content, setContent] = useState("");
    const [visibility, setVisibility] = React.useState("PUBLIC");
    const [open, setOpen] = React.useState(false);
    const [tags, SetTags] = useState([]);
    const tagRef = useRef();

    const handleDelete = (value) => {
      const newtags = tags.filter((val) => val !== value);
      SetTags(newtags);
    };
    const handleOnSubmit = (e) => {
      e.preventDefault();
      SetTags([...tags, tagRef.current.value]);
      tagRef.current.value = "";
    };

    // TO DO AXIOS API CALL
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
    
    async function handleSubmit() {
        const csrftoken = getCookie('csrftoken');
        const currentAuthorResponse = await fetch('/api/utils/me/', {
        method: 'GET',
        headers: {
            'Authorization': 'Basic ' + btoa('team24:team24'),
            'X-CSRFToken': csrftoken,
        }
        });

        const currentAuthor = await currentAuthorResponse.json();
        // console.log(currentAuthor)

        const url = '/api/authors/'+ currentAuthor["id"] +'/posts/'
        const data = {
            title: title,
            description: description,
            contentType: contentType,
            content: content,
            categories: tags,
            visibility: visibility,
        };
        axios
        .post(url, data, {
            headers: {
                'Authorization': 'Basic ' + btoa('team24:team24'),
                'X-CSRFToken': csrftoken,
            }
        }).then((response) => {
            console.log(response);
        }).catch((error) => {
        if( error.response ){
            console.log(error.response.data); // => the response payload
        }
    });
    }

    const handleTitleInput = event => {
        setTitle(event.target.value);
    };

    const handleDescriptionInput = event => {
        setDescription(event.target.value);
    };

    const handleContentInput = event => {
        setContent(event.target.value);
    };

    const handleChange = (event, newVisibility) => {
        if (newVisibility !== null){
            setVisibility(newVisibility);
        }
    };

    const handleTypeChange = (event, newVisibility) => {
        if (newVisibility !== null){
            setContentType(newVisibility);
        }
    };

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = (event, reason) => {
        if (reason && reason == "backdropClick") {
            return;
        }
        setTitle("");
        setDescription("");
        setContent("");
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

                            <TextField
                                required
                                fullWidth
                                id="title"
                                label="Post Title"
                                variant="outlined"
                                margin="normal"
                                aria-label="Title of Post"
                                value= {title}
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
                                aria-label="Description of Post"
                                value= {description}
                                onChange= {handleDescriptionInput}
                                inputProps={{ maxLength: 250 }}
                            />
                            <ToggleButtonGroup
                                color="primary"
                                value={contentType}
                                exclusive
                                onChange={handleTypeChange}
                                aria-label="Post's Content Type Choices"
                                sx={{paddingTop: 2, paddingBottom:2}}
                            >
                                <ToggleButton value="text/plain">Plain</ToggleButton>
                                <ToggleButton value="text/markdown">Markdown</ToggleButton>
                            </ToggleButtonGroup>
                            <TextField
                                fullWidth
                                multiline
                                rows={4}
                                id="content"
                                label="Content"
                                variant="outlined"
                                margin="normal"
                                aria-label="Content of Post"
                                value= {content}
                                onChange= {handleContentInput}
                                inputProps={{ maxLength: 250 }}
                            />
                            <form onSubmit={handleOnSubmit}>
                                <TextField
                                inputRef={tagRef}
                                fullWidth
                                variant='standard'
                                size='small'
                                sx={{ margin: "1rem 0" }}
                                margin='none'
                                placeholder={tags.length < 5 ? "Enter tags" : ""}
                                InputProps={{
                                    startAdornment: (
                                    <Box sx={{ margin: "0 0.2rem 0 0", display: "flex" }}>
                                        {tags.map((data, index) => {
                                        return (
                                            <Tags data={data} handleDelete={handleDelete} key={index} />
                                        );
                                        })}
                                    </Box>
                                    ),
                                }}
                                />
                            </form>
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

                            <ImageUploader title={title} description={description} content={content} tags={tags} visibility={visibility} />

                            <Box  sx={{paddingTop: 2, paddingBottom:2}}>
                                <Button type="button" sx={{marginRight: 2}} onClick={handleSubmit} variant="contained" endIcon={<PublishIcon />}>
                                        Publish
                                </Button>
                                <Button type="button" onClick={handleClose} variant="contained" endIcon={<CancelIcon />}>
                                        Cancel
                                </Button>
                            </Box>
                    </Container>
                </Dialog>
            </Box>
        </>
    );
}
