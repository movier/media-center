import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  saveVideoListData,
  selectVideoList,
 } from './videoSlice';
import './MediaList.css';
import { Link } from "react-router-dom";
import MediaCell from '../../common/MediaCell';
import axios from 'axios';

export default function MediaList(props) {

  const videoListData = useSelector(selectVideoList);
  const dispatch = useDispatch();
  const [selectedFile, setSelectedFile] = useState([]);

  function loadData() {
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
  }

  useEffect(() => {
    if (videoListData.length > 0) return;
    loadData(); 
  }, []);

  const handleCheckUpdate = () => {
    fetch('/api?is_check=true')
      .then(response => response.json())
      .then(data => {
        dispatch(saveVideoListData(data));
      });
  }

  const onFileChange = event => {
    setSelectedFile([...event.target.files]);
  };

  async function onFileUpload() {
    const formData = new FormData();
    selectedFile.forEach(file => {
      formData.append("file", file); 
    });
    const config = {
      onUploadProgress: progressEvent => console.log(progressEvent.loaded)
    };
    await axios.post("api/media", formData, config);
    loadData();
  };

  return (
    <div>
      <div style={{ margin: 16, textAlign: 'center' }}>
        <input type="file" onChange={onFileChange} multiple />
        <span style={{ cursor: 'pointer' }} className="material-symbols-outlined" onClick={onFileUpload}>file_upload</span>
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
