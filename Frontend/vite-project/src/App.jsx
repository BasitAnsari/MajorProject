import { useState, useEffect } from 'react'
import './App.css'
import { Summarize } from './components/summarize'
import {useAutoAnimate} from '@formkit/auto-animate/react'
function App() {
  const [loadingLinks, setLoadingLinks] = useState(true)
  const [links, setLinks] = useState(false)
  const [animationParent] = useAutoAnimate()
  useEffect(() => {
    const temp = async () => {
      const request = await fetch("https://ipinfo.io/json?token=693e5e55cdfd64")
      const jsonResponse = await request.json()
      const options = { 
        method:"POST",
        body: JSON.stringify({'query':jsonResponse.city}),
        headers: {
          "Content-Type": "application/json",
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
      const linksRequest = await fetch('http://127.0.0.1:8000/api/link/',options)
      const res = await linksRequest.json()
      const links = JSON.parse(res).links
      setLinks(links)
      setLoadingLinks(false)
    }
    if (navigator.geolocation) {
      temp()
    } else {
    alert('Sorry Not available!');
    }
  }, [])
  return (
    <>
    <div className='myContainer' ref={animationParent}>
    <nav className="navbar navbar-expand-lg bg-body-tertiary p-0 m-0">
  <div className="container-fluid p-0 m-0">
    <a className="navbar-brand" href="#">News Chomps</a>
  </div>
</nav>
    {loadingLinks ? 
      <div className='d-flex w-100 justify-content-center align-items-center' style={{height:"100vh"}}>
        <h1 className='d-inline'>
          <span className="loader"></span>
          <span className='magic'>
          Loading Links 
          </span>
        </h1>
      </div> :
      <div className="row mx-5 justify-content-center" ref={animationParent}>
        {links.map((link)=>{
          return <Summarize link = {link} key={link}/>
        })}
      </div>
        }
    </div>
    </>
  )
}

export default App
