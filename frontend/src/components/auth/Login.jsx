import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Login.css";


// https://sst.dev/chapters/create-a-login-page.html

export default function Login() {
    " State variables, stores the user inputs"
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function validateForm() {
        return email.length > 0 && password.length > 0;
    }

    const navigate = useNavigate();

    function handleSubmit(event) {
        event.preventDefault();
        navigate("/home");
    }
    function handleSignUp(event) {
        navigate("/signup");
    }
    return (
        <Container>

            <Form className="Login">
                <img className="Logo" src="" alt=""/>
                <h1>Sign In</h1>
                <Form.Group size="lg" controlId="email">
                <Form.Label>Email</Form.Label>
                <Form.Control
                    autoFocus
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                </Form.Group>
                <Form.Group size="lg" controlId="password">
                <Form.Label>Password</Form.Label>
                <Form.Control
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                </Form.Group>
                <Button onClick={handleSubmit} block="true" size="lg" type="submit" disabled={!validateForm()}>
                    Submit
                </Button>
                <Button onClick={handleSignUp}>
                    Sign Up
                </Button>
            </Form>
        </Container>
      );
}