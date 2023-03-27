import React from "react";

export default function ImageUploader() {
    // https://medium.com/nerd-for-tech/how-to-store-an-image-to-a-database-with-react-using-base-64-9d53147f6c4f
    // https://stackoverflow.com/questions/36580196/reactjs-base64-file-upload

    //URL: ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/image

    /* TO DO BACKEND NOT SETUP FOR IMAGE
    const url = "//service/authors/" + props.authorID  + "/posts/" + props.postID + "/image"
    const createImage = (newImage) => axios.post(url, newImage);

    const createPost = async (post) => {
        try {
        await createImage(post);
        } catch (error) {
        console.log(error.message);
        }
    };
    */

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

    };

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        const base64 = await convertToBase64(file);
        console.log(base64);
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