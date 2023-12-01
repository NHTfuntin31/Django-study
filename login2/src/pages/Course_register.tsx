import { useState } from "react"
import { InputField, LoginButton, LoginContainer, LoginForm } from "./LoginForm"
import { CourseRegister } from "../api/courseApi"


const CoursesRegister = () => {
   const [username, setUsername] = useState('')
   const [password, setPassword] = useState('')
   const [email, setEmail] = useState('')

   const handleRegister = (e: any) => {
      e.preventDefault();
      CourseRegister({username, email, password})
   }

   return(
      <>
         <LoginContainer>
            <LoginForm onSubmit={handleRegister}>
               <InputField
                  type="text"
                  placeholder="Username"
                  value={username}
                  onChange={(e: any) => setUsername(e.target.value)}
               />
               <InputField
                  type="text"
                  placeholder="Email"
                  value={email}
                  onChange={(e: any) => setEmail(e.target.value)}
               />
               <InputField
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e: any) => setPassword(e.target.value)}
               />
               <LoginButton type="submit">Register</LoginButton>
            </LoginForm>
         </LoginContainer>
      </>
   )
}

export default CoursesRegister