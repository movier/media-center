import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  saveVideoListData,
  selectVideoList,
 } from './videoSlice';
import './VideoList.css';
import { Link } from "react-router-dom";

/**
 * Format bytes as human-readable text.
 * 
 * @param bytes Number of bytes.
 * @param si True to use metric (SI) units, aka powers of 1000. False to use 
 *           binary (IEC), aka powers of 1024.
 * @param dp Number of decimal places to display.
 * 
 * @return Formatted string.
 */
 function humanFileSize(bytes, si=false, dp=1) {
  const thresh = si ? 1000 : 1024;

  if (Math.abs(bytes) < thresh) {
    return bytes + ' B';
  }

  const units = si 
    ? ['kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'] 
    : ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'];
  let u = -1;
  const r = 10**dp;

  do {
    bytes /= thresh;
    ++u;
  } while (Math.round(Math.abs(bytes) * r) / r >= thresh && u < units.length - 1);


  return bytes.toFixed(dp) + ' ' + units[u];
}

export default function VideoList(props) {

  const videoListData = useSelector(selectVideoList);
  const dispatch = useDispatch();

  useEffect(() => {
    if (videoListData.length > 0) return;
    fetch('/api')
      .then(response => response.json())
      .then(data => {
        console.log('response', data);
        if (data.has_error && data.error_code === 403) {
          console.log('error', data.error_message);
          const { remaining_seconds: remainingSeconds } = data.data;
          props.history.replace('/remaining-time', { remainingSeconds });
        } else {
          dispatch(saveVideoListData(data));
        }
      });
  }, []);

  const handleCheckUpdate = () => {
    fetch('/api?is_check=true')
      .then(response => response.json())
      .then(data => {
        dispatch(saveVideoListData(data));
      });
  }

  return (
    <div>
      <div style={{ marginTop: 16, textAlign: 'center' }}>
        <button onClick={handleCheckUpdate}>检查更新</button>
        <Link to="/cast">Cast</Link>
      </div>
      <div className="VideoList">
        {videoListData.map((value, index) => {
          const { uri, poster_uri, title, id, people, created_at, size } = value;
          const peopleNames = people.map(m => m.name).join(',');
          return (
            <div key={index}>
              <Link className="VideoList__link" to={`/watch?v=${uri}&id=${id}&cast=${peopleNames}`}>
                <img src={poster_uri} alt={title} />
                <p className="VideoList__title">{title}</p>
                <p className="VideoList__title">{created_at}</p>
                <p className="VideoList__title">{humanFileSize(size, true)}</p>
              </Link>
            </div>
          );
        })}
      </div>
    </div>
  );

}
