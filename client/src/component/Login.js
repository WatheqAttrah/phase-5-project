import React, { useState } from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';

function Login({ setUser }) {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const formSchema = yup.object().shape({
    username: yup.string().required('Must enter a username'),
    password: yup.string().required('Must enter a password'),
  });

  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          if (response.ok) {
            return response.json()
          }
          throw new Error('Login failed');
        })
        .then((user) => {
          setUser(user);
        })
        .catch((error) => {
          console.error('Error during login:', error);
        });
    },
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    formik.handleChange(event);
  };

  return (
    <div className="form-group">
      <h1>User Login</h1>
      <form onSubmit={formik.handleSubmit}>
        <br></br>
        <label className='label' htmlFor='username'>
          Username
        </label>
        <input
          className='input'
          id='username'
          name='username'
          type='text'
          onChange={handleInputChange}
          onBlur={formik.handleBlur}
          value={formData.username}
        />
        {formik.touched.username && formik.errors.username && (
          <p style={{ color: 'red' }}>{formik.errors.username}</p>
        )}
        <br></br>
        <label className='label' htmlFor='password'>
          Password
        </label>
        <input
          className='input'
          id='password'
          name='password'
          type='password'
          onChange={handleInputChange}
          onBlur={formik.handleBlur}
          value={formData.password}
        />
        {formik.touched.password && formik.errors.password && (
          <p style={{ color: 'red' }}>{formik.errors.password}</p>
        )}
        <br></br>
        <button className='button' type='submit' disabled={formik.isSubmitting}>
          {formik.isSubmitting ? 'Logging In...' : 'Login'}
        </button>
        <br></br>
      </form>
    </div>
  );
}

export default Login;
