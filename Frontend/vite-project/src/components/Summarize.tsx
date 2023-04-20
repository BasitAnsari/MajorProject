import React, { useEffect, useState } from 'react'

export const Summarize = (link) => {
    const [summarizing, setSummarizing] = useState(true)
    const [summary, setSummary] = useState(null)
    useEffect(() => {
        const fetchSummary = async (link) => {
            const options = { 
                method:"POST",
                body: JSON.stringify({'link':link.link}),
                headers: {
                  "Content-Type": "application/json",
                  // 'Content-Type': 'application/x-www-form-urlencoded',
                },
              }
              const summaryRequest = await fetch('http://127.0.0.1:8000/api/summarizer/',options)
              const summary = await summaryRequest.json()
              setSummary(summary.summary_text)
              setSummarizing(false)
        }
        fetchSummary(link)
    }, [])
  return (
    <div className='row justify-content-center p-4 rounded'>
                    <div className="col-12 loadingItem justify-content-center align-items-center d-flex">
                        {summarizing ? <h3 className='d-inline'>Summarizing.....</h3> : <p>{summary}</p>}
                    
                    </div>
                    </div>
  )
}
