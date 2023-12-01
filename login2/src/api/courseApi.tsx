import React from "react"
import axios from 'axios';

export const clientID = import.meta.env.VITE_CLIENT_ID;
export const clientSecret = import.meta.env.VITE_CLIENT_SECRET;
export const grantType = import.meta.env.VITE_GRANT_TYPE;

interface Login {
   username: string;
   password: string;
}

interface Register {
   username: string;
   password: string;
   email: string;
}

const CourseLogin: React.FC<Login> = ({username, password}) => {
   const loginData = new FormData();
      loginData.append('username', username);
      loginData.append('password', password);
      loginData.append('client_id', clientID);
      loginData.append('client_secret', clientSecret);
      loginData.append('grant_type', grantType);

   console.log(clientID, clientSecret, grantType);
   
   
   let resData;
   axios.post('http://localhost:8080/o/token/', loginData, {
      headers: {
         'Content-Type': 'multipart/form-data',
       },
      withCredentials: true,
    })
   .then(res => {
      resData = res.data
      console.log(res.data);
   })
   .catch(err => {
      resData = err
   })
   console.log(resData);
   return resData
}
const CourseRegister: React.FC<Register> = ({username, email, password}) => {
   // const registerData = {
   //    'username': username,
   //    'email': email,
   //    'password': password
   // }
   const registerData = new FormData();
      registerData.append('username', username);
      registerData.append('email', email);
      registerData.append('password', password);
   let resData;
   axios.post('http://localhost:8080/user/', registerData, {
      headers: {
         'Content-Type': 'multipart/form-data',
       },
      withCredentials: true,
    })
   .then(res => {
      resData = res
      console.log(res.data);
   })
   .catch(err => {
      resData = err
   })
   return resData
}

export {
   CourseLogin,
   CourseRegister
}