import React, { useRef, useEffect, useState } from "react";
import axios from "axios";

export default function ImageUploader(props) {
    // https://medium.com/nerd-for-tech/how-to-store-an-image-to-a-database-with-react-using-base-64-9d53147f6c4f
    // https://stackoverflow.com/questions/36580196/reactjs-base64-file-upload

    const [postImage, setPostImage] = useState("");
    //URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/image


    const url = "http://127.0.0.1:8000/api/authors/32e4e404-cb69-4f2f-9bfc-1bbdbc318bc7/posts/"
    const data = {
      title: props.title,
      description: props.description,
      contentType: "application/base64",
      content: postImage,
      categories: props.tags,
      visibility: props.visibility,
      unlisted: true
    };

    const createPost = async () => {
        try {
        await axios.post(url, data, { headers: {
          'Authorization': 'Basic ' + btoa('test_user:password'),}
        })
        } catch (error) {
        console.log(error.message);
        }
    };


    const convertToBase64 = (file) => {
        return new Promise((resolve, reject) => {
          const fileReader = new FileReader();
          fileReader.readAsDataURL(file)
          fileReader.onload = () => {
            resolve(fileReader.result);
          }
          fileReader.onerror = (error) => {
            reject(error);
          }
        })
      }

    const handleSubmit = (e) => {
        e.preventDefault();
        createPost(postImage);
    };

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        const base64 = await convertToBase64(file);
        //https://stackoverflow.com/questions/24289182/how-to-strip-type-from-javascript-filereader-base64-string
        const base64result = base64.split(',')[1];
        setPostImage(base64result);
    };

    return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          label="Image"
          name="myFile"
          accept="image/*" //https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/accept#unique_file_type_specifiers
          onChange={(e) => handleFileUpload(e)}
        />

        <button>Upload Image</button>
      </form>
    </div>


  );
}