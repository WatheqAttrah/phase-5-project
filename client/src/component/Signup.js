import React, { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function Signup({ setUser }) {
  // Validation using yup schema builder
  const formSchema = yup.object().shape({
    username: yup.string().required("Username is required"),
    password: yup.string().min(6, 'At least 6 characters').required("Password is required"),
    confirm: yup
      .string()
      .oneOf([yup.ref("password"), null], "Passwords must match")
      .required("Confirm Password is required"),
  });

  const formik = useFormik({
    initialValues: { username: "", password: "", confirm: "" },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((response) => {
          if (response.ok) {
            return response.json(); // Parse the JSON response
          } else {
            throw new Error("Failed to sign up"); // Handle the error case
          }
        })
        .then((user) => {
          setUser(user); // Set the user in your component state
        })
        .catch((error) => {
          console.error(error); // Handle any errors here
        });
    },
  });

  return (
    <div className="form-group">
      <h1>User Sign Up</h1>
      <br />
      <form onSubmit={formik.handleSubmit}>
        <label className='lable' htmlFor="username">Username</label>
        <br />
        <input className='input'
          id="username"
          name="username"
          type="text"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
        <p style={{ color: "red" }}>{formik.errors.username}</p>

        <label className='lable' htmlFor="password">Password</label>
        <br />
        <input className='input'
          id="password"
          name="password"
          type="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        <p style={{ color: "red" }}>{formik.errors.password}</p>

        <label className='lable'  htmlFor="password_confirmation">Confirm Password</label>
        <br />
        <input className='input'
          id="confirm"
          name="confirm"
          type="password"
          onChange={formik.handleChange}
          value={formik.values.confirm}
        />
        <p style={{ color: "red" }}>{formik.errors.confirm}</p>

        <button className='button' type="submit">Signup</button>
      </form>
    </div>
  );
}

export default Signup;
