import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  saveVideoListData,
  selectVideoList,
 } from './videoSlice';
import './MediaList.css';
import { Link } from "react-router-dom";
import MediaCell from '../../common/MediaCell';

export default function MediaList(props) {

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
      <div style={{ margin: 16, textAlign: 'center' }}>
        <span style={{ cursor: 'pointer' }} className="material-symbols-outlined">file_upload</span>
        <span style={{ margin: '0 20px', cursor: 'pointer' }} className="material-symbols-outlined" onClick={handleCheckUpdate}>sync</span>
        <Link to="/cast"><span style={{ color: 'white' }}  className="material-symbols-outlined">familiar_face_and_zone</span></Link>
      </div>
      <div className="MediaList">
        {videoListData.map((value, index) => {
          return <MediaCell key={index} media={value} />;
        })}
      </div>
    </div>
  );

}
