import React, { useState } from "react"
import { useFormik } from 'formik'
import * as yup from 'yup'

function Signup({ setUser }) {
  // Validation using yup schema builder
  const formSchema = yup.object().shape({
    username: yup.string().required('Username is required').max(15, '15 characters max'),
    password: yup.string().min(6, 'at least 6 characters').required('Password is required'),
    confirm: yup.string().oneOf([yup.ref('password'), null], 'Passwords must match').required('Confirm Password is required'),
    })

  const formik = useFormik({
    initialValues: {username: '', password: '', confirm: '',},

    validationSchema: formSchema,

    onSubmit: (values) => {
    fetch('/signup', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
        })
    .then(r=> {
        if (r.ok) {
        r.json()
        .then(u=> setUser(u))
            }
        })
    }
    })

    return (
        <div>
          <h1>User Signup</h1>
          <br />
          <form onSubmit={formik.handleSubmit}>
            <label htmlFor='username'>Username</label>
            <br />
            <input id='username' name='username' type='text' onChange={formik.handleChange} value={formik.values.username}/>
            <p style={{ color: 'red' }}>{formik.errors.username}</p>
    
            <label htmlFor='password'>Password</label>
            <br />
            <input id='password' name='password' type='password' onChange={formik.handleChange} value={formik.values.password}/>
            <p style={{ color: 'red' }}>{formik.errors.password}</p>
    
            <label htmlFor='password_confirmation'>Confirm Password</label>
            <br />
            <input id='confirm' name='confirm' type='password' onChange={formik.handleChange} value={formik.values.confirm}/>
            <p style={{ color: 'red' }}>{formik.errors.confirm}</p>
            
            <button type='submit'>Signup</button>        
          </form>
        </div>
      )
    }
    
    export default Signup