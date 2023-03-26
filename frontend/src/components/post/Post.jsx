import React, { useEffect, useState } from "react";
import Box from '@mui/material/Box';

export default function Post({key, obj}) {

    return (
        <Box sx={{border: "1px solid #333333" }}>
            <h1>{obj.content}</h1>
        </Box>
    );
}