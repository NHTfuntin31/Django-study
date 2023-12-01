import { useState } from 'react'
import CoursesLogin from './pages/Corses_login'
import CoursesRegister from './pages/Course_register'

function App() {
  const [isLogin, setIsLogin] = useState(false)
  return (
    <>
      { !isLogin ?
        <> 
            <CoursesLogin />
            <button onClick={() => setIsLogin(!isLogin)}>dangki?</button>
        </>
        :
        <> 
          <CoursesRegister />
          <button onClick={() => setIsLogin(!isLogin)}>dangnhap?</button>
        </>
      }
    </>
  )
}

export default App
