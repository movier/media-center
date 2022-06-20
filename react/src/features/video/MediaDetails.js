import React, { useState, useEffect } from 'react';
import '../../App.css';
import { useDispatch } from 'react-redux';
import { removeVideo } from './videoSlice';
import { removeVideoFromPeople } from '../cast/castSlice';
import './MediaDetails.css';

export default function MediaDetails(props) {

  const searchParams = new URLSearchParams(props.location.search);
  const id = searchParams.get('id');

  const [cast, setCast] = useState(searchParams.get('cast').split(','));
  const [newCast, setNewCast] = useState('');
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');
  const [mediaDetails, setMediaDetails] = useState(null);

  useEffect(() => {
    fetch(`/api/media/${id}`)
      .then(response => response.json())
      .then(data => {
        setMediaDetails(data);
      });
  }, []);

  const dispatch = useDispatch();

  const handleDeleteButtonClicked = () => {
    if (window.confirm("Are you sure to delete this video?")) {
      fetch(`/api/media/${id}`, {
        method: 'DELETE'
      }).then(() => {
        dispatch(removeVideo(id));
        dispatch(removeVideoFromPeople(id));
        props.history.goBack();
      });
    }
  }

  const handleAddCastButtonClick = () => {
    if (!newCast) return;
    const data = { cast_name: newCast };
    fetch(`/api/media/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }).then(() => {
      setCast(cast.concat(newCast));
      setNewCast('');
    })
  }

  const handleConfirmButtonClick = () => {
    if (!start || !end) return;
    const input = searchParams.get('v');
    const [name, suffix] = input.split('.');
    const output = `${name}_copy.${suffix}`;
    const data = {
      input,
      output,
      start,
      end,
    };
    const favicon = document.getElementById('favicon');
    favicon.href = process.env.PUBLIC_URL + '/loading.gif';
    fetch('/api/ffmpeg', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    }).then(() => {
      favicon.href = process.env.PUBLIC_URL + '/favicon.ico';
    });
  }

  function renderMedia(media) {
    switch (media.media_type) {
      case 1:
        return <img className="media" src={media.uri} />;
      case 2:
        return (
          <video className="media" controls autoPlay>
            <source src={media.uri} />
          </video>
        );
      default:
        return <h1>Unknown Media Type</h1>; 
    }
  }

  function handleBackBtnClicked() {
    props.history.goBack();
  }

  if (!mediaDetails) return null;
  return (
    <div className="media-container">
      {renderMedia(mediaDetails)}
      <div className='operation-container'>
        <div className="operation-container__inner">
          <div className="icon-container" onClick={handleBackBtnClicked}>
            <span className="material-symbols-outlined">arrow_back</span>
          </div>
          <div className="icon-container" onClick={handleDeleteButtonClicked}>
            <span className="material-symbols-outlined">delete</span>
          </div>
        </div>
        {/* <div>
          {cast.map((m, i) => (
            <span style={{ marginRight: 10 }} key={i}>{m}</span>
          ))}
        </div>
        <div>
          <span>New Cast:</span>
          <input type="text" value={newCast} onChange={e => setNewCast(e.target.value)} />
          <button onClick={handleAddCastButtonClick}>Add Cast</button>
        </div>
        <div>
          <span>Start:</span>
          <input type="text" value={start} onChange={e => setStart(e.target.value)} />
          <span>End:</span>
          <input type="text" value={end} onChange={e => setEnd(e.target.value)} />
          <button onClick={handleConfirmButtonClick}>Confirm</button>
        </div> */}
      </div>
    </div>
  );

}
