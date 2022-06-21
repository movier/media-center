import React, { useEffect } from 'react';
// import './VideoList.css';
import { useSelector, useDispatch } from 'react-redux';
import {
  saveCastListData,
  selectCastList,
 } from './castSlice';
import MediaCell from '../../common/MediaCell';

export default function CastList() {

  const castListData = useSelector(selectCastList);
  const dispatch = useDispatch();

  useEffect(() => {
    if (castListData.length > 0) return;
    fetch('/api/cast')
      .then(response => response.json())
      .then(data => {
        dispatch(saveCastListData(data));
      });
  }, []);

  return (
    <div>
      {castListData.map((cast, cast_index) => {
        const { name, media } = cast;
        return (
          <div key={cast_index}>
            <div style={{ color: 'white' }}>{name}</div>
            <div className="VideoList">
              {media.map((value, index) => {
                return <MediaCell key={index} media={value} />;
              })}
            </div>
          </div>
        );
      })}
    </div>
  );

}
