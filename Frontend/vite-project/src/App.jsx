import { useState, useEffect } from 'react'
import './App.css'
import { Summarize } from './components/summarize'

function App() {
  const [loadingLinks, setLoadingLinks] = useState(true)
  const [links, setLinks] = useState(false)
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
    temp()
  }, [])
  if(loadingLinks){
    return <h1>
      <span className="loader"></span>
      Loading Links</h1>
  }
  return (
    <>
    <div className="myContainer">

      {links&& links.map((link)=>{
      return <Summarize link = {link} key={link}/>
      })}
    </div>
    </>
  )
}

export default App
