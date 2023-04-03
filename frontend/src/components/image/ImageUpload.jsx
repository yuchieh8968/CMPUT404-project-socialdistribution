import React, { useRef, useEffect, useState } from "react";
import axios from "axios";

export default function ImageUploader(props) {
    // https://medium.com/nerd-for-tech/how-to-store-an-image-to-a-database-with-react-using-base-64-9d53147f6c4f
    // https://stackoverflow.com/questions/36580196/reactjs-base64-file-upload

    const [postImage, setPostImage] = useState("");
    //URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/image

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
    const createPost = async () => {
        try {
          const currentAuthorResponse = await fetch('https://social-distro.herokuapp.com/api/utils/me/', {
            method: 'GET',
            headers: {
                'Authorization': 'Basic ' + btoa('team24:team24')
            }
            });
          const csrftoken = getCookie('csrftoken');
          const currentAuthor = await currentAuthorResponse.json();
          const url = 'https://social-distro.herokuapp.com/api/authors/'+ currentAuthor.id +'/posts/'
          const data = {
            title: props.title,
            description: props.description,
            contentType: "image/jpeg;base64",
            content: postImage.split(',')[1],
            categories: props.tags,
            visibility: props.visibility,
            unlisted: true
          };
          await axios.post(url, data, { headers: {
            'Authorization': 'Basic ' + btoa('team24:team24'),
            'X-CSRFToken': csrftoken,}
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
        //const base64result = base64.split(',')[1];
        setPostImage(base64);
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