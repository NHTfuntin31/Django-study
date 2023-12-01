import { useState } from "react"
import { InputField, LoginButton, LoginContainer, LoginForm } from "./LoginForm"
import { CourseLogin } from "../api/courseApi"


const CoursesLogin = () => {
   const [username, setUsername] = useState('')
   const [password, setPassword] = useState('')

   const handleLogin = (e: any) => {
      e.preventDefault();
      CourseLogin({username, password})
   }

   return(
      <>
         <LoginContainer>
            <LoginForm onSubmit={handleLogin}>
               <InputField
                  type="text"
                  placeholder="Username"
                  value={username}
                  onChange={(e: any) => setUsername(e.target.value)}
               />
               <InputField
                  type="password"
                  placeholder="Password"
                  value={password}
                  onChange={(e: any) => setPassword(e.target.value)}
               />
               <LoginButton type="submit">Login</LoginButton>
            </LoginForm>
         </LoginContainer>
      </>
   )
}

export default CoursesLogin