import React, { useState } from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';



function Login({ setUser }) {

    const formSchema = yup.object().shape({
        username: yup.string().required('Must enter a username'),
        password: yup.string().required('Must enter a password'),
    });

    const formik = useFormik({
        initialValues: { username: '', password: '', },

        validationSchema: formSchema,

        onSubmit: (values) => {
            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(values)
            })
                .then((response) => {
                    if (response.ok) {
                        response.json().then((user) => setUser(user))
                    }
                })
        }
    })

    return (
        <div>
            <h1>User Login</h1>
            <form onSubmit={formik.handleSubmit}>
                <label htmlFor='username'>username</label>
                <input id='username' name='username' type='text' onChange={formik.handleChange} value={formik.values.username} />
                <br></br>
                <label htmlFor='password'>password</label>
                <input id='password' name='password' type='password' onChange={formik.handleChange} value={formik.values.password} />

                <button type='submit'>Login</button>
            </form>
        </div>
    )
}




export default Login