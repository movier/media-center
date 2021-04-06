import React, { useState, useEffect } from 'react';
import './VideoList.css';
import { Link } from "react-router-dom";

export default function VideoList(props) {

  let initialData = [];
  const data = localStorage.getItem('data');
  if (data) {
    initialData = JSON.parse(data);
  }
  
  const [ videoList, setVideoList ] = useState(initialData);

  useEffect(() => {
    if (videoList.length > 0) return;
    fetch('/api')
      .then(response => response.json())
      .then(data => {
        console.log('response', data);
        if (data.has_error && data.error_code === 403) {
          console.log('error', data.error_message);
          const { remaining_seconds: remainingSeconds } = data.data;
          props.history.replace('/remaining-time', { remainingSeconds });
        } else {
          localStorage.setItem('data', JSON.stringify(data));
          setVideoList(data);
        }
      });
  }, []);

  const handleCheckUpdate = () => {
    fetch('/api?is_check=true')
      .then(response => response.json())
      .then(data => {
        localStorage.setItem('data', JSON.stringify(data));
        setVideoList(data);
      });
  }

  return (
    <div>
      <div style={{ marginTop: 16, textAlign: 'center' }}>
        <button onClick={handleCheckUpdate}>检查更新</button>
        <Link to="/cast">Cast</Link>
      </div>
      <div className="VideoList">
        {videoList.map((value, index) => {
          const { uri, poster_uri, title, id, cast } = value;
          const castNames = cast.map(m => m.name).join(',');
          return (
            <div key={index}>
              <Link className="VideoList__link" to={`/watch?v=${uri}&id=${id}&cast=${castNames}`}>
                <img src={poster_uri} alt={title} />
                <p className="VideoList__title">{title}</p>
              </Link>
            </div>
          );
        })}
      </div>
    </div>
  );

}
